from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.Chardfild(max_length=15)
    red_date = models.Datetimerfield(auto_now_add=True)
    def __str__(self):
        return self.Category

# таблица для продуктов
 class Product(models.Model):
     product_name = models.CharField(max_length=75)
     product_count = models.IntegerField
     product_des = models.TextField
     product_photo = models.PhotoField
     product_price = models.FloatField
     product_category = models.ForeignKey(Category , on_delete=models.SET_NULL, null=True)





 # Таблица корзины пользователя
 class UserCart(models.Model():
    user_id = models.IntegerField
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
