from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    mail=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table='tbl_employee'
