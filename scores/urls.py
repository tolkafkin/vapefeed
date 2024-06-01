from django.urls import path

from scores.views import ScoreListAPIView, ScoreDetailAPIView, UserFeedbackScoreListAPIView, \
    UserFeedbackScoreDetailAPIView, LiquidFeedbackScoreListAPIView, LiquidFeedbackScoreDetailAPIView

app_name = 'scores'
urlpatterns = [
    path('', ScoreListAPIView.as_view(), name='list'),
    path('<int:pk>/', ScoreDetailAPIView.as_view(), name='detail'),

    path('feedback/', UserFeedbackScoreListAPIView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/', UserFeedbackScoreDetailAPIView.as_view(), name='feedback-detail'),

    path('liquid/', LiquidFeedbackScoreListAPIView.as_view(), name='liquid-list'),
    path('liquid/<int:pk>/', LiquidFeedbackScoreDetailAPIView.as_view(), name='liquid-detail'),
]
