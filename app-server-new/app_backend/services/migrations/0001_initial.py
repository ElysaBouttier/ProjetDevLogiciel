# Generated by Django 3.1.4 on 2021-05-21 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issuingDate', models.DateTimeField(auto_now_add=True)),
                ('isPaid', models.BooleanField()),
                ('payementDate', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('firstName', models.CharField(max_length=40)),
                ('mail', models.CharField(max_length=80)),
                ('registrationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
                ('picture', models.CharField(max_length=80)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('idBills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.bill')),
            ],
        ),
        migrations.CreateModel(
            name='BillProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=7)),
                ('idBills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.bill')),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.product')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='idClient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.client'),
        ),
        migrations.AddField(
            model_name='bill',
            name='products',
            field=models.ManyToManyField(through='services.BillProduct', to='services.Product'),
        ),
    ]
