from django.contrib import admin
from .models import NewBuy
from .models import usedBuy
from .models import checkout

# Register your models here.
admin.site.register(NewBuy)
admin.site.register(usedBuy)
admin.site.register(checkout)