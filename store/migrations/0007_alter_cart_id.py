# Generated by Django 4.2.7 on 2023-11-24 10:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=uuid.uuid4),
        ),
    ]
