# Generated by Django 4.0.5 on 2022-06-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='landing_page',
            field=models.ImageField(default='./static/images/default-website-landing-page.png', upload_to='photos/'),
        ),
    ]
