# Generated by Django 4.0.1 on 2022-01-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='demo_limk',
            new_name='demo_link',
        ),
    ]
