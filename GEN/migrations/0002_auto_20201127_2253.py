# Generated by Django 2.2.6 on 2020-11-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbase',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
