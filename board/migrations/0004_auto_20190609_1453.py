# Generated by Django 2.1.7 on 2019-06-09 05:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20190326_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
