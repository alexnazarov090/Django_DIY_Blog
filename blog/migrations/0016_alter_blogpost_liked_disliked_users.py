# Generated by Django 3.2.9 on 2022-01-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='liked_disliked_users',
            field=models.JSONField(default={'disliked_users': [], 'liked_users': []}),
        ),
    ]
