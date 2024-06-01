from django.urls import path

from feedbacks.views import FeedbackListCreateAPIView, FeedbackDetailAPIView

app_name = 'feedbacks'
urlpatterns = [
    path('', FeedbackListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', FeedbackDetailAPIView.as_view(), name='detail'),
]
