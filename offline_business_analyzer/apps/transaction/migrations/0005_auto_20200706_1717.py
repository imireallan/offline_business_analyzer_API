# Generated by Django 3.0.7 on 2020-07-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20200706_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to='csv'),
        ),
    ]
