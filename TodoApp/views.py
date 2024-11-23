from django.shortcuts import redirect, render  # Importing necessary functions for view handling
from .models import Task  # Importing the Task model to interact with the database
from .forms import TodoForms  # Importing the TodoForms class to handle task forms
from datetime import datetime  # Importing datetime (though not used in the code)

# View to add a new task
def Taskadd(request):
    # Fetching all tasks from the Task model to display on the home page
    task1 = Task.objects.all()
    
    # If the request method is POST (form submission)
    if request.method == 'POST':
        # Retrieving data from the form (name, priority, and date)
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        
        # Creating a new Task object with the retrieved data
        task = Task(name=name, priority=priority, date=date)
        
        # Saving the new task to the database
        task.save()
        
    # Rendering the home page (home.html) and passing the tasks to display
    return render(request, 'index.html', {'task1': task1})

# View to handle deleting a task
def delete(request, taskId):
    # Fetching the task to be deleted using the provided taskId
    task2 = Task.objects.get(id=taskId)
    
    # If the request method is POST (confirmation to delete)
    if request.method == 'POST':
        # Deleting the task from the database
        task2.delete()
        # Redirecting to the home page after deletion
        return redirect('/')
    
    # Rendering the delete confirmation page with the task details
    return render(request, 'delete.html', {'task2': task2})

# View to handle updating a task
def update(request, id):
    # Fetching the task to be updated using the provided task ID
    task3 = Task.objects.get(id=id)
    
    # Binding the form to the POST data and the existing task instance
    f = TodoForms(request.POST or None, instance=task3)
    
    # If the form is valid after submission
    if f.is_valid():
        # Saving the updated task data to the database
        f.save()
        # Redirecting to the home page after updating the task
        return redirect('/')
    
    else:
        # Debugging: print form errors to the console if the form is not valid
        print(f.errors)
        # If the form is not valid, rendering the edit page with the form and task details
        return render(request, 'edit.html', {'f': f, 'task3': task3})
    
    # If the form is empty or no data is passed, rendering the edit page with the form and task details
    return render(request, 'edit.html', {'f': f, 'task3': task3})
