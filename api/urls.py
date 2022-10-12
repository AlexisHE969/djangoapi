from django.urls import path
from .routes import urlcompany, urlpeople


urlpatterns = urlcompany
urlpatterns += urlpeople

