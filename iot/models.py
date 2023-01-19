from django.db import models

# 녹화파일 업로드
# sec_file/년도/월/일 폴더에 사진이 저장될 예정
class SecFile(models.Model):
    file_name = models.CharField(max_length=100)
    sec_file = models.FileField(upload_to="sec_file/%Y/%m/%d/")
