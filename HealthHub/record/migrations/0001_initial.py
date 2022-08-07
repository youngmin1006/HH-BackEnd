# Generated by Django 4.0.4 on 2022-08-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercise', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='기록 작성 시간')),
                ('member_id', models.ForeignKey(db_column='member_id', on_delete=django.db.models.deletion.CASCADE, related_name='record_member', to='accounts.member')),
                ('routine_id', models.ForeignKey(db_column='routine_id', on_delete=django.db.models.deletion.CASCADE, related_name='record_routine', to='exercise.routine')),
            ],
        ),
    ]
