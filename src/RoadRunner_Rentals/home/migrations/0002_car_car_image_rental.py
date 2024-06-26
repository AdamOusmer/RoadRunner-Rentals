# Generated by Django 5.0.4 on 2024-04-07 10:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(null=True, upload_to='car_images'),
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_start_date', models.DateTimeField()),
                ('rental_end_date', models.DateTimeField()),
                ('rental_total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rental_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.branch')),
                ('rental_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.car')),
                ('rental_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
