from django.urls import path

from password_generator_web.web.views import index_page, generate_unique_pass

urlpatterns = (
    path('', index_page, name='index page'),
    path('generate-password/', generate_unique_pass, name='generate pass'),
)