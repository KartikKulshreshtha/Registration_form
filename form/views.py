from django.shortcuts import render, redirect
from .models import Detail 

def start(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        rollnumber = request.POST['rollnumber']
        section = request.POST['section']
        branch = request.POST['branch']
        year = request.POST['year']
        email = request.POST['email']
        adhaar_number = request.POST['adhaar_number']
        ins = Detail(name = name, age = age, rollnumber = rollnumber, section = section, branch = branch, year = year, email = email, adhaar_number = adhaar_number)
        ins.save()
    return render(request,'form/start.html')
    