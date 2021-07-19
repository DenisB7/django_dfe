from django.urls import path

from hello.views import hello_view

app_name = 'hello'
urlpatterns = [
    path('', hello_view, name='hello-not-html'),
]
