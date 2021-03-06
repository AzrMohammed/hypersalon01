# Generated by Django 2.2.6 on 2020-11-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0009_branchservisablecategory_branchservisableproduct_branchservisableproductbase'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('is_available', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
