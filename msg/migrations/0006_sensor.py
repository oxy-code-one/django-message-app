# Generated by Django 4.1.4 on 2023-01-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0005_remove_sense_id_alter_sense_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity1', models.CharField(default='', max_length=6)),
                ('activity2', models.CharField(default='', max_length=6)),
                ('activity3', models.CharField(default='', max_length=6)),
                ('activity4', models.CharField(default='', max_length=6)),
                ('activity5', models.CharField(default='', max_length=6)),
                ('activity6', models.CharField(default='', max_length=6)),
                ('activity7', models.CharField(default='', max_length=6)),
                ('activity8', models.CharField(default='', max_length=6)),
                ('activity9', models.CharField(default='', max_length=6)),
                ('activity10', models.CharField(default='', max_length=6)),
                ('activity11', models.CharField(default='', max_length=6)),
                ('activity12', models.CharField(default='', max_length=6)),
                ('activity13', models.CharField(default='', max_length=6)),
                ('activity14', models.CharField(default='', max_length=6)),
                ('activity15', models.CharField(default='', max_length=6)),
                ('activity16', models.CharField(default='', max_length=6)),
                ('activity17', models.CharField(default='', max_length=6)),
                ('activity18', models.CharField(default='', max_length=6)),
                ('activity19', models.CharField(default='', max_length=6)),
                ('activity20', models.CharField(default='', max_length=6)),
                ('activity21', models.CharField(default='', max_length=6)),
                ('activity22', models.CharField(default='', max_length=6)),
                ('activity23', models.CharField(default='', max_length=6)),
                ('activity24', models.CharField(default='', max_length=6)),
                ('activity25', models.CharField(default='', max_length=6)),
                ('activity26', models.CharField(default='', max_length=6)),
                ('activity27', models.CharField(default='', max_length=6)),
                ('activity28', models.CharField(default='', max_length=6)),
                ('activity29', models.CharField(default='', max_length=6)),
                ('activity30', models.CharField(default='', max_length=6)),
                ('activity31', models.CharField(default='', max_length=6)),
                ('activity32', models.CharField(default='', max_length=6)),
                ('activity33', models.CharField(default='', max_length=6)),
                ('activity34', models.CharField(default='', max_length=6)),
                ('activity35', models.CharField(default='', max_length=6)),
                ('activity36', models.CharField(default='', max_length=6)),
                ('activity37', models.CharField(default='', max_length=6)),
                ('activity38', models.CharField(default='', max_length=6)),
                ('activity39', models.CharField(default='', max_length=6)),
                ('activity40', models.CharField(default='', max_length=6)),
                ('activity41', models.CharField(default='', max_length=6)),
                ('activity42', models.CharField(default='', max_length=6)),
                ('activity43', models.CharField(default='', max_length=6)),
                ('activity44', models.CharField(default='', max_length=6)),
                ('activity45', models.CharField(default='', max_length=6)),
                ('activity46', models.CharField(default='', max_length=6)),
                ('activity47', models.CharField(default='', max_length=6)),
                ('activity48', models.CharField(default='', max_length=6)),
                ('activity49', models.CharField(default='', max_length=6)),
                ('activity50', models.CharField(default='', max_length=6)),
                ('activity51', models.CharField(default='', max_length=6)),
                ('activity52', models.CharField(default='', max_length=6)),
                ('activity53', models.CharField(default='', max_length=6)),
                ('activity54', models.CharField(default='', max_length=6)),
                ('activity55', models.CharField(default='', max_length=6)),
                ('activity56', models.CharField(default='', max_length=6)),
                ('activity57', models.CharField(default='', max_length=6)),
                ('activity58', models.CharField(default='', max_length=6)),
                ('activity59', models.CharField(default='', max_length=6)),
                ('activity60', models.CharField(default='', max_length=6)),
                ('userID', models.IntegerField(db_index=True)),
                ('time', models.CharField(db_index=True, max_length=13)),
            ],
            options={
                'index_together': {('userID', 'time')},
            },
        ),
    ]