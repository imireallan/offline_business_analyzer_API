# Generated by Django 3.0.7 on 2020-06-15 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billpayment',
            old_name='transaction_data',
            new_name='transaction_date',
        ),
    ]
