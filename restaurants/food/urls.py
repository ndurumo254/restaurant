from django.urls import path
from.import views

urlpatterns = [
    path('', views.index,name="index"),
    path("detail/<int:id>/", views.detail,name="detail"),
    path("add/food", views.create_item,name="create_item")
]