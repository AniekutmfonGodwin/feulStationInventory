from django.contrib import admin

# Register your models here.
from tank.models import Tank


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    pass
    

