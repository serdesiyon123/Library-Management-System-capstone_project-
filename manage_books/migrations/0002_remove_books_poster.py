# Generated by Django 5.0.3 on 2024-03-09 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='poster',
        ),
    ]