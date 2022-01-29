# Generated by Django 4.0.1 on 2022-01-29 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('spiders', '0007_remove_spider_list_spider_owner_delete_animalslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]