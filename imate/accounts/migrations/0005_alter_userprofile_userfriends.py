# Generated by Django 3.2.8 on 2021-10-28 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_alter_userprofile_userhash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userFriends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
