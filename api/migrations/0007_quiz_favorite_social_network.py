# Generated by Django 4.1.2 on 2022-10-12 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='favorite_social_network',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
    ]
