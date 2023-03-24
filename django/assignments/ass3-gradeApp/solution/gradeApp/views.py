from django.shortcuts import render
from .models import Teacher, Grade, Lesson, Student
from .serializers import TeacherSerializer, GradeSerializer, LessonSerializer, StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class TeacherMVS(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class GradeMVS(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # viewste uniqulik sağlamak için
        lesson=request.data["lesson_id"]#gelen datadan lesson_id bilgisini çekip değişkene atadık
        student=request.data["student_id"]#gelen datadan student_id bilgisini çekip değişkene atadık
        grade_qs=Grade.objects.filter(lesson=lesson,student=student)# Grade modelimizde iki şartı da sağlayan veriyi çektik
        if grade_qs.exists():# grade_qs verisi varsa kullanıcıya hata mesajı dönüyoruz
            message="Same lesson and student have a grade."
            return Response(message,status=status.HTTP_400_BAD_REQUEST)  
        else: #  grade_qs verisi yoksa gelen veriyi kaydediyoruz
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
    # Inherit aldığımız ModelViewSet e gittik oradan onun Inherit aldığı CreateApiViewe gittik create metodunu aldık burada override yapıp ilgili şartlarımız koymuş olduk.



class LessonMVS(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer