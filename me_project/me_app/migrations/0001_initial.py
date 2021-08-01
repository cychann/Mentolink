# Generated by Django 3.2.3 on 2021-05-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('writer', models.CharField(max_length=100)),
                ('body', models.TextField(default='', null=True)),
                ('pud_date', models.DateTimeField()),
            ],
        ),
    ]
