from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def people(request):
    return render(request,'people.html')

def research_area(request):
     return render(request,'research_area.html')\

def publication(request):
    return render(request,'publications.html')

def alumni(request):
    return render(request,'alumni.html')

def lab_life(request):
    return render(request,'lab_life.html')

def area_gis(request):
    return render(request,'area_gis.html')

def area_disaster(request):
    return render(request,'area_disaster.html')

def area_rs(request):
    return render(request,'area_rs.html')

def mj(request):
    return render(request,'mainPage.html')

def typhoon_1(request):
    return render(request,'1_typhoon.html')

def isolate_3(request):
    return render(request,'isolate_3.html')

def reservoir_4(request):
    return render(request,'reservoir_4.html')

def burstiness_1(request):
    return render(request,'1_burstiness.html')

def sink_6(request):
    return render(request,'6_sink.html')

def damage_7(request):
    return render(request,'7_damage.html')

def evacuation_8(request):
    return render(request,'8_evacuation.html')

def reallsolate_9(request):
    return render(request,'9_realsolate.html')

