# Generated by Django 4.1.4 on 2023-01-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timeinfo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]