# Generated by Django 3.1.6 on 2021-02-03 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestMode1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_field', models.CharField(blank=True, db_column='class', max_length=255, null=True)),
            ],
            options={
                'db_table': 'dept',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Kemu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('km', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'kemu',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('sex', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('classid', models.ForeignKey(blank=True, db_column='classid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='TestMode1.dept')),
            ],
            options={
                'db_table': 'student',
                'managed': True,
            },
        ),
        migrations.RenameModel(
            old_name='Test',
            new_name='Testmode1Test',
        ),
        migrations.AlterModelOptions(
            name='testmode1test',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='testmode1test',
            table='testmode1_test',
        ),
        migrations.CreateModel(
            name='StudentKemu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kemuid', models.ForeignKey(db_column='kemuid', on_delete=django.db.models.deletion.DO_NOTHING, to='TestMode1.kemu')),
                ('studentid', models.ForeignKey(db_column='studentid', on_delete=django.db.models.deletion.DO_NOTHING, to='TestMode1.student')),
            ],
            options={
                'db_table': 'student_kemu',
                'managed': True,
                'unique_together': {('studentid', 'kemuid')},
            },
        ),
    ]
