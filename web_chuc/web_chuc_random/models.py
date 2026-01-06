# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, andelete the table
# Feel free to rename the models, but don't rename db_table values or field names. d
from django.db import models


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.TextField()  # Cung cấp giá trị mặc định nếu không có giá trị
    who = models.TextField()
    loi_chuc = models.TextField(null=True, blank=True)
    loai = models.TextField(null=True, blank=True)

    class Meta:
        managed = True  # Đảm bảo Django quản lý bảng này (tạo bảng trong DB)
        db_table = 'log'  # Tên bảng trong cơ sở dữ liệu