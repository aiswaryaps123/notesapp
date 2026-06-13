from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Note
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def hello(request):
    return HttpResponse("hai abhi ")
def hi(request):
    return JsonResponse({
        "name" : "abhi",
        "age" : 21
    })

#get api
def getnotes(request):
    list_notes = []
    notes = Note.objects.all()
    for note in notes:
        list_notes.append(
            {
                "id" : note.id,
                "title" : note.title,
                "content" : note.content

            }
        )
    return JsonResponse(list_notes, safe=False)

#post api
@csrf_exempt
def notes(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")
        user = User.objects.get(id=1)
        note = Note(
            title = title,
            content = content,
            user = user 
        )
        note.save()
        return JsonResponse({
            "message" : "successful"
        })
    
#delete api   
def deln(request):
        note = Note.objects.all()
        notedel = Note.objects.get(id=2)
        notedel.delete()
        return JsonResponse(
            {
                "message" : "deleted successfully"
            }
        )

#put api
def putnote(request):
     note=Note.objects.get(id=1)
     note.title = "new title"
     note.content = "now content"
     note.save()
     return JsonResponse(
          {
               "message" : "updated succesfully"
          }
     )

def notes(request,id):
     if request.method == "GET":
          notes=Note.objects.get(id=id)
          return JsonResponse(
               {
                    "id" : notes.id,
                    "title" : notes.title,
                    "content" : notes.content
               }
          )
     




        





      

