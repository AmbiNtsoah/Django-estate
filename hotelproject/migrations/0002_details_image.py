# Generated by Django 5.0.3 on 2024-04-11 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
