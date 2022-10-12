from django.urls import path
from ..views.company import CompanyView

urlcompany = [
    path('companies/', CompanyView.as_view(), name = 'companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name = 'companies_process'),
]