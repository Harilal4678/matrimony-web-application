# Generated by Django 4.2.20 on 2025-05-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
    ]
