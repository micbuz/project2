from django.db import models

class Join(models.Model):
    email = models.EmailField()
    ref_id = models.CharField(max_length=120, default = 'abra')
    ip_address = models.CharField(max_length=120, default='ABC')
#    dupa = models.CharField(max_length=120, default='dupa')
#    kupa = models.CharField(max_length=120, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add =True, auto_now=False)
    updated = models.DateTimeField(auto_now_add =False, auto_now=True)


    def __str__(self):
        return self.email

class JoinFirends(models.Model):
    email = models.OneToOneField(Join, related_name='Sharer')
    friends = models.ManyToManyField(Join, related_name='Friend', null=True, blank=True)

