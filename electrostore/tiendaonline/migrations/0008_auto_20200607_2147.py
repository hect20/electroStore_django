# Generated by Django 3.0.5 on 2020-06-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaonline', '0007_auto_20200607_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
    ]