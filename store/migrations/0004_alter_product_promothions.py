# Generated by Django 4.2.7 on 2023-11-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_collection_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promothions',
            field=models.ManyToManyField(blank=True, to='store.promotions'),
        ),
    ]
