# Generated by Django 4.2.7 on 2023-11-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='email address'),
        ),
    ]