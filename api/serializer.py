from classperiod.models import Class_Period
from classroom.models import Classroom
from course.models import Courses
from student.models import Student
from rest_framework import serializers
from teacher.models import Teacher
from datetime import datetime


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
    
class StudentSerializer(serializers.ModelSerializer):
    courses= CourseSerializer(many=True)
    
    class Meta:
        model = Student
        exclude=["email"]
class MinimalStudentSerializer(serializers.ModelSerializer):
    
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f'{object.first_name} {object.last_name}'
    
    age=serializers.SerializerMethodField()
    def get_age(self,object):
        today = datetime.now
        age = today-object.date_of_birth
        return age 
    class Meta:
        model = Student
        fields = ["id","full_name","email","age"]
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"
class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = '__all__'