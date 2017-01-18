
"""boot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from dupa import views as dupa_views
from joins import views as joins_views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dupa_views.start_page),
    url(r'^produkty/$', dupa_views.produkty, name='produkty'), 
    url(r'^email/$', joins_views.email_form, name='email'),  
   url(r'^numbers/$', dupa_views.numbers, name='numbers'),
    url(r'^paragony/', include('dupa.urls',namespace='paragony')),    
    
#    url(r'^(?P<ref_id>.*)$', joins_views.share, name='share'),
    
    
    
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


