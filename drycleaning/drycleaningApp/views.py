from django.shortcuts import render
from django.views.generic import TemplateView
from drycleaningApp.forms import MessageForm
from .models import Message
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'dryApp/index.html')

def home(request):
    form = MessageForm()
    return render(request, 'dryApp/home.html', { 'form':form })

def my_messages(request):

        if request.method == 'POST':

            form = MessageForm(request.POST)

            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.POST.get('author')
                message.text = request.POST.get('text')
                message.phone = request.POST.get('phone')
                message.location = request.POST.get('location')

                message.save()

                messages.success(request, 'We appreciate your feedback, we will get back to you as soon as possible')
                return redirect('home')

            else:
                messages.error(request, 'Invalid form, please fill the necessary fields')
                return redirect('home')

        else:
            form = MessageForm()
        return render(request, 'dryApp/home.html', {'form': form})
