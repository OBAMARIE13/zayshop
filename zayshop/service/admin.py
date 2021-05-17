from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom','icone', "date_add", "date_update", "status")
    search_fields = ["nom"]

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',"date_add", "date_update", "status")
    
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "picture","taille", "prix","categorie", "genre","date_add", "date_update", "status")
    search_fields = ["name"]

@admin.register(models.Categorie_article)
class Categorie_articleAdmin(admin.ModelAdmin):
    list_display = ("name","date_add", "date_update", "status")
    search_fields = ["name"]

@admin.register(models.Groupe_categorie)
class Groupe_categorieAdmin(admin.ModelAdmin):
    list_display = ("name", "categorie_article","date_add", "date_update", "status")
    search_fields = ["name"]

@admin.register(models.Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ("note", "article","date_add", "date_update", "status")