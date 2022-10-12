from django.urls import path
from ..views.people import PeopleView

urlpeople = [
    path('people/', PeopleView.as_view(), name='people_list'),
    path('people/<int:id>', PeopleView.as_view(), name='people_process')
]