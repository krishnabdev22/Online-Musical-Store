# Generated by Django 3.1.6 on 2021-02-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='namie',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
