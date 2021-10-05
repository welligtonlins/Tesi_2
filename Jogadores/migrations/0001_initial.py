# Generated by Django 3.2.7 on 2021-09-28 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Times', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jogador_Nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('Jogador_Cpf', models.CharField(max_length=14, verbose_name='Cpf')),
                ('Jogador_Gols', models.IntegerField(verbose_name='Gols')),
                ('Jogador_CartaoAmarelo', models.IntegerField(verbose_name='Cartão Amarelo')),
                ('Jogador_CartaoVermelho', models.IntegerField(verbose_name='Cartão Vermelho')),
                ('Jogador_Time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Times.time')),
            ],
        ),
    ]