# Generated by Django 4.1.3 on 2022-12-19 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_follow_alter_user_options_user_unique_username_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
