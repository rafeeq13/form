# Generated by Django 4.2 on 2023-05-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0010_apply_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='resume',
            field=models.FileField(default=True, upload_to='uploads/'),
        ),
    ]
