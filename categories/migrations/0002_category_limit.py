# Generated by Django 5.0.2 on 2024-03-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='limit',
            field=models.IntegerField(default=0),
        ),
    ]
