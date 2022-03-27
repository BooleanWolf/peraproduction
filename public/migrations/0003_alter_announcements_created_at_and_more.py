# Generated by Django 4.0.3 on 2022-03-14 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_announcements_created_at_assignments_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='class_tests',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
