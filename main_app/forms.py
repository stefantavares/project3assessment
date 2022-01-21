
from django.forms import ModelForm
from .models import Widget

class CreateWidgetForm(ModelForm):
  class Meta:
    model = Widget
    fields = ['description', 'quantity']