# Generated by Django 4.2.5 on 2023-09-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_contact_form_submission_free_quote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact_form_submission",
            name="email",
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="contact_form_submission",
            name="form_purpose",
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="contact_form_submission",
            name="name",
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="contact_form_submission",
            name="phone_number",
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="contact_form_submission",
            name="user_type",
            field=models.CharField(max_length=10000),
        ),
    ]
