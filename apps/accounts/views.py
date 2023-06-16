from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.views import View

# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profesional:lista_profesionales') #cambiar para que redirija despues de registrar, puesto asi para mostrar que entra aca
        return render(request, 'registration.html',{'form':form})
    
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('profesional:lista_profesionales') #cambiar para que redirija despues de registrar, puesto asi para mostrar que entra aca
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    
    def logout_view(self, request):
        logout(request)
        return redirect('profesional:lista_profesionales')
    