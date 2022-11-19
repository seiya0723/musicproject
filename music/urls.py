from django.urls import path


#TODO:ここを直す
#from .migrations import views
from . import views


urlpatterns = [

    path('music/', views.ListMusicView.as_view()),
    
]
