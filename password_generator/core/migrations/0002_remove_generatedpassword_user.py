# Generated by Django 5.0.3 on 2024-03-21 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedpassword',
            name='user',
        ),
    ]
