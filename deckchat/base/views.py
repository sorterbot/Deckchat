from multiprocessing import context
import re
from django.shortcuts import render


rooms = [
    {'id':1, 'name':'Jund'},
    {'id':2, 'name':'Jeskai Murktide'},
    {'id':3, 'name':'Naya Depths'},
]

def home(request):
    context={'rooms': rooms}
    return render(request, 'base/home.html', context)

    
def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context={'room':room}
    return render(request, 'base/room.html', context)
