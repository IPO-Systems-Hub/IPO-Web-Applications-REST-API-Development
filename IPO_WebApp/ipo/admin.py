from django.contrib import admin
from .models import Company, IPO, MarketPrice

admin.site.register(Company)
admin.site.register(IPO)
admin.site.register(MarketPrice)
