# Generated by Django 3.1.5 on 2021-01-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telefoni', '0002_auto_20210107_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]