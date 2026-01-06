from django.db import models

# Create your models here.

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.TextField(max_length=100)
    person_name = models.TextField(max_length=50)
    cau_chuc = models.TextField(max_length=1000)
    loai_thiep = models.TextField(max_length=10)

    class Meta:
        managed = True
        db_table = 'info'