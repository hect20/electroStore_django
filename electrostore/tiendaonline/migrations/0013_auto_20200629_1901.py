# Generated by Django 3.0.5 on 2020-06-29 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaonline', '0012_auto_20200629_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagen',
            old_name='imagen',
            new_name='nombreArchivo',
        ),
    ]
