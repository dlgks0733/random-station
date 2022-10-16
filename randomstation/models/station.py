from django.db import models
from .common import BaseModel

# 지하철 역 모델
# TODO: 필요 Field 추가
class Station(BaseModel):
	name = models.CharField(
		max_length=64,
		blank=False,
		null=False,
		verbose_name="역명",
		help_text="지하철 역명"
	)

	line = models.CharField(
		max_length=24,
		blank=False,
		null=False,
		verbose_name="호선",
		help_text="지하철 호선"
	)

	order = models.IntegerField(
		blank=False,
		null=False,
		verbose_name="순번",
		help_text="순번"
	)

	def __init__(self, name, line, order):
		self.name = name
		self.line = line
		self.order = order

class Meta:
	verbose_name="지하철 역"
	verbose_name_plural="지하철 역 목록"
	ordering = ['line']

	def __str__(self):
		return f"Station-{self.line}-{self.name}"