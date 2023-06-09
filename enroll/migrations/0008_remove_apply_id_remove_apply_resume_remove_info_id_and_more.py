# Generated by Django 4.2 on 2023-05-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_apply_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='id',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='info',
            name='id',
        ),
        migrations.AlterField(
            model_name='apply',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
