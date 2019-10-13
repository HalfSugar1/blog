from django.urls import path
from . import views

app_name = 'control'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('register/',views.user_register,name='user_register'),
    path('delete/<int:id>',views.user_delete,name='user_delete'),
    path('edit/<int:id>/',views.profile_edit,name='profile_edit')
]