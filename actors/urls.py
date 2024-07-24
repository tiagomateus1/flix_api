from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorCreateLisView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyApiView.as_view(), name='actor-detail-view'),
]
