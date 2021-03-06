from django.urls import path

from adminapp.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, admin_users_restore, admin_products

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users_create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users_update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users_delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('users_restore/<int:user_id>/', admin_users_restore, name='admin_users_restore'),
    path('products/', admin_products, name='admin_products'),
]