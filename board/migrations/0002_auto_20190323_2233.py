# Generated by Django 2.1.7 on 2019-03-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curtain',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_order',
            field=models.IntegerField(default=1),
        ),
    ]
