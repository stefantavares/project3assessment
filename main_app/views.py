from pyexpat import model
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView
from.forms import CreateWidgetForm
from .models import Widget

# Create your views here.

def index(request):
    widgets = Widget.objects.all()
    widget_form = CreateWidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form})

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'

def remove_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('index')