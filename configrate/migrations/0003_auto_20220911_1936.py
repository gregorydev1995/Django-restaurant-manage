# Generated by Django 3.2.6 on 2022-09-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configrate', '0002_auto_20220817_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='name_fk',
            field=models.CharField(default='', max_length=50, verbose_name='اسم الصنف الاجنبي'),
        ),
        migrations.AddField(
            model_name='items',
            name='name_lo',
            field=models.CharField(default='', max_length=50, verbose_name='اسم الصنف المحلي'),
        ),
    ]
