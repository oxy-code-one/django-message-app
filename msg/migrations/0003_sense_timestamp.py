# Generated by Django 4.1.4 on 2022-12-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0002_sense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sense',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
