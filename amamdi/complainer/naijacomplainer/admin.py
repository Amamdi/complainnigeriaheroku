from django.contrib import admin
from .models import Complainer
# Register your models here.


class ComplainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'firstname', 'lastname', 'state', 'complaintIsAgainst', 'natureOfComplaint', 'complaint',)


admin.site.site_header = "Complain Nigeria"
admin.site.register(Complainer, ComplainerAdmin)
