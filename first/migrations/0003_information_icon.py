# Generated by Django 3.2.12 on 2022-07-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_information_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='icon',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
