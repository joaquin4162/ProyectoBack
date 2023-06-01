from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm, RegistroFrom

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        print('paso por aca')
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print('paso por aca')
            password = form.cleaned_data['password']
            print('paso por aca')
            user = authenticate(request, username=username, password=password)
            print('paso por aca')
            if user is not None:
                login(request, user)
                print('paso por aca')
                return redirect('asd')  # Reemplaza 'home' con la URL a la que deseas redirigir después del inicio de sesión
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('profesional:lista_profesionales')  # Reemplaza '' con la URL a la que deseas redirigir después del cierre de sesión


#---------------------------

class Registerview(View):
    def get(self, request):
        form = RegistroFrom()
        return render(request, 'registro.html', {'form':form})
    
    def post(self, request):
        form = RegistroFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profesional:lista_profesionales') # Reemplaza '' con la URL a la que deseas redirigir después del registro
        return render(request, 'registro.html', {'form':form})