# Generated by Django 5.0.2 on 2024-06-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0005_tirage_tirage_défini'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('adress', models.CharField(max_length=250)),
                ('winner_id', models.ManyToManyField(to='registration.winners')),
            ],
        ),
        migrations.CreateModel(
            name='Vole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('aeroprt', models.CharField(max_length=250)),
                ('date_depart', models.DateField()),
                ('heur_depart', models.TimeField()),
                ('date_arrivee', models.DateField()),
                ('heur_arrivee', models.TimeField()),
                ('nb_places', models.IntegerField()),
                ('winner_id', models.ManyToManyField(to='registration.winners')),
            ],
        ),
    ]
