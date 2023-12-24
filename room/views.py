from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Room, Message

@login_required
def rooms(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        room = None
        if not Room.objects.filter(name=room_name).exists():
            room = Room.objects.create(name=room_name)
            room.save()
        #messages = Message.objects.filter(room=room)
        #return render(request, 'room/room.html', {'room': room, 'messages': messages})
        # url = f'rooms/';
        # print(url)
        url_redirect = reverse('room:room',args=[room_name]);
        return redirect(url_redirect)
    return render(request, 'room/rooms.html')

@login_required
def room(request, room_name):
    
    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=room)
    
    return render(request, 'room/room.html', {'room': room, 'messages': messages})