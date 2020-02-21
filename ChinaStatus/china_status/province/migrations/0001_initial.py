# Generated by Django 2.0.6 on 2018-06-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50, verbose_name='省份')),
                ('total', models.IntegerField(verbose_name='总体收入')),
                ('total_increase_rate', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='总体增速')),
                ('city', models.IntegerField(blank=True, null=True, verbose_name='城镇收入')),
                ('city_increase_rate', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='城镇增速')),
                ('rural', models.IntegerField(blank=True, null=True, verbose_name='农村收入')),
                ('rural_increase_rate', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='农村增速')),
                ('total_increase', models.IntegerField(blank=True, null=True, verbose_name='全体增量')),
                ('city_increase', models.IntegerField(blank=True, null=True, verbose_name='城镇增量')),
                ('rural_increase', models.IntegerField(blank=True, null=True, verbose_name='农村增量')),
                ('year', models.IntegerField(blank=True, default=2017, null=True, verbose_name='年份')),
            ],
            options={
                'verbose_name': '省级数据',
                'verbose_name_plural': '中国大陆省级全体居民收入排名',
                'ordering': ['-total'],
            },
        ),
    ]
