# Generated by Django 5.1.3 on 2024-11-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, null=True)),
                ('jeton_N', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
