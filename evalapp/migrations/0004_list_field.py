# Generated by Django 3.0.3 on 2020-02-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evalapp', '0003_auto_20200218_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='field',
            field=models.CharField(choices=[('전공', 'w'), ('교양', 'Medium'), ('교직', 'Large')], default='전공', max_length=2),
        ),
    ]
