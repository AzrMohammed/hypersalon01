# Generated by Django 2.2.6 on 2021-01-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0030_servisablestorecapacitycriteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandbranchbasicinfo',
            name='store_capacity',
            field=models.IntegerField(default=111453),
        ),
    ]