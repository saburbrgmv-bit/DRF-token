from django.urls import path
from .views import *

urlpatterns = [
  path('create-list', BlogListCraeteView.as_view()),
  path('update-delete', BlogUpdateDeleteView.as_view()),
]