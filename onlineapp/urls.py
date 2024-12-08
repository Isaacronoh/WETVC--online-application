from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('onlineapplication/', views.apply, name='apply'),
    path('about/', views.about_us, name='about_us' ),
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('courses/', views.courses, name='courses'),
    path('applications/', views.application_list, name='application_list'),
    path('search/', views.search, name='search'),
    path('studentregistration/', views.studentregistration, name='studentregistration'),
    path('staffregistration/', views.staffregistration, name='staffregistration'),
    path('dashboard/', views.dashboard, name='studentdashboard'),
    path('login/', views.student_login, name='studentlogin'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('staffdashboard/', views.staffdashboard, name='staffdashboard'),
    path('finance/', views.finance, name='finance'),
    path('staff/enter-results/', views.staff_enter_results, name='staff_enter_results'),
    path('staff/edit-results/', views.staff_edit_results, name='staff_edit_results'),
    path('student/view-results/', views.student_view_results, name='student_view_results'),
    path('edit/<int:pk>/', views.edit_application, name='edit_application'),
    path('delete/<int:pk>/', views.delete_application, name='delete_application'),
    path('logout/', views.logout, name='logout'),
    path('staff/personal-info/', views.staff_personal_info, name='staff_personal_info'),
    path('staff/view-results/', views.staff_view_results, name='staff_view_results'),

]
