# Generated by Django 3.1.4 on 2021-01-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210108_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=35)),
                ('email', models.CharField(default='', max_length=35)),
                ('phone', models.CharField(default='', max_length=35)),
                ('desc', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
