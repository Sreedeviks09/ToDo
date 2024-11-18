from .models import Task  # Importing the Task model from models.py to be used in the form
from django import forms  # Importing Django's forms module

# Defining the TodoForms class, which is a ModelForm for the Task model
class TodoForms(forms.ModelForm):
    
    # Meta class is used to define additional options for the ModelForm
    class Meta:
        model = Task  # Specifying that this form is based on the Task model
        fields = ['name', 'priority', 'date']  # Defining the fields that should be included in the form
