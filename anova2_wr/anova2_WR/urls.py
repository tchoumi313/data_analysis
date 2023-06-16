from django.urls import path
from . import views

urlpatterns = [
    path('values/', views.anova_view, name='anova_values'),
    path('', views.index, name='index'),
    path('data/', views.validate_params, name='validate_params'),
]