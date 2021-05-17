from django.db import models


# Create your models here.

class Service(models.Model):
    nom = models.CharField(max_length= 200)
    icone = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom

class Genre(models.Model):
    OPTIONS = [
        ('H', 'homme'),
        ('F', 'femme'),
        ('A', 'all')
    ]
    genre = models.CharField(max_length= 200, choices= OPTIONS)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return f"genre {self.id}"

class Article(models.Model):
    name = models.CharField(max_length=200)
    picture = models.FileField()
    taille = models.CharField(max_length= 200)
    prix = models.FloatField()
    categorie = models.ForeignKey("Categorie_article", on_delete=models.CASCADE,related_name="article_categorie")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name= "genre_article")
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name

class Categorie_article(models.Model):
    name = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categorie_article'
        verbose_name_plural = 'Categorie_articles'

    def __str__(self):
        return self.name

class Groupe_categorie(models.Model):
    name = models.CharField(max_length=200)
    categorie_article = models.ForeignKey("Categorie_article", on_delete=models.CASCADE, related_name= "groupe_categorie_article")
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Groupe_categorie'
        verbose_name_plural = 'Groupe_categories'

    def __str__(self):
        return self.name

class Star(models.Model):

    note = models.FloatField()
    article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name= "Article_star")
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'

    def __str__(self):
        return self.user