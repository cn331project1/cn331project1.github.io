# Generated by Django 3.2.6 on 2021-09-14 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='subject',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
    ]
