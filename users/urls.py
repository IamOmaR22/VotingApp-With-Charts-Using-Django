from django.urls import path
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
]