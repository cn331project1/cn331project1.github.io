# Generated by Django 3.2.6 on 2021-09-15 06:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20210915_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='flights', to=settings.AUTH_USER_MODEL),
        ),
    ]