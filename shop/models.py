from django.db import models
class Brand(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)
    def __str__(self):
        return self.brand_name
class Mobile(models.Model):
    mobile_name=models.CharField(max_length=120)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    price=models.IntegerField(null=False)
    model_name=models.CharField(max_length=80)
    specs=models.CharField(max_length=250)
    description=models.CharField(max_length=120)
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.model_name

class Order(models.Model):
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    user=models.CharField(max_length=120)
    choices=[
        ("ordered","ordered"),
        ("despatched","despatched"),
        ("cancelled","cancelled")
    ]
    status=models.CharField(max_length=10,choices=choices,default="ordered")

