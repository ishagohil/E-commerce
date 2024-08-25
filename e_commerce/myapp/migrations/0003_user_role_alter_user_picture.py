# Generated by Django 5.0.1 on 2024-02-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_user_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="picture",
            field=models.ImageField(
                default="Default1.jpg", upload_to="profilepicture/"
            ),
        ),
    ]
