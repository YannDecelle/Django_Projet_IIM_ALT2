from django.db import models

class ShopModel(models.Model):

    Product_Name = models.CharField(max_length=200)
    Product_Description = models.CharField(max_length=200)
    Product_Stock = models.IntegerField()
    Product_Price = models.CharField(max_length=200)
    Product_Image = models.URLField(default='http://www.ipsgroup.fr/wp-content/uploads/2013/12/default_image_01-1024x1024-570x321.png')

class BuyModel(models.Model):
    User_Buy = models.IntegerField()