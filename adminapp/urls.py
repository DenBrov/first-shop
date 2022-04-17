from django.urls import path

from adminapp.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete, admin_users_restore

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users_create/', admin_users_create, name='admin_users_create'),
    path('users_update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('users_delete/<int:user_id>/', admin_users_delete, name='admin_users_delete'),
    path('users_restore/<int:user_id>/', admin_users_restore, name='admin_users_restore'),
]