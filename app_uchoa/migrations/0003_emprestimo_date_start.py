# Generated by Django 2.2 on 2020-08-30 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_uchoa', '0002_remove_emprestimo_cobrador'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='date_start',
            field=models.DateField(default=datetime.date(2020, 8, 30)),
        ),
    ]