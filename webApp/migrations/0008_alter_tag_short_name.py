# Generated by Django 4.2.1 on 2023-07-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0007_remove_tag_id_alter_tag_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='short_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
