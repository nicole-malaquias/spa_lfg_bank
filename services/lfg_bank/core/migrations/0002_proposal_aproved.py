# Generated by Django 4.2.5 on 2023-10-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='aproved',
            field=models.BooleanField(default=False),
        ),
    ]
