# Generated by Django 4.0.4 on 2022-05-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_human_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Baby',
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.DeleteModel(
            name='Human',
        ),
    ]
