from django.contrib import admin
from .models import Item, UserPreference

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'acidity', 'body', 'sweetness')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'acidity', 'body')
