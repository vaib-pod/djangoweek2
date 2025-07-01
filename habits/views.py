from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import DailyHabit
from .forms import HabitForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



def home_page(request):
    return render(request, 'home.html')

@login_required
def habit_list(request):
    habits = DailyHabit.objects.all().order_by('-date_added')
    return render(request, 'habit_list.html', {'habits' : habits})
@login_required
def habit_create(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')      
    else:
        form = HabitForm()
    return render(request, 'habit_form.html', {'form':form})
@login_required   
def habit_edit(request , habit_id):
    habit = get_object_or_404(DailyHabit , pk = habit_id, user = request.user)
    if request.method == "POST":
        form = HabitForm(request.POST, instance = habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit_form.html', {'form':form})
@login_required
def habit_delete(request, habit_id):
    habit = get_object_or_404(DailyHabit, pk = habit_id,user = request.user)
    if request.method == 'POST':
        habit.delete()
        return redirect('habit_list')
    return render(request, 'habit_confirm_delete.html', {'habit' : habit})
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('habit_list')
            
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})
