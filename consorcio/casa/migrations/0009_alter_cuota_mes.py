# Generated by Django 4.0.5 on 2022-07-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casa', '0008_inquilino_vigencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuota',
            name='mes',
            field=models.CharField(choices=[('01', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], default='enero', max_length=15),
        ),
    ]