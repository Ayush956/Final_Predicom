# Generated by Django 4.1.5 on 2023-05-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop_name', models.CharField(max_length=50)),
                ('laptop_link', models.URLField()),
            ],
        ),
    ]
