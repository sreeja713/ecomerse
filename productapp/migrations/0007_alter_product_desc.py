# Generated by Django 4.0.3 on 2022-03-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0006_alter_product_options_remove_product_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]