# Generated by Django 2.2.11 on 2020-03-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200322_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]