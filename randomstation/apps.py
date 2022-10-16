from django.apps import AppConfig
import os, json
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class RandomstationConfig(AppConfig):
    name = 'randomstation'
    verbose_name = 'Random Station'

    # App 구동 시 Open API 호출 데이터 저장
    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            self.save()


    # 서울 지하철 정보 가져오기
    def get_all_contents(self):
        start_index = 1
        end_index = 10 # 최대 1000건 제한
        url = self.make_url(start_index, end_index)
        contents = self.call_api(url)
        # self.append_all_contents(start_index, end_index, contents)
        return contents

    # Open API 호출
    def call_api(self, url):
        response = requests.get(url)
        return json.loads(response.content.decode('utf-8'))['SearchSTNBySubwayLineInfo']


	# Open API URL 생성
    def make_url(self, start_index, end_index):
        secrets = json.loads(open(os.path.join(BASE_DIR, 'secrets.json')).read())
        service_key = secrets['SERVICE_KEY']
        return f'http://openapi.seoul.go.kr:8088/{service_key}/json/SearchSTNBySubwayLineInfo/{str(start_index)}/{str(end_index)}/'


	# 컨텐츠 끝까지 Append
    def append_all_contents(self, start_index, end_index, contents):
        if contents['list_total_count'] > end_index:
            start_index += end_index
            end_index *= 2
            url = self.make_url(start_index, end_index)
            next_contents = self.call_api(url)
            contents['row'].append(next_contents['row'])
            self.append_all_contents(start_index, end_index, next_contents)

    def save(self):
        from randomstation.models import Station
        from randomstation.serializers import StationSerializer

        all_contents = self.get_all_contents()
        for (order, content) in enumerate(all_contents['row']):
            name = content['STATION_NM']
            line = content['LINE_NUM']
            station = Station(name=name, line=line, order=order)
            print(f'station={station}')
            
            ## TODO: 데이터 저장하기
            # serializer = StationSerializer(data={"name": name, "line": line, "order": order})
            # print(f'{serializer}')
