# Generated by Django 3.1.3 on 2020-12-27 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20201226_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': [('can_set_is_senior', "Право устанавливать поле 'старший'")], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
    ]
