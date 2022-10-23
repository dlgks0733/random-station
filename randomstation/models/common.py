from datetime import datetime
from django.db import models

# 공통 모델
class BaseModel(models.Model):
	created_at = models.DateTimeField(
		auto_now_add=True,
		blank=True,
		null=False,
		verbose_name="생성 일시",
		help_text="데이터 생성 일시",
	)

	updated_at = models.DateTimeField(
		auto_now_add=True,
		blank=True,
		null=False,
		verbose_name="수정 일시",
		help_text="데이터 수정 일시",
	)

	class Meta:
		abstract = True