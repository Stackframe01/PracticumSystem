# Generated by Django 3.1.5 on 2021-01-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop_system', '0003_auto_20210124_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.CharField(max_length=50000, null=True),
        ),
    ]
