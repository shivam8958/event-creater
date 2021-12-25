# Generated by Django 3.1 on 2021-12-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=150)),
                ('dat', models.DateTimeField()),
                ('location', models.CharField(max_length=150)),
                ('des', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='album')),
            ],
        ),
    ]
