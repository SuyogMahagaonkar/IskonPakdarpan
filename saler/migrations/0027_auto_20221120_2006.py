# Generated by Django 2.2.14 on 2022-11-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0026_auto_20221115_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_GluttentFree',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_HighProtein',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_Sattvik',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_SugarFree',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_Veg',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_Vegan',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_not',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
