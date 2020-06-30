from django.urls import path
from django.conf.urls import include

from views.requires import RequiresView
from views.stdlib import StdlibView

urlpatterns = [
    path('requires', RequiresView.as_view()),
    path('stdlib', StdlibView.as_view()),
]
