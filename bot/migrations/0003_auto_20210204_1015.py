# Generated by Django 3.1.6 on 2021-02-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_setting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.TextField(),
        ),
    ]
