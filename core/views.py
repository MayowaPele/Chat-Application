from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {
       'username': username,
       'room_name': room,
        'room_details': room_details
    }
    return render(request, 'room.html', context)

def checkroom(request):
    room = request.POST['room_name']
    user_name = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+user_name)
    else:
        new_room = Room.objects.create(name=room) 
        new_room.save()
        return redirect('/'+room+'/?username='+user_name)

def sendMessage(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']

    new_message = Message.objects.create(value=message, user=username, room_id=room_id)
    new_message.save()
    
   

def getMessages(request, room):
    Room_details = Room.objects.get(name=room)

    room_messages = Message.objects.filter(room_id=Room_details.id)
    return JsonResponse({'messages':list(room_messages.values())})
