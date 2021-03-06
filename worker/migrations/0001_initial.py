# Generated by Django 3.2.7 on 2021-10-03 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('is_Admin', models.BooleanField(default=False)),
                ('admin_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='owner.owner')),
            ],
        ),
    ]
