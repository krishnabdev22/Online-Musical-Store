# Generated by Django 3.1.6 on 2021-02-03 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_namie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='namie',
        ),
    ]
