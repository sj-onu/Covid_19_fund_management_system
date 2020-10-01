# Generated by Django 3.1.1 on 2020-09-21 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0002_auto_20200921_1019'),
        ('Donation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationclass',
            name='donation_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='donationclass',
            name='donor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Donor.donorclass'),
        ),
        migrations.AlterField(
            model_name='donationclass',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
