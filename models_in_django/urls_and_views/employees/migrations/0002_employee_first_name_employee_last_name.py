# Generated by Django 5.0.4 on 2024-04-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
