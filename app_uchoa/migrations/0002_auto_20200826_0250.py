# Generated by Django 2.2 on 2020-08-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_uchoa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='atraso',
            new_name='falta',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
