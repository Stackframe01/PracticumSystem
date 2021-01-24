# Generated by Django 3.1.5 on 2021-01-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalStandart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('created', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('found_by', models.CharField(max_length=500)),
                ('job_titles', models.ManyToManyField(to='workshop_system.JobTitle')),
            ],
        ),
    ]