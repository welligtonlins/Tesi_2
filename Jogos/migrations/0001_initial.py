# Generated by Django 3.2.7 on 2021-10-04 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Campos', '0001_initial'),
        ('Juizes', '0001_initial'),
        ('Times', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jogo_Data', models.DateField(verbose_name='Data')),
                ('Jogo_Campo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campos.campo')),
                ('Jogo_Juiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juizes.juiz')),
                ('Jogo_Time', models.ManyToManyField(to='Times.Time')),
            ],
        ),
    ]