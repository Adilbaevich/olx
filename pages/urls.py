from django.urls import path
from .views import (
    home,
    animal,
    create_transport,
    business_detail,
    electro,
    electro_detail,
    furnature,
    furnature_detail,
    realty,
    transport,
    transport_detail,
    animal_detail,
    transport_delete,
    transport_update,
    create_animal,
    animal_delete,
    animal_update,
    create,
    create_furnature,
    electro_delete,
    electro_update,
    furnature_delete,
    furnature_update
)

urlpatterns = [
    path('', home, name='home'),

    path('animal/', animal, name='animal'),
    path('animal/<int:pk>/', animal_detail, name='animal_detail'),
    path('create_animal/', create_animal, name='create_animal'),
    path('animal/<int:pk>/delete', animal_delete, name='animal_delete'),
    path('animal/<int:pk>/update', animal_update, name='animal_update'),

    path('business/<pk>/', business_detail, name='business_detail'),

    path('electro/', electro, name='electro'),
    path('create/', create, name='create'),
    path('electro/<int:pk>/', electro_detail, name='electro_detail'),
    path('electro/<int:pk>/delete', electro_delete, name='electro_delete'),
    path('electro/<int:pk>/update', electro_delete, name='electro_update'),

    path('furnature/', furnature, name='furnature'),
    path('furnature/<pk>/', furnature_detail, name='furnature_detail'),
    path('create_furnature/', create_furnature, name='create_furnature'),
    path('furnature/<pk>/delete', furnature_delete, name='furnature_delete'),
    path('furnature/<pk>/update', furnature_update, name='furnature_update'),

    path('realty/', realty, name='realty'),

    path('transport/', transport, name='transport'),
    path('create_transport/', create_transport, name='create_transport'),
    path('transport/<pk>/', transport_detail, name='transport_detail'),
    path('transport/<pk>/delete', transport_delete, name='transport_delete'),
    path('transport/<pk>/update', transport_update, name='transport_update'),
    
]