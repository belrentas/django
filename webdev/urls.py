from django.urls import path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.show),
    path(r'add/', views.add),
    path(r'view_contacts/<int:contact_id>/',views.view_contacts, name='view_contacts'),
]