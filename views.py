from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations

# Create your views here.
def index(request):
    dest1 = Destinations()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.img = 'mumbai.jpg'
    dest1.price = 2000
    dest1.offer = False

    dest2 = Destinations()
    dest2.name = 'Chennai'
    dest2.desc = 'The city of Pilgrimages,Palaces,Lakes'
    dest2.img = 'chennai.jpg'
    dest2.price = 1500
    dest2.offer = False


    dest3 = Destinations()
    dest3.name = 'Kolkata'
    dest3.desc = 'The "cultural capital of India".'
    dest3.img = 'kolkata.jpg'
    dest3.price = 1000
    dest3.offer = True


    dests = [dest1 ,dest2 , dest3]


   


    
    return render(request, 'index.html', {'dests': dests})
    