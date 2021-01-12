from django.shortcuts import render

# Create your views here.


# home view
def index(request):
    return render(request, 'index.html', {})

# room view


def room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'chatroom.html', context)
