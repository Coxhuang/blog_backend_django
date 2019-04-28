# Generated by Django 2.2 on 2019-04-28 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_blogtag_user', to=settings.AUTH_USER_MODEL, verbose_name='博主'),
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_blogarticle_user', to=settings.AUTH_USER_MODEL, verbose_name='博主'),
        ),
    ]