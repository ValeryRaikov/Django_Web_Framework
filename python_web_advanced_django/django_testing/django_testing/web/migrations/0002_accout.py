# Generated by Django 5.1.3 on 2024-11-17 15:35

import django.db.models.deletion
import django_testing.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, validators=[django_testing.web.validators.check_username_containes_only_alphanumerics])),
                ('password', models.CharField(max_length=16)),
                ('is_banned', models.BooleanField(blank=True, default=False, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.profile')),
            ],
        ),
    ]
