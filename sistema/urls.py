from django.urls import path
from sistema import views

# Informa qual sera a rota que ira chamar determinana view(função).
urlpatterns = [
    path('sistema/', views.index),
]