# Generated by Django 4.0.1 on 2022-01-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiders', '0009_spider_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider',
            name='sex',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Not sure')], default='N', max_length=1, null=True),
        ),
    ]