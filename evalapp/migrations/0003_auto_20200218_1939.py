# Generated by Django 3.0.3 on 2020-02-18 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evalapp', '0002_auto_20200218_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='list',
            name='score',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
