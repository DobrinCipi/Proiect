# Generated by Django 4.1.4 on 2023-02-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0007_adresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='adresa',
            name='oras',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]