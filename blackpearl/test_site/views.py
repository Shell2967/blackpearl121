from django.shortcuts import render
from datetime import date
from .models import Feedback

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def contacts_page(request):
    return render(request, 'contacts.html')

def menu_page(request):
    return render(request, 'menu.html')

def navigate_page(request):
    return render(request, 'navigate.html')

def photo_page(request):
    return render(request, 'photo.html')


def reviews_page(request):

    context = {
        'feedback': Feedback.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )
    return render(request, 'reviews.html', context)

