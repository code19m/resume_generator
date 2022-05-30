# Generated by Django 4.0.3 on 2022-04-21 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='CommandTypeText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commands.commandtype')),
            ],
        ),
    ]