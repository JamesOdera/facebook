# Generated by Django 3.1.7 on 2021-04-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='restrict_comment',
            field=models.BooleanField(default=False),
        ),
    ]