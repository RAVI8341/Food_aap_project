from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_disc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(max_length=500,default="https://media-cdn.tripadvisor.com/media/photo-s/1b/3d/36/a0/fresh-hand-stretched.jpg")