from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length= 250)
    sous_title = models.CharField(max_length= 250)
    description = models.TextField()
    color = models.BooleanField(default= False)
    image = models.FileField(upload_to='ImageSlider')
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sldiders'

    def __str__(self):
        return self.title

class Sociaux(models.Model):
    name = models.CharField(max_length= 200)
    icone = models.CharField(max_length= 200)
    lien = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Sociaux'

    def __str__(self):
        return self.name

class Siteweb(models.Model):
    copyright = models.TextField()
    name_site = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    description_categorie = models.TextField()
    description_produit = models.TextField()
    adresse = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Siteweb'
        verbose_name_plural = 'Siteweb'

    def __str__(self):
        return self.name_site


class About(models.Model):
    picture = models.FileField(upload_to='images_about')
    description = models.TextField()
    description_service = models.TextField()
    description_marque = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return f"A propos: {self.id}"

    
class Newsletter(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name

class Marque(models.Model):
    name = models.CharField(max_length=250)
    marque = models.FileField(upload_to='image_marque')
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Marque'
        verbose_name_plural = 'Marques'

    def __str__(self):
        return self.name