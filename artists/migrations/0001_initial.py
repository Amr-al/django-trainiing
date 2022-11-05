# Generated by Django 4.1.2 on 2022-11-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stage_name', models.CharField(max_length=30, unique=True)),
                ('Social_link', models.URLField(blank=True)),
            ],
            options={
                'ordering': ('Stage_name',),
            },
        ),
    ]