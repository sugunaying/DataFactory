# Generated by Django 2.2 on 2021-08-20 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_db_href_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_href',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
