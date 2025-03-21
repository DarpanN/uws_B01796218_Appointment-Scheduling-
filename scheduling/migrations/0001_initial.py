# Generated by Django 5.1.7 on 2025-03-15 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=255)),
                ('client_address', models.TextField()),
                ('client_email', models.EmailField(max_length=254, unique=True)),
                ('client_mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_payroll_number', models.CharField(max_length=10, unique=True)),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=255)),
                ('service_description', models.TextField()),
                ('service_hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expenses', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.service')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_number', models.CharField(max_length=20, unique=True)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.appointment')),
            ],
        ),
    ]
