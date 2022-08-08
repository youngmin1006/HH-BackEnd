# Generated by Django 3.2.14 on 2022-08-08 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('exercise', '0002_alter_routine_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='member_id',
            field=models.ForeignKey(blank=True, db_column='member_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='routine_member', to='accounts.member'),
        ),
    ]