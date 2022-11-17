# Generated by Django 3.0.5 on 2022-11-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(verbose_name='Post Created')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
