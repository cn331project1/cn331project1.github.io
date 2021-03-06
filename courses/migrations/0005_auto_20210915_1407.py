# Generated by Django 3.2.6 on 2021-09-15 07:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20210915_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
                ('semester', models.IntegerField()),
                ('year', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('status', models.BooleanField()),
                ('count', models.IntegerField(default=0)),
                ('student', models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
