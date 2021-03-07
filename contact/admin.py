from django.contrib import admin
from .models import Contact, CarSourcing, EmailSubscriber
import csv
from django.shortcuts import render
from django.http import HttpResponse
from itertools import islice


# Register your models here.
def export_emails(modelAdmin, request, queryset):
    response = HttpResponse(content_type='type/csv')
    writer = csv.writer(response)
    headers = []

    # Each iteration over querysets values returns the full list of keys. 
    # So in order to write them once and use them as the header, we set a limit using islice.
    for k in islice(queryset.values(),1):
        headers += k.keys()
    writer.writerow(headers)
    
    for contact in queryset.values_list():
        writer.writerow(contact)
    response['Content-Disposition'] = 'attachment; filename="email_list.csv"'
    return response


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'submission_date')
    actions = [export_emails]


class CarSourcingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'submission_date')
    actions = [export_emails]

class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscription_start_date')
    actions = [export_emails]


 
admin.site.register(Contact, ContactAdmin)
admin.site.register(CarSourcing, CarSourcingAdmin)
admin.site.register(EmailSubscriber, EmailSubscriberAdmin)

