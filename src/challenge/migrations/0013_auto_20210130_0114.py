# Generated by Django 3.1.5 on 2021-01-30 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0012_auto_20201226_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='unlock_requirements',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
