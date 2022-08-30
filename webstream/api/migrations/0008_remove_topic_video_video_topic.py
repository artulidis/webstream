# Generated by Django 4.1 on 2022-08-17 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_video_watchlist_video_watchlists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.topic'),
        ),
    ]
