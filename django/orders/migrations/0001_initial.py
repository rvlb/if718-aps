# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 13:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnt', models.IntegerField(verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Preço pago')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MenuItem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]