from django.urls import path
from django.conf.urls import include

from views.requires import RequiresView

urlpatterns = [
    path('requires', RequiresView.as_view()),
]
