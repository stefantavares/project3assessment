from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addwidget/', views.WidgetCreate.as_view(), name='add_widget'),
    # path('removewidget/<int:pk>/', views.RemoveWidget.as_view(), name='remove_widget')
    path('removewidget/<int:widget_id>/', views.remove_widget, name='remove_widget')
]