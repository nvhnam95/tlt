# Generated by Django 3.2.7 on 2021-10-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_boschrevenuemodel_costmodel_siderevenuemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costmodel',
            name='cost_type',
            field=models.TextField(default=''),
        ),
    ]
