# Generated by Django 4.1.7 on 2023-02-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=12)),
                ('IsActive', models.BooleanField(default=False)),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
                ('DateModified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'master',
            },
        ),
    ]