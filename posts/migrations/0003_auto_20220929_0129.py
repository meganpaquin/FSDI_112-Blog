# Generated by Django 4.1.1 on 2022-09-29 01:29

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "published" : "A post that appears on the sit (to all users)",
        "draft" : "A post being worked on and not ready to be viewed",
        "archived" : "A post that was published but is no longer appears to users"
    }
    Status = apps.get_model("posts", "Status")

    for name, desc in entries.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_status'),
    ]

    operations = [migrations.RunPython(populate_status)]