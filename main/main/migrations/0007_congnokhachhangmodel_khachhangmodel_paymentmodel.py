# Generated by Django 3.2.7 on 2021-10-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_customermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHangModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='')),
                ('company', models.TextField(blank=True, default='')),
                ('address', models.TextField(blank=True, default='')),
                ('note', models.TextField(blank=True, default='')),
                ('ma_so_thue', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.FloatField(default=0, null=True)),
                ('khach_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.khachhangmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CongNoKhachHangModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_xuat_hang', models.DateField(blank=True, null=True)),
                ('bosch_no', models.TextField(blank=True, default='')),
                ('zexel_no', models.TextField(blank=True, default='')),
                ('ma_tem', models.TextField(blank=True, default='')),
                ('english_name', models.TextField(blank=True, default='')),
                ('vietnamese_name', models.TextField(blank=True, default='')),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('total', models.FloatField(default=0, null=True)),
                ('vat', models.FloatField(default=0, null=True)),
                ('khach_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.khachhangmodel')),
            ],
        ),
    ]