from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
# views for user registration form
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.method)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome', {username}, 'your account has been created')
            return redirect('food:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html',{'form':form})