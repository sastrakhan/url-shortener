# Generated by Django 3.0.6 on 2020-05-07 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_name', models.CharField(max_length=100)),
                ('shortened_version', models.CharField(max_length=50)),
                ('custom_version', models.CharField(max_length=50)),
            ],
        ),
    ]
