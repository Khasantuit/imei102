# Generated by Django 5.1.3 on 2024-11-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qidiruv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qidiruv_N', models.CharField(max_length=200, null=True)),
                ('fio', models.CharField(max_length=200, null=True)),
                ('jshshir', models.CharField(max_length=200, null=True)),
                ('info', models.CharField(max_length=200, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
