# Generated by Django 2.0 on 2017-12-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='calories',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='items',
            name='fat_saturated',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='items',
            name='fiber',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=30, unique='true'),
        ),
        migrations.AlterField(
            model_name='items',
            name='sodium',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='items',
            name='sugar',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='items',
            name='tot_carbs',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='items',
            name='tot_fat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='items',
            name='tot_protein',
            field=models.FloatField(default=0.0),
        ),
    ]