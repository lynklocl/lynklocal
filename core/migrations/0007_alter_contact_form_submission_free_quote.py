# Generated by Django 4.2.5 on 2023-09-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "core",
            "0006_rename_registrationoption_contact_form_submission_form_purpose_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact_form_submission",
            name="free_quote",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
