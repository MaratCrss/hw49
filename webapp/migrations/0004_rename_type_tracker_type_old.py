# Generated by Django 4.1.3 on 2022-11-22 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_tracker_status_alter_tracker_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='type',
            new_name='type_old',
        ),
    ]
