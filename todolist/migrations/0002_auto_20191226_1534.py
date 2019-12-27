# Generated by Django 3.0.1 on 2019-12-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[(2, 'high'), (1, 'middle'), (0, 'low')], max_length=10),
        ),
    ]
