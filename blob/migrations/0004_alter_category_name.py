# Generated by Django 4.0.4 on 2022-07-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blob', '0003_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]