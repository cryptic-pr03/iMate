# Generated by Django 3.2.9 on 2021-11-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_userprofile_randomalias'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomfrnd',
            name='chatHash',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
