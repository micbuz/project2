from django.db import models



class BillingItem(models.Model):
    item_name = models.CharField(max_length=120, null=True, blank=True, default='Processing image... Refresh to check for results.')
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return str(self.total)



class Paragon(models.Model):
    image = models.FileField()
    image_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.image)

class ParagonItems(models.Model):
    id_paragonu =models.IntegerField(null=True, blank=True)
    cena = models.CharField(max_length=120, null=True, blank=True)
    produkt = models.CharField(max_length=120, null=True, blank=True)


