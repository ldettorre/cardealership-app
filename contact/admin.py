from django.contrib import admin
from .models import Contact, CarSourcing, EmailSubscribers
import csv
from django.shortcuts import render
from django.http import HttpResponse


# Register your models here.
def export_emails(modelAdmin, request, queryset):
    response = HttpResponse(content_type='type/csv')
    writer = csv.writer(response)
    writer.writerow(['name','email'])
    for contact in queryset.values_list('name','email'):
        writer.writerow(contact)
    response['Content-Disposition'] = 'attachment; filename="email_list.csv"'

    return response


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'submission_date')
    actions = [export_emails]


class CarSourcingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'submission_date')

class EmailSubscribersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscription_start_date')
    actions = [export_emails]
 
admin.site.register(Contact, ContactAdmin)
admin.site.register(CarSourcing, CarSourcingAdmin)
admin.site.register(EmailSubscribers, EmailSubscribersAdmin)

