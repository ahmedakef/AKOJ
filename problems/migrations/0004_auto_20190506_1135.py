# Generated by Django 2.2.1 on 2019-05-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20190505_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='Output',
            field=models.TextField(null=True),
        ),
    ]
