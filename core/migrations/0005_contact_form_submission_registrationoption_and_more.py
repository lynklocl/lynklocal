# Generated by Django 4.2.5 on 2023-09-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_delete_our_services_remove_lynklocal_about_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact_form_submission",
            name="registrationOption",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="contact_form_submission",
            name="userType",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]