# Generated by Django 4.1.3 on 2022-11-30 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='testhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='test',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courses'),
        ),
        migrations.AddField(
            model_name='test',
            name='history',
            field=models.ManyToManyField(through='course.TestHistory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subscribed',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courses'),
        ),
        migrations.AddField(
            model_name='subscribed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mcq',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test'),
        ),
        migrations.AddField(
            model_name='courses',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courses',
            name='subscription',
            field=models.ManyToManyField(through='course.Subscribed', to=settings.AUTH_USER_MODEL),
        ),
    ]
