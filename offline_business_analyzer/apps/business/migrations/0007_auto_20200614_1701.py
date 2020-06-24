# Generated by Django 3.0.7 on 2020-06-14 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0006_auto_20200614_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='countries_of_operation',
            field=models.CharField(blank=True, default='United States of America', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL),
        ),
    ]
