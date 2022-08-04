# Generated by Django 4.0.6 on 2022-08-04 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_routine_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routineexercise',
            name='exercise_id',
            field=models.ForeignKey(db_column='exercise_id', on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='exercise.exercise'),
        ),
    ]
