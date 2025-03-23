from django.urls import path 
from .views import home, services, about, contact, get_quote_request, article_detail


# Url patterns 
urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('articles/<int:article_id>/', article_detail, name='article_detail'),
    path('quotation/', get_quote_request, name='quotation'),

]
