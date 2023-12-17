from django.urls import path
from rest_framework.routers import DefaultRouter

from study.apps import StudyConfig
from study.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView

app_name = StudyConfig.name
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')


urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
] + router.urls
