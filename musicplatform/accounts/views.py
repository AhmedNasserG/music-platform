from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import RegisterForm, LoginForm


class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        print('form', form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                print('User is authenticated')
                return redirect('/artists/')
            messages.error(request, 'Invalid username or password.')
        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, 'Account created successfully for ' + user)
            return redirect('/login/')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('/login/')


class LoginRequieredView(LoginRequiredMixin, View):
    login_url = '/login/'
