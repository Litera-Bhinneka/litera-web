# Generated by Django 4.2.6 on 2023-10-28 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_rename_recomendation_recommendation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='book_image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
