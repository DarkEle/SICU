# Generated by Django 2.0.6 on 2018-07-30 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180729_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autor_Post',
            field=models.TextField(default=''),
        ),
    ]
