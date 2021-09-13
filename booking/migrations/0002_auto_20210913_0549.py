# Generated by Django 3.2.4 on 2021-09-13 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.bookingstatus', verbose_name='Booking Status'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='forename',
            field=models.CharField(blank=True, max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='surname',
            field=models.CharField(blank=True, max_length=20, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_period',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Time Period'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_unit',
            field=models.CharField(blank=True, default='day', max_length=64, verbose_name='Time Unit'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='zip_code',
            field=models.CharField(blank=True, max_length=256, verbose_name='ZIP Code'),
        ),
    ]