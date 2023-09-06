# Generated by Django 4.2.4 on 2023-09-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='广告标题')),
                ('link', models.CharField(max_length=500, verbose_name='广告链接')),
                ('image_url', models.ImageField(blank=True, max_length=255, null=True, upload_to='banner', verbose_name='广告图片')),
                ('remark', models.TextField(verbose_name='备注信息')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '轮播广告',
                'verbose_name_plural': '轮播广告',
                'db_table': 'ly_banner',
            },
        ),
    ]
