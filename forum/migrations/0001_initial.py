# Generated by Django 3.2.8 on 2021-10-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPertanyaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('pekerjaan', models.CharField(max_length=100)),
                ('konten', models.TextField()),
                ('tag', models.TextField()),
            ],
        ),
    ]
