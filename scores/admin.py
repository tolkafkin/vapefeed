from django.contrib import admin
from .models import Score, UserFeedbackScore, LiquidFeedbackScore


admin.site.register(Score)
admin.site.register(UserFeedbackScore)
admin.site.register(LiquidFeedbackScore)
