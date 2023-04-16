# Generated by Django 4.1.7 on 2023-04-06 14:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pat', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('category', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
