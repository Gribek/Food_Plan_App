# Generated by Django 2.1.3 on 2018-11-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0004_recipe_preparation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
