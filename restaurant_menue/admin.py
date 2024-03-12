from django.contrib import admin
from . models import Item

class RestaurantMenuAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('meal', 'status')
    search_fields = ('status', 'description')


admin.site.register(Item, RestaurantMenuAdmin)

# Register your models here.
