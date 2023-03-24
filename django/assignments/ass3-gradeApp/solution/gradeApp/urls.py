from django.urls import path, include
from rest_framework import routers
from .views import TeacherMVS, GradeMVS, StudentMVS, LessonMVS

router = routers.DefaultRouter()
router.register("teachers",TeacherMVS)
router.register("grades",GradeMVS)
router.register("students",StudentMVS)
router.register("lessons",LessonMVS)

urlpatterns = router.urls