# Generated by Django 3.2.6 on 2021-09-28 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socio', models.CharField(max_length=60)),
                ('tasa', models.FloatField()),
                ('mon_max', models.IntegerField()),
            ],
        ),
    ]
