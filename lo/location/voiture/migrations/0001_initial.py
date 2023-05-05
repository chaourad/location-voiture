# Generated by Django 4.2 on 2023-05-05 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date_permis', models.DateField()),
                ('ref_permis', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True, unique=True)),
                ('prix_jour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('nombre_siege', models.CharField(max_length=100, null=True)),
                ('nbr_bagage', models.CharField(max_length=100, null=True)),
                ('nbr_portes', models.CharField(max_length=100, null=True)),
                ('climatise', models.CharField(max_length=100, null=True)),
                ('manuelle', models.CharField(max_length=100, null=True)),
                ('photourl', models.CharField(max_length=700, null=True)),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villes', to='voiture.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voiture.client')),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voitures', to='voiture.voiture')),
            ],
        ),
    ]
