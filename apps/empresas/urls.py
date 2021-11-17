from django.urls import path
from .views import EmpresasCreate, EmpresasEdit

urlpatterns = [
    path('novo/', EmpresasCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresasEdit.as_view(), name='edit_empresa'),
]
