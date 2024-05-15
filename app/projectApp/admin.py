from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')  # Fields to display in the list view
    search_fields = ('name', 'email')  # Fields to enable searching
    list_filter = ('age',)  # Filters for list view
