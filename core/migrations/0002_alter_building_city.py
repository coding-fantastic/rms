# Generated by Django 4.2.1 on 2023-06-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
