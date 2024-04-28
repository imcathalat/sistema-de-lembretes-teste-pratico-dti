from django.urls import path
from . import views

urlpatterns = [
    path('lembretes/', views.LembreteList.as_view(), name='lembretes'),
    path('lembretes/<uuid:lembrete_id>/', views.LembreteDelete.as_view(), name='excluir_lembrete'),
]