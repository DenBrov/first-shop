from django.urls import path

from adminapp.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin_users/', admin_users, name='admin_users'),
    path('admin_users_create/', admin_users_create, name='admin_users_create'),
    path('admin_users_update/', admin_users_update, name='admin_users_update'),
    path('admin_users_delete/', admin_users_delete, name='admin_users_delete')
]