from django.conf.urls import url,include
from django.contrib import admin
from dupa import views as dupa_views
from joins import views as joins_views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', dupa_views.paragon_base, name='paragon_base'),
    url(r'^receipt-list/$', dupa_views.lista_paragonow, name='lista_paragonow'),
    url(r'^receipt-form/$', dupa_views.add_receipt, name='add_receipt'),
    ]
