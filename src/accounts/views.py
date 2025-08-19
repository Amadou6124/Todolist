from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Connexion automatique après inscription
            return redirect('task-list')  # ou 'task_list' ou autre
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})