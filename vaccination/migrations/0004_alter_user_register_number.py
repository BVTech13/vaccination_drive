# Generated by Django 3.2.6 on 2021-08-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0003_auto_20210827_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_number',
            field=models.BigIntegerField(),
        ),
    ]