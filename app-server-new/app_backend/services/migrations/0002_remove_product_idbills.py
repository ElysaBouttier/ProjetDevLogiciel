# Generated by Django 3.1.4 on 2021-05-23 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='idBills',
        ),
    ]
