# Generated by Django 2.2.7 on 2020-07-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_amount',
        ),
    ]
