# Generated by Django 5.1.5 on 2025-01-26 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('hall', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('payment_method', models.CharField(max_length=20)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='tickets.guest')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='tickets.movie')),
            ],
        ),
    ]
