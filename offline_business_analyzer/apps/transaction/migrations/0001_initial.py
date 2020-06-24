# Generated by Django 3.0.7 on 2020-06-15 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0010_auto_20200615_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.IntegerField()),
                ('status', models.CharField(choices=[('OPEN', 'open'), ('CLOSED', 'closed')], default='open', max_length=10)),
                ('supplier', models.CharField(max_length=100)),
                ('unit_amount_currency', models.DecimalField(decimal_places=4, max_digits=19)),
                ('unit_amount', models.DecimalField(decimal_places=4, max_digits=19)),
                ('total_transaction_currency', models.DecimalField(decimal_places=4, max_digits=19)),
                ('total_transaction', models.DecimalField(decimal_places=4, max_digits=19)),
                ('transaction_date', models.DateField()),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unit_amount_currency', models.DecimalField(decimal_places=4, max_digits=19)),
                ('unit_amount', models.DecimalField(decimal_places=4, max_digits=19)),
				('total_transaction_currency', models.DecimalField(decimal_places=4, max_digits=19)),
                ('total_transaction', models.DecimalField(decimal_places=4, max_digits=19)),
                ('order_id', models.IntegerField()),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('ACCEPTED', 'accepted'), ('REJECTED', 'rejected'), ('COMPLETED', 'completed')], default='pending', max_length=20)),
                ('transaction_date', models.DateField()),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Bill')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='business.Business')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('transaction_date', models.DateField()),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_payments', to='transaction.Order')),
            ],
        ),
        migrations.CreateModel(
            name='BillPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=100)),
                ('transaction_data', models.DateField()),
                ('bill_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills_payment', to='transaction.Bill')),
            ],
        ),
    ]
