# Generated by Django 4.0.5 on 2022-08-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('txt', models.TextField()),
            ],
        ),
    ]
