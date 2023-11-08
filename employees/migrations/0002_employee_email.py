# Generated by Django 4.2.7 on 2023-11-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
