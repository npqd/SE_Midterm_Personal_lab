# Generated by Django 2.2 on 2022-04-14 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Products'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Deliveried', 'Deliveried')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('In door', 'In door'), ('Out door', 'Out door')], max_length=200, null=True),
        ),
    ]
