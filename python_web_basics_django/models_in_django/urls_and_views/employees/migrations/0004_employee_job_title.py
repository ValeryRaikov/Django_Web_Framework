# Generated by Django 5.0.4 on 2024-04-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_egn'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[('BackEnd-Dev', 1), ('FrontEnd-Dev', 2), ('QA', 3), ('DevOps', 4), ('Team Lead', 5)], default='', max_length=30),
            preserve_default=False,
        ),
    ]
