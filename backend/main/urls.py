from django.urls import path
from . import views

urlpatterns = [
    path('lembretes/', views.LembreteList.as_view(), name='lembretes'),
]