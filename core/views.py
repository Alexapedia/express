from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages 
from .models import Article, Contact, Service, QuoteRequest



# Home page 
def home(request):
    services = Service.objects.all()
    articles = Article.objects.all()
    return render(request, 'index.html', {'services' : services, 'articles': articles})


def services(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if not name or not phone or not email or not message:
            return render(request, 'contact.html', {'error': 'جميع الحقول مطلوبة!'})
        
        # Save to the database
        contact_message = Contact(name=name, phone=phone, email=email, message=message)
        contact_message.save()

        # If saving is successful
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})


def quotation(request):
    return render(request, 'quotation.html')



def get_quote_request(request):
    if request.method == 'GET':
        return render(request, 'quotation.html')
    
    elif request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        company = request.POST.get("company")
        service_type = request.POST.get("service_type")

        shipment_type = request.POST.get("shipment_type")
        weight = request.POST.get("weight")
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        goods_description = request.POST.get("goods_description")
        customs_location = request.POST.get("customs_location")
        notes = request.POST.get("notes")

        if not name or not phone or not service_type:
            return messages.error(request, "الاسم ورقم الهاتف ونوع الخدمة مطلوب")

        quote = QuoteRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            company=company,
            service_type=service_type,
            shipment_type=shipment_type,
            weight=weight if weight else None,
            source = source,
            destination=destination,
            goods_description=goods_description,
            customs_location=customs_location,
            notes=notes
        )

        messages.success(request, "تم تقديم طلب عرض السعر بنجاح.")
        return render(request,'quotation.html')
    return messages.error(request, 'you must use POST request for processing...')
    return render(request,'quotation.html')

