# Generated by Django 2.1.2 on 2018-10-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.CharField(max_length=200)),
                ('nome_cliente', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=1)),
                ('tipo', models.CharField(max_length=1)),
                ('dia_pagamento', models.IntegerField()),
            ],
        ),
    ]
