from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    
    
    path('index/', views.home_index, name='index'),
    # path('home/<int:admin_id>/', views.home, name='home'),
    path('home/', views.home, name='home'),

    
    path('main_company_add/', views.main_company_add, name='main_company_add'),
    path('', views.log_in, name='log_in'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-record/<int:id>/', views.edit_record, name='edit_record'),
    path('update-record/', views.update_record, name='update_record'),
    path('payment_details/<int:id>/', views.payment_details, name='payment_details'),
    path('export/', views.export_users, name='export_users'),
    path('get-team-leader-name/', views.get_team_leader_name, name='get_team_leader_name'),
    
    
    # path('baluhome/', views.baluhome, name='baluhome'),
    path('baluhome/<str:admin_id>/', views.baluhome, name='baluhome'),
    path('edit_company/<str:admin_id>/', views.edit_company, name='edit_company'),
    
    # path('balu_company_add/<str:admin_id>/', views.balu_company_add, name='balu_company_add'),
    path('balu_company_add/<str:admin_id>/', views.balu_company_add, name='balu_company_add'),

    path('balu_company_index/', views.balu_company_index, name='balu_company_index'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
]
