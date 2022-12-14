# Generated by Django 4.1.2 on 2022-10-13 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='タグ名')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('good', models.ManyToManyField(blank=True, related_name='question_good', to=settings.AUTH_USER_MODEL, verbose_name='いいねしたユーザー')),
                ('tag', models.ManyToManyField(blank=True, related_name='question_tag', to='qa.tag', verbose_name='タグ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
    ]
