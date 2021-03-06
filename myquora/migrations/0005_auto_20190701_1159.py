# Generated by Django 2.2.2 on 2019-07-01 11:59

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0004_auto_20190701_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 59, 12, 230625), null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 59, 12, 230645), null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 59, 12, 229329), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 59, 12, 229988)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 59, 12, 230010)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 59, 12, 231472), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 59, 12, 231494), null=True),
        ),
    ]
