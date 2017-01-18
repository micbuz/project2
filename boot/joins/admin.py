from django.contrib import admin
from .models import Join,JoinFirends

class JoinAdmin(admin.ModelAdmin):
    list_display = ['__str__','email', 'timestamp', 'updated','ip_address','ref_id']# ,'dupa','kupa']
    class Meta:
        model = Join


admin.site.register(Join, JoinAdmin)
admin.site.register(JoinFirends)


