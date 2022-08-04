from itertools import count
from django.db import models
from numpy import integer

# Create your models here.
class Routine(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey("accounts.Member", related_name="routine_member", on_delete=models.CASCADE, db_column="member_id")
    creatorName = models.CharField(max_length=20)
    routineName = models.CharField(max_length=20)
    isOpen = models.BooleanField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.routineName


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    en_name = models.CharField(max_length=40)
    ko_name = models.CharField(max_length=40,unique=True)
    part = models.CharField(max_length=40)

    def __str__(self):
        return self.ko_name

class RoutineExercise(models.Model):
    id = models.AutoField(primary_key=True)
    routine_id = models.ForeignKey("Routine", related_name="re_routine", on_delete=models.CASCADE, db_column="routine_id")
    exercise_name= models.ForeignKey("Exercise",to_field='ko_name' ,related_name="exercise", on_delete=models.CASCADE, db_column="exercise_id",null=True)


class Set(models.Model):
    id = models.AutoField(primary_key=True)
    routine_exercise_id= models.ForeignKey("RoutineExercise", related_name="set_exercise", on_delete=models.CASCADE, db_column="routine_exercise_id",null=True)
    count = models.IntegerField()
    weight = models.IntegerField()