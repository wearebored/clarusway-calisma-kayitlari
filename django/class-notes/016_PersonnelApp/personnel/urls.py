from django.urls import path
from .views import DepartmentView, PersonnelListCreateView, PersonalGetUpdateDelete, DepartmentPersonnelView, Custom

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel/", PersonnelListCreateView.as_view()),
    path("personnel/<int:pk>/",PersonalGetUpdateDelete.as_view()),
    path("department/<str:name>/",Custom.as_view()),
    # path("department/<str:department>/", DepartmentPersonnelView.as_view()),
]
