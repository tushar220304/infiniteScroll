# Generated by Django 3.2.13 on 2022-09-16 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email_subscription',
            old_name='Name',
            new_name='Email',
        ),
    ]