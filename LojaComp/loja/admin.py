from django.contrib import admin
from .models import Pedido, Status
# Register your models here.

admin.site.register(Pedido)
admin.site.register(Status)