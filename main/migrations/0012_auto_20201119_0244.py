# Generated by Django 3.1.3 on 2020-11-18 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201119_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movemententry',
            options={'permissions': [('change_owned_movemententry', 'Право изменения записи созданной пользователем'), ('delete_owned_movemententry', 'Право удаления записи созданной пользователем')], 'verbose_name': 'Запись о заезде/отъезде', 'verbose_name_plural': 'Записи о заездах/отъездах'},
        ),
    ]
