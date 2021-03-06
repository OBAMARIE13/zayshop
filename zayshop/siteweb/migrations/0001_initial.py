# Generated by Django 3.2.2 on 2021-05-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='images_about')),
                ('description', models.TextField()),
                ('description_service', models.TextField()),
                ('description_marque', models.TextField()),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('marque', models.FileField(upload_to='image_marque')),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Marque',
                'verbose_name_plural': 'Marques',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
        ),
        migrations.CreateModel(
            name='Siteweb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.TextField()),
                ('name_site', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('description_categorie', models.TextField()),
                ('description_produit', models.TextField()),
                ('adresse', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Siteweb',
                'verbose_name_plural': 'Siteweb',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('sous_title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('color', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sldiders',
            },
        ),
        migrations.CreateModel(
            name='Sociaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icone', models.CharField(max_length=200)),
                ('lien', models.TextField()),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Sociaux',
            },
        ),
    ]
