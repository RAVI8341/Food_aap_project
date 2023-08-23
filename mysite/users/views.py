from django.shortcuts import redirect,render
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# views for user registration form
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome', {username}, 'your account has been created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html',{'form':form})

# creating a users profile view
@login_required
def profilepage(request):
    return render(request, 'users/profile.html',{'user': request.user})