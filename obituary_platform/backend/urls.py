from django.urls import path
from .views import submit_obituary, view_obituaries, view_obituary_detail

urlpatterns = [
    path('', view_obituaries, name='view_obituaries'),
    path('submit/', submit_obituary, name='submit_obituary'),
    path('<slug:slug>/', view_obituary_detail, name='obituary_detail'),
]