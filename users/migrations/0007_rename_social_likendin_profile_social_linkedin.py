# Generated by Django 4.0.1 on 2022-01-11 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_desription_skill_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_likendin',
            new_name='social_linkedin',
        ),
    ]