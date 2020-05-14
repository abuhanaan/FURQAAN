from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
# from django.template.defaultfilters import slugify

# Create your models here.

User = get_user_model()


class Manufacturer(models.Model):
    maker = models.CharField(max_length=20)

    def __str__(self):
        return self.maker


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=15)
    maker = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    priceByDefault = models.IntegerField(default=1, blank=True)
    # slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('inventory:detail', kwargs={'pk': self.pk})

    """
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
        return super().save(*args, **kwargs)
    """


"""
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
"""


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trans_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sellPrice = models.IntegerField(default=1)
    imei = models.CharField(max_length=15)
    custName = models.CharField(max_length=50)
    custAdd = models.TextField(max_length=100)
    cusPhone = models.CharField(max_length=11, blank=True)
    custEmail = models.EmailField(blank=True)
    note = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return ("%s , %s , %s, %s" % (self.item.item_name, self.item.quantity,
                self.sellPrice, self.time))

    def get_absolute_url(self):
        return reverse('inventory:trans-detail', kwargs={'pk': self.pk})


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_assigned = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    quantity_inStock = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.item.item_name

    def get_absolute_url(self):
        return reverse('inventory:detail_cashierLog', kwargs={'pk': self.pk})
