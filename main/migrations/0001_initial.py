# Generated by Django 3.1.3 on 2020-11-07 17:51

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=40, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=40, verbose_name='Отчество')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=40, verbose_name='Отчество')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='FacilityObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название производственного объекта')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Уникальная строка идентификатор (slug)')),
            ],
            options={
                'verbose_name': 'Производственный объект',
                'verbose_name_plural': 'Производственные объекты',
            },
        ),
        migrations.CreateModel(
            name='MovementEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_type', models.CharField(choices=[('ARR', 'Заезд'), ('LVN', 'Отъезд')], default='ARR', max_length=3, verbose_name='Тип списка')),
                ('scheduled_datetime', models.DateTimeField(verbose_name='Дата и время заезда/отъезда')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('creator', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кем создана')),
                ('employee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.employee', verbose_name='Заезжающий/отъезжающий сотрудник')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.facilityobject', verbose_name='Производственный объект')),
            ],
            options={
                'verbose_name': 'Запись о заезде/отъезде',
                'verbose_name_plural': 'Записи о заездах/отъездах',
            },
        ),
        migrations.CreateModel(
            name='MovementEntryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_type', models.CharField(choices=[('ARR', 'Заезд'), ('LVN', 'Отъезд')], default='ARR', max_length=3, verbose_name='Тип списка')),
                ('scheduled_datetime', models.DateTimeField(verbose_name='Дата и время заезда/отъезда')),
                ('modified_datetime', models.DateTimeField(verbose_name='Время внесения изменений')),
                ('employee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.employee', verbose_name='Заезжающий/отъезжающий сотрудник')),
                ('modified_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('modified_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movemententry')),
            ],
            options={
                'verbose_name': 'Состояние записи',
                'verbose_name_plural': 'Состояния записей',
            },
        ),
    ]
