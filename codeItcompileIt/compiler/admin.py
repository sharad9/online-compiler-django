from django.contrib import admin
from compiler.models import Payload

# Register your models here.

class PayloadAdmin(admin.ModelAdmin):
	list_display=['userName','code','language','inputs','output'];


admin.site.register(Payload, PayloadAdmin);


