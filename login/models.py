from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class customer_profile(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_first_name = models.CharField(max_length=200,null=True, blank=True)
    customer_last_name = models.CharField(max_length=200,null=True, blank=True)
    customer_email = models.EmailField(max_length=200,null=True, blank=True,unique=True)
    customer_phone_number = models.CharField(max_length=200,null=True, blank=True)
    customer_address = models.CharField(max_length=200,null=True, blank=True)

class product_info(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_profile = models.ForeignKey(customer_profile, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=200,null=True, blank=True)
    product_description = models.CharField(max_length=200,null=True, blank=True)
    product_price = models.CharField(max_length=200,null=True, blank=True)
    product_id = models.CharField(max_length=200,null=True, blank=True)
    product_unit= models.IntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to='ProductImage',null=True, blank=True)
    product_status = models.IntegerField(null=True, blank=True)

class order_info(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    product_info = models.ForeignKey(product_info, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.CharField(max_length=200, null=True, blank=True)
    product_price = models.CharField(max_length=200, null=True, blank=True)
    product_id = models.CharField(max_length=200, null=True, blank=True)
    product_unit = models.IntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to='OrderImage', null=True, blank=True)
    order_status = models.CharField(max_length=200, null=True, blank=True)




