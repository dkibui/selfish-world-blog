# Generated by Django 4.2.3 on 2023-07-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='hello', upload_to='uploads/applications/'),
            preserve_default=False,
        ),
    ]
