# Generated by Django 3.2.9 on 2022-05-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
