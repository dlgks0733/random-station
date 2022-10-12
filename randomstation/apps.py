from django.apps import AppConfig


class RandomstationConfig(AppConfig):
    name = 'randomstation'
    verbose_name = 'Random Station'

    def ready(self):
        # TODO: Station 미존재 시 공공데이터 API Call 후, 저장
        # http://data.seoul.go.kr/dataList/OA-15442/S/1/datasetView.do
        pass