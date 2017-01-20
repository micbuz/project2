from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task

from .models import BillingItem, Paragon, ParagonItems
import time
import pytesseract
from PIL import Image, ImageFilter
from .image_utils import to_ogorki

@task(name='tessaract_in_action')
def items_from_image(image):
    hj=Paragon.objects.get(image=image)
    dane = pytesseract.image_to_string(Image.open(hj.image.path), lang='pol')
    dane2 = to_ogorki(dane)
    for i,j in dane2:
        p=ParagonItems(id_paragonu=hj, cena =j, produkt=i)
        p.save()
    print('id z celery', hj.id)
    hj.image_data = dane2
    hj.save()



@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
    number_1 = x
    time.sleep(5)
    number_2 = y* random.randint(3, 100)
    time.sleep(6)
    total = number_1 * number_2

    time.sleep(10)
#    new_object = BillingItem.objects.create(
 #           item_name='some item', 
  #          number_1=number_1,
   #         number_2=number_2, 
    #        total=total)

    b=BillingItem(item_name='some item',number_1=number_1,number_2=number_2,total=total)
    b.save()

    return total


@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)
