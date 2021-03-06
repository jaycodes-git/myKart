# Generated by Django 3.1.4 on 2021-02-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=150),
        ),
    ]
