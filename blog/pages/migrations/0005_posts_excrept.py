# Generated by Django 3.0.2 on 2020-01-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200129_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='excrept',
            field=models.CharField(default='Add Excrept', max_length=125),
            preserve_default=False,
        ),
    ]
