# Generated by Django 4.1.1 on 2022-09-29 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220929_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.status'),
        ),
    ]