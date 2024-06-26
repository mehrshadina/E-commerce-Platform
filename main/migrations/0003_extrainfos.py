# Generated by Django 4.2.11 on 2024-06-25 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extrainfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
