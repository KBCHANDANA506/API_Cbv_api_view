from django.db import models

# Create your models here.

class Product_Category(models.Model):
    PcId=models.IntegerField(primary_key=True)
    PcName=models.CharField(max_length=100)

    def __str__(self):
        return self.PcName


class Product(models.Model):
    PcName=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    PDate=models.DateField()


    def __str__(self):
        return self.Pname