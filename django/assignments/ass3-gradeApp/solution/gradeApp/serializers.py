from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Teacher, Lesson, Grade, Student


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"

        
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ("id","lesson_name","teacher")

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("id","student_number","first_name","last_name")

class GradeSerializer(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField()
    lesson_id = serializers.IntegerField()
    student = serializers.StringRelatedField()
    student_id = serializers.IntegerField()

    class Meta:
        model = Grade
        fields = ("id","grade","lesson","student","student_id","lesson_id")
        # serializer da uniquelik sağlamak için aşağıdaki metodu kullanıyoruz.Bu metotla admin panelde kısıtlama yapmış olmuyoruz. Burada yaptığımız işlem UniqueTogetherValidatorü import edip içine birleştiğinde unique olmasını istediğimiz fieldları veriyoruz ve kontrol etmesini istediğimiz queryseti veriyoruz o bizim yerimize kontrolü sağlıyor.Örneğimizde lesson ve student eşleşmeleri böylelikle istediğimiz gibi tek olmuş oluyor. Aynı isimde ders birden fazla öğrenci ile eşleşebilir ama aynı öğrenci ile eşleşemez aynı şekilde öğrenci için de öyle.
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Grade.objects.all(),
        #         fields=['lesson_id', 'student_id']#create işleminde kullanılan fieldları yazıyoruz
        #     )
        # ]
