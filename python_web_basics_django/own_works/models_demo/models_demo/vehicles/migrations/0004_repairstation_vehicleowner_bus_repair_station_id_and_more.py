# Generated by Django 5.0.4 on 2024-05-02 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_bus_dealership_id_car_dealership_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('open_hours', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='repair_station_id',
            field=models.ManyToManyField(to='vehicles.repairstation'),
        ),
        migrations.AddField(
            model_name='car',
            name='repair_station_id',
            field=models.ManyToManyField(to='vehicles.repairstation'),
        ),
        migrations.AddField(
            model_name='motorcycle',
            name='repair_station_id',
            field=models.ManyToManyField(to='vehicles.repairstation'),
        ),
        migrations.AddField(
            model_name='truck',
            name='repair_station_id',
            field=models.ManyToManyField(to='vehicles.repairstation'),
        ),
        migrations.AddField(
            model_name='bus',
            name='vehicle_owner_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicleowner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='vehicle_owner_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicleowner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motorcycle',
            name='vehicle_owner_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicleowner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truck',
            name='vehicle_owner_id',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicleowner'),
            preserve_default=False,
        ),
    ]
