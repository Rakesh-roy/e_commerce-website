from django.db import models
from django.contrib.auth.models import User


class CustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ProductsModel(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.item_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def cart_total(self):
        orderitems = self.orderitemmodel_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def cart_items(self):
        orderitems = self.orderitemmodel_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddressModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

