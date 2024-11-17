# Generated by Django 5.0.6 on 2024-06-28 08:21

import django.core.validators
import regular_exam_02.web_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Outdoor Plants', 'Op'), ('Indoor Plants', 'Ip')], max_length=14, verbose_name='Plant type:')),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinValueValidator(2), regular_exam_02.web_app.validators.validate_plant_name], verbose_name='Plant name:')),
                ('image_url', models.URLField(verbose_name='Plant image URL:')),
                ('description', models.TextField(verbose_name='Description:')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price:')),
            ],
        ),
    ]