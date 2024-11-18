from django.urls import path
from event_planner import views

urlpatterns = [
    path('', views.list_events_view),
    path('list_events/', views.list_events_view, name='list_events_view'),
    path('list_conflicts/', views.list_conflicts_view, name='list_conflicts_view'),

]