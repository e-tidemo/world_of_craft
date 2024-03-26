# crafts_panel/urls.py
from django.urls import path
from . import views

app_name = 'crafts_panel'

urlpatterns = [
    path('admin/panel/', views.PanelCreateView.as_view(), name='panel-create'),
]
