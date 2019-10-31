# Generated by Django 2.2.6 on 2019-10-09 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/')),
                ('title', models.CharField(default='', max_length=512)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
