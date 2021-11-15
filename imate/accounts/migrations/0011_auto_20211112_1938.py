# Generated by Django 3.2.9 on 2021-11-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211111_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomchat',
            name='RandomChatId',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='randomchat',
            name='isPaired',
            field=models.BooleanField(default=False),
        ),
    ]
