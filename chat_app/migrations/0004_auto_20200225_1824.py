# Generated by Django 2.2.10 on 2020-02-25 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_app', '0003_auto_20200225_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='text',
        ),
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='messages',
            field=models.ManyToManyField(related_name='chat_rooms', to='chat_app.Message'),
        ),
    ]
