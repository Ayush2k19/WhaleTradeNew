# Generated by Django 2.2.8 on 2020-10-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RssFeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group_url',
            field=models.URLField(default='None'),
            preserve_default=False,
        ),
    ]