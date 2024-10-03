# Generated by Django 5.1.1 on 2024-10-03 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housewise', '0002_userhousewise_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('housetype_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(choices=[('concrete', 'Concrete'), ('wooden', 'Wooden')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('width', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('house_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='housewise.housetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
