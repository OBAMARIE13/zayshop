# Generated by Django 3.2 on 2021-05-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.FileField(default=1, upload_to='ImageSlider'),
            preserve_default=False,
        ),
    ]
