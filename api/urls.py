from django.urls import path
from . import views
#this is class based urlpatterns
urlpatterns = [
    path('', views.PlanListView.as_view(), name='plan-list'),
    path('plans/create/', views.PlanCreateView.as_view(), name='plan-create'),
    path('plans/delete/<int:pk>/', views.PlanDestroyView.as_view(), name='plan-delete'),
    path('plans/update/<int:pk>/', views.PlanupdateView.as_view(), name='plan-update'),
]
