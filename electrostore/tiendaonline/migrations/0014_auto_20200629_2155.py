# Generated by Django 3.0.5 on 2020-06-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaonline', '0013_auto_20200629_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombreArchivo',
            field=models.ImageField(blank=True, null=True, upload_to='imgproducto'),
        ),
    ]
