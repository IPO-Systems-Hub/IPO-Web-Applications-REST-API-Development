from django.db import models
from datetime import date

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)  # Optional logo
    def __str__(self):
        return self.company_name

class IPO(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price_band = models.CharField(max_length=50)  # Using CharField for flexibility
    issue_size = models.CharField(max_length=100)  # Keep it as CharField for units like 'Cr.'
    issue_type = models.CharField(max_length=50)  # Book Built or other types
    listing_date = models.DateField(null=True, blank=True)
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    rhp_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    drhp_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return f"{self.company.company_name} IPO"

class MarketPrice(models.Model):
    ipo = models.OneToOneField(IPO, on_delete=models.CASCADE)
    current_market_price = models.FloatField()
    current_return = models.FloatField()
    
    def __str__(self):
        return f"{self.ipo.company.company_name} Market Price"
