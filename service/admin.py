from django.contrib import admin
from .models import ServiceParent,ServiceChild,ServiceChild,ParentLocations,Location

class ServiceParentAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(ServiceParent,ServiceParentAdmin)


class ServiceChildAdmin(admin.ModelAdmin):
    list_display = ['id','name','parent_cat']

admin.site.register(ServiceChild,ServiceChildAdmin)


class ParentLocationsAdmin(admin.ModelAdmin):
    list_display = ['id','location_name','service_name']

admin.site.register(ParentLocations,ParentLocationsAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','name','parent_location','service_name']
    list_display_links = ['id','name','parent_location','service_name']
    search_fields = ['name']
    list_filter = ['name','service_name']
    

admin.site.register(Location,LocationAdmin)




