from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, PartnerPreference,Message

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'religion', 'location', 'profession')
    search_fields = ('user__username', 'religion', 'location', 'profession')
    list_filter = ('gender', 'religion', 'location', 'profession')

@admin.register(PartnerPreference)
class PartnerPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'min_age', 'max_age', 'preferred_religion', 'preferred_location', 'preferred_profession')
    search_fields = ('user__username', 'preferred_religion', 'preferred_location', 'preferred_profession')
    list_filter = ('preferred_religion', 'preferred_location', 'preferred_profession')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=('sender', 'receiver', 'content', 'timestamp')