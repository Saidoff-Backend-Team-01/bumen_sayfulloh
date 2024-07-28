from django.contrib import admin

from .models import (
    FAQ,
    AppInfo,
    Contacts,
    ContactUsWeb,
    PrivacyPolicy,
    SocialMedia,
    Sponsor,
)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["address", "phone_number", "email", "location"]
    list_filter = ["address", "phone_number", "email", "location"]
    search_fields = ["phone_number"]


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["telegram", "instagram", "facebook", "linkedin"]
    list_filter = ["telegram", "instagram", "facebook", "linkedin"]


@admin.register(AppInfo)
class AppInfoAdmin(admin.ModelAdmin):
    list_display = ["title", "desc"]
    list_filter = ["title", "desc"]


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["question", "answer"]
    list_filter = ["question", "answer"]


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ["text"]


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ["image", "url"]


@admin.register(ContactUsWeb)
class ContactUsWebAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "message"]
    search_fields = ["phone_number"]
