# Generated by Django 4.0.3 on 2022-03-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_announcements_description_alter_assignments_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_tests',
            name='type',
            field=models.CharField(choices=[('mcq', 'Mcq'), ('written', 'Written')], default='mcq', max_length=10),
        ),
    ]
