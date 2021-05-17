from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "date_add", "date_update", "status")
    # search_fields = ["title"]

@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):
    list_display = ("name", "icone", "date_add", "date_update", "status")
    # search_fields = ["name"]

@admin.register(models.Siteweb)
class SitewebAdmin(admin.ModelAdmin):
    list_display = ("name_site", "date_add", "date_update", "status")
    # search_fields = ["name_site"]

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image_view', "date_add", "date_update", "status")

    def image_view(self, obj):
        return mark_safe('<img src= f"{obj.picture.url}" style ="height:50px; width:100px>')


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', "date_add", "date_update", "status")
    # search_fields = ('email',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email', "date_add", "date_update", "status")
    # search_fields = ('name',)


@admin.register(models.Marque)
class MarqueAdmin(admin.ModelAdmin):
    list_display = ('name', "date_add", "date_update", "status")
    # search_fields = ('name',)



