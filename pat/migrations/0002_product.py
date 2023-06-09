# Generated by Django 4.1.7 on 2023-04-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('category', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]
