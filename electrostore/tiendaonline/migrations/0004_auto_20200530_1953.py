# Generated by Django 3.0.5 on 2020-05-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaonline', '0003_auto_20200529_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_hora',
            field=models.DateField(auto_now=True),
        ),
    ]
