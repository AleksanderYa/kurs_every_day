# Generated by Django 3.2.5 on 2021-10-05 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_auto_20210826_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['-date'], 'permissions': [('monobank_currency_view', 'Can see monobanck currency'), ('privatbank_currency_view', 'Can see privatbanck currency')], 'verbose_name': 'Курс валют', 'verbose_name_plural': 'Курсы валют'},
        ),
    ]
