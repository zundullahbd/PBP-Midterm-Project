# Generated by Django 3.2.8 on 2021-10-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=30)),
                ('eventTime', models.DateTimeField()),
                ('eventDescription', models.TextField()),
            ],
        ),
    ]
