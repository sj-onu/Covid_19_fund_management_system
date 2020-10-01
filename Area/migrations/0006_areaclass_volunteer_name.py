# Generated by Django 3.1.1 on 2020-09-23 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0004_auto_20200923_0021'),
        ('Area', '0005_remove_areaclass_volunteer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='areaclass',
            name='volunteer_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Volunteer.volunteerclass'),
        ),
    ]
