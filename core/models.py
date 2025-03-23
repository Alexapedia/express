from django.db import models
from django.urls import reverse

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='services/')
    description = models.TextField(max_length=3000)
    def __str__(self):
        return self.name 


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.name 
    

class Article(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    def __str__(self):
        return self.title 


# Quote Request 
class QuoteRequest(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    service_type = models.CharField(max_length=50, choices=[("الشحن", "الشحن"), ("التخليص الجمركي", "التخليص الجمركي")])
    # Shipping
    shipment_type = models.CharField(max_length=50, blank=True, null=True, choices=[("وثائق", "وثائق"), ("طرود", "طرود"), ("بضائع", "بضائع")])
    weight = models.FloatField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    
    # Customs Clearance
    goods_description = models.TextField(blank=True, null=True)
    customs_location = models.CharField(max_length=255, blank=True, null=True)
    
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"طلب عرض سعر من {self.name} - {self.service_type}"
