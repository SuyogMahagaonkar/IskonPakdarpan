# Generated by Django 2.2.14 on 2022-11-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0025_product_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='saler',
            field=models.CharField(default='AttiTude@admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_not',
            field=models.IntegerField(null=True),
        ),
    ]
