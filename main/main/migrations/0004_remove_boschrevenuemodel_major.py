# Generated by Django 3.2.7 on 2021-10-17 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_costmodel_cost_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boschrevenuemodel',
            name='major',
        ),
    ]
