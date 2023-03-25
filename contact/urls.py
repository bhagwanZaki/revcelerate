from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', CompanyView,'product')

urlpatterns = [
    path('', ContactView.as_view(), name='contact-list'), 
    path('<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('companyContact/<str:name>', SearchCustomerByCompany.as_view(), name='contact-search'),
]

urlpatterns += router.urls