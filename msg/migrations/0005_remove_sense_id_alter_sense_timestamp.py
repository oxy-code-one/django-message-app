# Generated by Django 4.1.4 on 2022-12-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0004_alter_sense_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sense',
            name='id',
        ),
        migrations.AlterField(
            model_name='sense',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]
