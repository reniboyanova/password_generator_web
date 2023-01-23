from django.urls import path

from password_generator_web.web.views import index_page

urlpatterns = (
    path('', index_page, name='index page'),
)