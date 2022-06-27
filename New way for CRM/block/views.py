from multiprocessing import context
from django.shortcuts import redirect, render, reverse
from django.views import generic
from .forms import Registration
from .models import *

def home(request):
    
    navbar = Navbar.objects.all()
    slayd = Slayd.objects.all()
    body = Body.objects.all()
    body1 = Body1.objects.all()
    end = End.objects.all()
    
    context = {
        "navbar":navbar,
        "slayd":slayd,
        "body":body,
        "body1":body1,
        "end":end  
    }
    
    return render(request, 'index.html', context)
    

class Register(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = Registration
    
    def get_success_url(self):
        return reverse('django:home')