from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms import views

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', views.LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', views.LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lessons/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson_delete'),
] + router.urls
