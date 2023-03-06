# Generated by Django 4.1.7 on 2023-03-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_delete_instagramlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagramlinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='instagram')),
                ('link', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Instagram Link',
                'verbose_name_plural': 'Instagram Links',
            },
        ),
    ]
