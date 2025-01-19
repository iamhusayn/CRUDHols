# Generated by Django 5.1.5 on 2025-01-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('books', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
