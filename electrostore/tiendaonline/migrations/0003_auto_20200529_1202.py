# Generated by Django 3.0.5 on 2020-05-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaonline', '0002_auto_20200527_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_hora',
            field=models.DateField(),
        ),
    ]