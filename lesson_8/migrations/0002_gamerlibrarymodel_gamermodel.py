# Generated by Django 3.0.6 on 2020-06-14 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_8', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GamerLibraryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('game', models.ManyToManyField(to='lesson_8.GameModel')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_8.GamerModel')),
            ],
        ),
    ]