# Generated by Django 2.2.1 on 2019-05-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20190505_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='Problem_Name',
            field=models.CharField(max_length=90),
        ),
    ]
