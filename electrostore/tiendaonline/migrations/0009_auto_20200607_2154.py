# Generated by Django 3.0.5 on 2020-06-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaonline', '0008_auto_20200607_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=3000),
        ),
    ]