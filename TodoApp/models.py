from django.db import models  # Importing the models module from Django

# Creating a Task model to represent a task in the database
class Task(models.Model):
    
    # Defining a 'name' field for the task, which will be a character field (text field)
    name = models.CharField(max_length=250)  # Max length of 250 characters
    
    # Defining a 'priority' field for the task, which will be an integer field (e.g., 1, 2, 3, etc.)
    priority = models.IntegerField()  # Integer to represent the priority of the task
    
    # Defining a 'date' field to store the task's due date, which will be a date field
    date = models.DateField()  # Date field to store the task's date (without time)
    
    # Defining a __str__ method to return a string representation of the Task object
    # This method will return the task's name when the task is printed or displayed
    def __str__(self):
        return self.name
