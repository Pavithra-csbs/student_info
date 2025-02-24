from django.contrib import admin
from .models import OnDuty
class OnDutyAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'reason') 
    search_fields = ('student__name', 'date')
# Register your models here.
admin.site.register(OnDuty, OnDutyAdmin)