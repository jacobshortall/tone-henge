# Generated by Django 4.0.3 on 2022-04-23 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_userquery_query'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userquery',
            options={'verbose_name_plural': 'User queries'},
        ),
    ]