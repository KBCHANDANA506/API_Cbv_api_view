# Generated by Django 4.2.2 on 2023-06-09 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('PcId', models.IntegerField(primary_key=True, serialize=False)),
                ('PcName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pid', models.IntegerField()),
                ('Pname', models.CharField(max_length=100)),
                ('Pprice', models.IntegerField()),
                ('PDate', models.DateField()),
                ('PcName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_category')),
            ],
        ),
    ]
