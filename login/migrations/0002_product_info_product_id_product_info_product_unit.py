# Generated by Django 4.1.5 on 2023-03-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_info',
            name='product_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product_info',
            name='product_unit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
