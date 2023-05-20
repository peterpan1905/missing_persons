from django.shortcuts import render
from django.http import HttpResponse
from .models import Missing

def indexPageView(request) :
    return render(request, 'missingpersonsapp/index.html')

def BYUPageView(request) :
    return render(request, 'missingpersonsapp/BYU.html')

def contactPageView(request) :
    return render(request, 'missingpersonsapp/contact.html')

def projectsPageView(request) :
    return render(request, 'missingpersonsapp/projects.html')

def searchmissingpersonsPageView(request):
    sFirst = request.GET.get('firstName')
    sLast = request.GET.get('lastName')
    data = Missing.objects.filter(First_Name=sFirst, Last_Name=sLast)
    print(sFirst, sLast)
    print(data.count())
    if data.count() > 0:
        print(sFirst, sLast)
        context = {
            "Missing": data
        }
        
        return render(request, 'missingpersonsapp/viewmissingpersons.html', context)
    else:
        return render(request, 'missingpersonsapp/searchmissingpersons.html')


def addmissingpersonsPageView(request) :
    if request.method == 'POST':
        new_missing = Missing()
        new_missing.First_Name = request.POST.get("firstName")
        new_missing.Last_Name = request.POST.get("lastName")
        new_missing.city = request.POST.get("city")
        new_missing.state= request.POST.get("state")
        new_missing.age_at_missing = request.POST.get("ageAtMissing")
        new_missing.Date_Missing = request.POST.get("dateMissing")
        new_missing.gender = request.POST.get("gender")
        new_missing.race = request.POST.get("race")
        new_missing.case_link = request.POST.get("caseLink")
        print(new_missing.First_Name)
        new_missing.save()
    data = Missing.objects.all()
    context = {"Missing": data}
    return render(request, "missingpersonsapp/addmissingpersons.html", context)
        

    # what is this context doing? 
    # context = {"person": data}
    # dont forget to add context to the following line when we get to that point if we need context line of code given on line below
    # return render(request, 'missingpersonsapp/addmissingpersons.html', context)


def viewmissingpersonsPageView(request):

    if request.method =='POST':
        new_person = Missing()
        new_person.Date_Missing = request.POST.get('dateMissing')
        new_person.First_Name = request.POST.get('firstName')
        new_person.Last_Name = request.POST.get('lastName')
        new_person.age_at_missing = request.POST.get('ageMissing')
        new_person.city = request.POST.get('city')
        new_person.state = request.POST.get('state')
        new_person.gender = request.POST.get('gender')
        new_person.race = request.POST.get('race')
        new_person.case_link = request.POST.get('caseLink')
        new_person.save()
# somethins is wierd here and we need to fix it
# 
    data = Missing.objects.all()
    context = {"viewmissingpersons": data}
    return render(request, "missingpersonsapp/viewmissingpersons.html", context)


