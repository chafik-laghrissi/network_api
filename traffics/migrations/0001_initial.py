# Generated by Django 4.0.2 on 2022-02-02 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('name', models.CharField(default='', max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('hour_interval', models.CharField(max_length=6)),
                ('collective_transport', models.IntegerField(default=0)),
                ('particular_transport', models.IntegerField(default=0)),
                ('haulage', models.IntegerField(default=0)),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffics.point')),
            ],
        ),
    ]
