from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>/', views.ReviewRetriveUpdateDestroyView.as_view(), name='reviews-detail-view'),
]
