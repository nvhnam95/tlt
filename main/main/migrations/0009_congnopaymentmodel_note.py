# Generated by Django 3.2.7 on 2021-10-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211022_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='congnopaymentmodel',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
    ]
