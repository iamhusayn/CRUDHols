# Generated by Django 5.1.5 on 2025-01-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=100)),
                ('Field', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
    ]
