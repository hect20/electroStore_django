# Generated by Django 3.0.5 on 2020-06-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaonline', '0010_auto_20200629_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='nombreArchivo',
            field=models.ImageField(blank=True, default='static/default.png', null=True, upload_to='static/imgproducto'),
        ),
    ]
