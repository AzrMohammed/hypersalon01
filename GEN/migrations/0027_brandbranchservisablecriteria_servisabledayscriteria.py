# Generated by Django 2.2.6 on 2020-12-30 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0026_auto_20201204_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServisableDaysCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_start_time', models.DateTimeField(blank=True, null=True)),
                ('service_end_time', models.DateTimeField(blank=True, null=True)),
                ('day_of_week', models.IntegerField(choices=[(1001, 'None'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1001)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GEN.BrandBranchBasicInfo')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GEN.BrandBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='BrandBranchServisableCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GEN.BrandBranchBasicInfo')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GEN.BrandBasicInfo')),
            ],
        ),
    ]
