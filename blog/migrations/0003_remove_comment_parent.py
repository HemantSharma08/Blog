# Generated by Django 2.2.6 on 2019-10-13 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
