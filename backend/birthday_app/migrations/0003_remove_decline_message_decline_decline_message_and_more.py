# Generated by Django 4.1.2 on 2022-10-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_app', '0002_decline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='decline',
            name='message',
        ),
        migrations.AddField(
            model_name='decline',
            name='decline_message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
