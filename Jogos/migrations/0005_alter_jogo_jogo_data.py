# Generated by Django 3.2.7 on 2021-10-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jogos', '0004_alter_jogo_jogo_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='Jogo_Data',
            field=models.DateTimeField(verbose_name='Data/Hora'),
        ),
    ]
