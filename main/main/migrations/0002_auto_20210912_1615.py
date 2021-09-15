# Generated by Django 3.2.7 on 2021-09-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhapkhomodel',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pomodel',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='xuatkhomodel',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='xuatnhaptonmodel',
            name='bor',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='xuatnhaptonmodel',
            name='so_luong_nhap',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='xuatnhaptonmodel',
            name='so_luong_xuat',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='xuatnhaptonmodel',
            name='ton_cuoi',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='xuatnhaptonmodel',
            name='total_po',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
