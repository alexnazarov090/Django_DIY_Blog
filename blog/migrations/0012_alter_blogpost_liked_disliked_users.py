# Generated by Django 3.2.9 on 2022-01-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20220116_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='liked_disliked_users',
            field=models.JSONField(default={'disliked_users': None, 'liked_users': None}),
        ),
    ]