from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', views.ReviewRetrieUpdateDestroyView.as_view(), name='review-detail'),
]
