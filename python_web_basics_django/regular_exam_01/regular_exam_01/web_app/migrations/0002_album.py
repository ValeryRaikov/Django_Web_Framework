# Generated by Django 5.0.6 on 2024-06-25 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Pop Music', 'Pop'), ('Jazz Music', 'Jazz'), ('R&B Music', 'R B'), ('Rock Music', 'Rock'), ('Country Music', 'Country'), ('Dance Music', 'Dance'), ('Hip Hop Music', 'Hip Hop'), ('Other', 'Other')], max_length=13)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
