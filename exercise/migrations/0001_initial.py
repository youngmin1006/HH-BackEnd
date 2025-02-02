# Generated by Django 3.2.14 on 2022-08-07 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('en_name', models.CharField(max_length=50)),
                ('ko_name', models.CharField(max_length=40, unique=True)),
                ('part', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creatorName', models.CharField(max_length=20)),
                ('routineName', models.CharField(max_length=20)),
                ('isOpen', models.BooleanField()),
                ('count', models.IntegerField(default=0)),
                ('member_id', models.ForeignKey(db_column='member_id', on_delete=django.db.models.deletion.CASCADE, related_name='routine_member', to='accounts.member')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineExercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise_id', models.ForeignKey(db_column='exercise_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_exercise', to='exercise.exercise')),
                ('routine_id', models.ForeignKey(db_column='routine_id', on_delete=django.db.models.deletion.CASCADE, related_name='re_routine', to='exercise.routine')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('routine_exercise_id', models.ForeignKey(db_column='routine_exercise_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='set_exercise', to='exercise.routineexercise')),
            ],
        ),
    ]
