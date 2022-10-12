from django.urls import path
from ..views.quiz import QuizView

urlquiz = [
    path('quiz/', QuizView.as_view(), name='quiz_list'),
    path('quiz/<int:id>', QuizView.as_view(), name='quiz_process')
]