from django.contrib import admin
from .models import Service, Contact, Article, QuoteRequest

# Register your models here.
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Article)


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'service_type', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)