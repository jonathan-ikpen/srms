from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('medical_record/', views.MedicalRecordView.as_view(), name='medical_record'),
    path('exam_record/', views.ExamRecordView.as_view(), name='exam_record'),
    path('download_pdf/', views.DownloadPDFView.as_view(), name='download_pdf'), 
    path('performance_track/', views.PerformanceTrackView.as_view(), name='performance_track'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

