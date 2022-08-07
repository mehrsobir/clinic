# Generated by Django 4.1 on 2022-08-07 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_doctorsworks_images_partners_doctors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='Partners',
            new_name='Partner',
        ),
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
        migrations.RenameModel(
            old_name='DoctorsWorks',
            new_name='ServiceGroup',
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.servicegroup')),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dw',
            field=models.ManyToManyField(to='main.service'),
        ),
    ]
