# Generated by Django 3.1.3 on 2020-12-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20201201_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReCommentTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=200)),
                ('profileImage', models.CharField(default='/media/red.jpg', max_length=500)),
                ('user_pk', models.IntegerField(default=True)),
                ('commentTodo_pk', models.IntegerField(default=True)),
            ],
        ),
    ]