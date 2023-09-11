from django.urls import path
from autenticar import views


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar')
   
]

