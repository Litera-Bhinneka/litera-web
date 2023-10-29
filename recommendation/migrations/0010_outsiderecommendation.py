# Generated by Django 4.2.6 on 2023-10-29 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0009_remove_recommendation_user_recommendation_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutsideRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_book_title', models.CharField(max_length=255)),
                ('another_out_book_title', models.CharField(max_length=255)),
                ('out_description', models.TextField()),
                ('out_recommendation_date', models.DateTimeField(auto_now_add=True)),
                ('out_recommender_name', models.CharField(max_length=150)),
            ],
        ),
    ]
