# Generated by Django 2.1.3 on 2018-11-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('body', models.CharField(max_length=200)),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('editdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('birthdate', models.DateField()),
                ('nickname', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('avatar', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microblog.BlogUser'),
        ),
    ]