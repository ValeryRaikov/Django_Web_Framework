# Generated by Django 5.1.3 on 2024-11-17 15:24

import django_testing.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django_testing.web.validators.check_name_contains_only_letters])),
                ('last_name', models.CharField(max_length=50, validators=[django_testing.web.validators.check_name_contains_only_letters])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
