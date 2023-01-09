from django.shortcuts import render

def map(request):
    return render (request,"html/imgmap.html")

def museum(request):
    return render (request,"html/museum.html")

def botanical(request):
    return render (request,"html/botanical.html")

def bronze(request):
    return render (request,"html/bronze.html")
    
def children(request):
    return render (request,"html/children.html")

def theater(request):
    return render (request,"html/theater.html")


# Create your views here.
