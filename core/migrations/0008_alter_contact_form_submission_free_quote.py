# Generated by Django 4.2.5 on 2023-09-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_contact_form_submission_free_quote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact_form_submission",
            name="free_quote",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
