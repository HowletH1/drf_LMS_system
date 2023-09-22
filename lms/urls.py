from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms import views

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/', views.LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/create/', views.LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lessons/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('payments/', views.PaymentListAPIView.as_view(), name='payments_list'),
    path('payments/create/', views.PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payments/<int:pk>/', views.PaymentRetrieveAPIView.as_view(), name='payment'),
    path('payments/update/<int:pk>/', views.PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('payments/delete/<int:pk>/', views.PaymentDestroyAPIView.as_view(), name='payment_delete'),
] + router.urls
