# Generated by Django 2.1 on 2018-08-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_auto_20180820_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
