# Generated by Django 3.2.9 on 2022-02-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_review_order_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
