# Generated by Django 4.1.7 on 2023-08-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('caption', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
