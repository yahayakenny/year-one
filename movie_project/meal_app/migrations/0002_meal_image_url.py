# Generated by Django 3.1.3 on 2020-11-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='image_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
