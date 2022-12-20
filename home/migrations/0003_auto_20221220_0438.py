# Generated by Django 3.2.16 on 2022-12-20 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_friend_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='desired_gift',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='password',
            field=models.CharField(default='lzsphk', max_length=20),
        ),
        migrations.AlterField(
            model_name='friend',
            name='secret_friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.friend'),
        ),
    ]
