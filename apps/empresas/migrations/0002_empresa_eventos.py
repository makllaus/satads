# Generated by Django 2.2.5 on 2019-09-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_remove_evento_atracoes'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='eventos',
            field=models.ManyToManyField(to='eventos.Evento'),
        ),
    ]