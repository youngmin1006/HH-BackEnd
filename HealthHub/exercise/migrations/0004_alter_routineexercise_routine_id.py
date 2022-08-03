# Generated by Django 3.2.14 on 2022-08-03 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_alter_routineexercise_routine_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routineexercise',
            name='routine_id',
            field=models.ForeignKey(db_column='routine_id', on_delete=django.db.models.deletion.CASCADE, related_name='re_routine', to='exercise.routine'),
        ),
    ]
