# Generated by Django 3.2.6 on 2021-08-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0008_auto_20210827_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placefour',
            name='first_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placefour',
            name='second_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placefour',
            name='slot_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placefour',
            name='slot_three',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placefour',
            name='slot_two',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placeone',
            name='first_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placeone',
            name='second_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placeone',
            name='slot_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placeone',
            name='slot_three',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placeone',
            name='slot_two',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placethree',
            name='first_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placethree',
            name='second_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placethree',
            name='slot_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placethree',
            name='slot_three',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placethree',
            name='slot_two',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placetwo',
            name='first_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placetwo',
            name='second_dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placetwo',
            name='slot_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placetwo',
            name='slot_three',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='placetwo',
            name='slot_two',
            field=models.IntegerField(default=0),
        ),
    ]