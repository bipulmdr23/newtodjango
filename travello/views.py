from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Nepal'
    dest1.desc = 'lland of the dead'
    dest1.img ='destination_6.jpg'
    dest1.price = 123
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'LA'
    dest2.desc = 'lld'
    dest2.img = 'destination_5.jpg'
    dest2.price = 23
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'BHUTAN'
    dest3.desc = 'lasd'
    dest3.img = 'destination_3.jpg'
    dest3.price = 12323
    dest3.offer = True

    dests = [dest1,dest2,dest3]

    return render(request,'index.html',{'dests':dests})