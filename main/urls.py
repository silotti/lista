from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista_compras'),
    path('item/<int:item_id>/update_quantity/', views.update_quantity, name='update_quantity'),
    path('adicionar/', views.adicionar_item, name='adicionar_item'),
]
