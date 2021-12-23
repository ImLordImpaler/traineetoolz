# Generated by Django 3.2.9 on 2021-12-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_reactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='reactions',
            field=models.ManyToManyField(blank=True, related_name='article_reaction', to='article.Reaction'),
        ),
    ]