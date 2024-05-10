from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Dealership(models.Model):
    class Locations(models.TextChoices):
        SOFIA = 'Sofia',
        VARNA = 'Varna',
        RUSE = 'Ruse',

    name = models.CharField(
        max_length=50,
    )

    location = models.CharField(
        max_length=max(len(l) for l in [Locations.SOFIA, Locations.VARNA, Locations.RUSE]),
    )

    open_hours = models.TimeField()

    def __str__(self):
        return f'Dealership: {self.name}, {self.location}'


class RepairStation(models.Model):
    name = models.CharField(
        max_length=50,
    )

    location = models.CharField(
        max_length=50,
    )

    address = models.TextField()

    open_hours = models.TimeField()

    def __str__(self):
        return f'Repair station: {self.name} located in {self.location}'


class VehicleOwner(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    city = models.CharField(
        max_length=50,
    )

    phone_number = models.CharField(
        max_length=10,
        unique=True,
    )

    def __str__(self):
        return f'Vehicle Owner: {self.first_name} {self.last_name}'


class BaseVehicle(models.Model):
    class Engine(models.TextChoices):
        DIESEL = 'Diesel',
        PETROL = 'Petrol',
        ELECTRIC = 'Electric',

    class Category(models.TextChoices):
        A = 'Motorcycles',
        B = 'Cars'
        C = 'Micro-buses and buses'
        D = 'Trucks',
        O = 'Other',

    brand = models.CharField(
        max_length=50,
    )

    model = models.CharField(
        max_length=50,
    )

    production_date = models.DateField()

    engine_type = models.CharField(
        max_length=max(len(e) for e in [Engine.DIESEL, Engine.PETROL, Engine.ELECTRIC]),
        choices=Engine,
    )

    horse_power = models.IntegerField(
        validators=[
            MinValueValidator(60),
            MaxValueValidator(900),
        ],
    )

    category = models.CharField(
        max_length=1,
        choices=Category,
    )

    mileage = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    dealership_id = models.ForeignKey(
        to=Dealership,
        on_delete=models.CASCADE,
    )

    repair_station_id = models.ManyToManyField(
        to=RepairStation,
    )

    vehicle_owner_id = models.ForeignKey(
        to=VehicleOwner,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True,
        ordering = ['brand', 'model'],

    def __str__(self):
        return f'Vehicle: {self.brand} {self.model}'


class Motorcycle(BaseVehicle):
    category = BaseVehicle.Category.A

    def __str__(self):
        return f'Motorcycle: {self.brand} {self.model}'


class Car(BaseVehicle):
    category = BaseVehicle.Category.B

    def __str__(self):
        return f'Car: {self.brand} {self.model}'


class Bus(BaseVehicle):
    category = BaseVehicle.Category.C

    def __str__(self):
        return f'Bus: {self.brand} {self.model}'


class Truck(BaseVehicle):
    category = BaseVehicle.Category.D

    def __str__(self):
        return f'Truck: {self.brand} {self.model}'
