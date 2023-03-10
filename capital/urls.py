from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('play-quiz',views.home,name="home"),
    path('answer',views.answer_view,name="answer-view")
]