# Generated by Django 5.1.3 on 2024-11-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, null=True)),
                ('JetonN', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]