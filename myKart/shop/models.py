from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):       # to override the default name
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35, default="")
    email = models.CharField(max_length=35, default="")
    phone = models.CharField(max_length=35, default="")
    desc = models.CharField(max_length=150, default="")

    def __str__(self):      # to override the default name
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=150)


class Tracker(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=500)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."



