# Generated by Django 4.1.3 on 2022-11-18 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='TrackerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Tip')),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=140, verbose_name='Kratkoe opisanie')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Polnoe opisanie')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Vremya sozdaniya')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Vremya izmeneniya')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.trackerstatus', verbose_name='Status')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.trackertype', verbose_name='Tip')),
            ],
        ),
    ]
