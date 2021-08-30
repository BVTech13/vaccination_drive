# Generated by Django 3.2.6 on 2021-08-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0006_alter_user_register_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='placefour',
            name='first_dose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='placefour',
            name='second_dose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='placeone',
            name='first_dose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='placeone',
            name='second_dose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='placethree',
            name='first_dose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='placethree',
            name='second_dose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='placetwo',
            name='first_dose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='placetwo',
            name='second_dose',
            field=models.IntegerField(null=True),
        ),
    ]
