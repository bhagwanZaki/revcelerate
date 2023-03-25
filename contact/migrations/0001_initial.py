# Generated by Django 4.0.4 on 2023-03-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(blank=True, max_length=20)),
                ('address', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('instagram_handle', models.CharField(blank=True, max_length=255)),
                ('companies', models.ManyToManyField(related_name='contacts', to='contact.company')),
            ],
        ),
    ]