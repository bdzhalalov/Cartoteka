# Generated by Django 4.1.4 on 2022-12-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField()),
                ('number', models.PositiveBigIntegerField()),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('last_usage', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='not activated', max_length=32)),
            ],
        ),
    ]
