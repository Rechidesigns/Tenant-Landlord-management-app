from django.urls import path
from . import views


urlpatterns = [
    path('Apartment/', views.ApartmentView().as_view(), name="Apartment_List"),
    path('Apartment/<int:apartment_id>/', views.ApartmentDetailView.as_view(), name="Apartment_Detail"),
    path('Tenant/', views.TenantView().as_view(), name="Tenant_Iist"),
    path('Tenant/<int:tenant_id>/', views.TenantDetailView.as_view(), name="Tenant_Detail"),

]