from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.faculty_login, name='faculty_login'),
    
    path('salary/', views.view_salary_information, name='view_salary_information'),
    path('record_teaching_activity/', views.record_teaching_activity, name='record_teaching_activity'),
    path('faculty_dashboard',views.faculty_dashboard,name='faculty_dashboard'),
    path('download/csv/', views.download_csv, name='download_csv'),
    path('download/doc/', views.download_doc, name='download_doc'),
    path('logout/', views.faculty_logout, name='faculty_logout'),
    path('superuser_dashboard/', views.superuser_dashboard, name='superuser_dashboard'),
    path('admin/csv/', views.admin_csv, name='admin_csv'),
    path('admin/doc/', views.admin_doc, name='admin_doc'),
    path('profile/', views.profile_view, name='profile'),
    path("",views.home),
    path('download_excel/', views.download_excel, name='download_excel'),
]
