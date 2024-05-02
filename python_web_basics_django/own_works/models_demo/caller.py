# This is a test file for basic queries related to the models

import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_demo.settings")
django.setup()

from models_demo.vehicles.models import Dealership, RepairStation, VehicleOwner


def display_all_dealerships():
    dealerships = Dealership.objects.all()

    return '\n'.join([str(d) for d in dealerships])


def display_filtered_dealerships():
    dealerships = Dealership.objects.filter(
        location='Sofia',
    )

    return '\n'.join([str(d) for d in dealerships])


def display_repair_stations():
    repair_stations = RepairStation.objects.filter(
        address__icontains='zh.k.',
    )

    return '\n'.join([
        f'Repair station {rs.name} from {rs.location} with address: {rs.address}'
        for rs in repair_stations
    ])


def display_owners():
    owners = VehicleOwner.objects.filter(city__in=['Sofia', 'Plovdiv',])

    if not owners:
        return 'No owners from Sofia or Plovdiv'

    return '\n'.join(str(o) for o in owners)


def get_owner_by_phone_number():
    owner = VehicleOwner.objects.get(phone_number='0887111899',)

    if owner is None:
        return 'No owner found'

    return str(owner)


def get_first_owner():
    owner = VehicleOwner.objects.first()

    if owner.city != 'Sofia':
        return 'Not from Sofia'


def update_first_owner():
    owner = VehicleOwner.objects.first()

    if owner:
        owner.city = 'Pomorie'
        owner.save()
        return f'{str(owner)} from {owner.city}'

    return 'No VehicleOwner found'


# print(display_all_dealerships())
# print(display_filtered_dealerships())
# print(display_repair_stations())
# print(display_owners())
# print(get_owner_by_phone_number())
# print(get_first_owner())
# print(update_first_owner())
