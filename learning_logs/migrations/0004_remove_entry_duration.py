# Generated by Django 2.1.7 on 2019-03-31 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_entry_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='duration',
        ),
    ]
