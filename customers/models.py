from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    date_of_birth = models.DateField('Date of Birth')


class CustomersDetail(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    customer_detail_description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
