# Generated by Django 2.2.14 on 2022-11-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0039_auto_20221121_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='allergies',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
