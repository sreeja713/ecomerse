# Generated by Django 4.0.3 on 2022-03-30 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0007_alter_product_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
    ]
