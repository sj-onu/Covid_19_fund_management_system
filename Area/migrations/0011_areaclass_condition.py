# Generated by Django 3.1.1 on 2020-10-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0010_areaclass_area_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='areaclass',
            name='condition',
            field=models.CharField(default='poor', max_length=300),
        ),
    ]
