# Generated by Django 3.2.3 on 2021-05-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehiclepart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
