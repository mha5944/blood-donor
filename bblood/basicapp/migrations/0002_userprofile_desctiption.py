# Generated by Django 3.0.4 on 2020-04-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='desctiption',
            field=models.TextField(blank=True),
        ),
    ]