# Generated by Django 3.0.4 on 2020-04-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0003_auto_20200412_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='case',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
