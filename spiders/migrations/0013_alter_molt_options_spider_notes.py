# Generated by Django 4.0.1 on 2022-02-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiders', '0012_alter_molt_options_spider_current_molt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='molt',
            options={'ordering': ['spider', '-date', '-number']},
        ),
        migrations.AddField(
            model_name='spider',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
