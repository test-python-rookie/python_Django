# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dept(models.Model):
    id = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'dept'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class Kemu(models.Model):
    id = models.IntegerField(primary_key=True)
    km = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kemu'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    classid = models.ForeignKey(Dept, models.DO_NOTHING, db_column='classid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student'


class StudentKemu(models.Model):
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentid')
    kemuid = models.ForeignKey(Kemu, models.DO_NOTHING, db_column='kemuid')

    class Meta:
        managed = True
        db_table = 'student_kemu'
        unique_together = (('studentid', 'kemuid'),)


class Testmode1Test(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'testmode1_test'
