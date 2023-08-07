from django.contrib import admin
from Tester.models import *
# Register your models here.

admin.site.register(Menu)
admin.site.register(Romes_Model_API)
admin.site.register(Desk_model)
admin.site.register(Person_Room)
admin.site.register(Rating)

@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name") 
    search_fields = ("first_name__startswith", ) 