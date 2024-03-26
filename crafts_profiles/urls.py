from django.urls import path
from crafts_profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<str:username>', views.ProfileDetail.as_view())
]