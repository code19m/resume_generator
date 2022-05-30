# Generated by Django 4.0.3 on 2022-04-21 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('number', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=50)),
                ('paragraph_1', models.TextField()),
                ('paragraph_2', models.TextField()),
                ('cause', models.TextField()),
                ('confirmer_role', models.CharField(max_length=30)),
                ('confirmer_name', models.CharField(max_length=50)),
                ('address_uz', models.CharField(max_length=255)),
                ('address_en', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commands.commandtype')),
            ],
        ),
    ]