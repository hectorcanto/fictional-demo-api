# Generated by Django 3.2.3 on 2021-05-23 02:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_alter_vehiclepart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
