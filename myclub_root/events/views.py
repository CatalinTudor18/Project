
from django.shortcuts import redirect, render
from datetime import date
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponse
from events.models import Item

def index(request, year=date.today().year,month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099 : year = date.today().year
    month_name = calendar.month_name[month]
    title = "Webpage"
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
     {
        'date': '20-5-2020', 'announcement': "Open Website - First run - It's workiiinggg!!!"
     },
     {
         'date': '23-5-2020', 'announcement': "Got stuck like a noob"
     },
     {
         'date': '25-5-2020', 'announcement': "Linked my first page"
     },
     {
         'date': '26-5-2020', 'announcement': "Working on those requirements"
     },
    ]
    return render(request, 'events/calendar_base.html', {'title' : title, 'cal' : cal, 'announcements': announcements})

def About(request):
    return render(request, 'events/About.html')

def Enjoy(request):
    return render(request, 'events/Enjoy.html')

def Upcoming_year(request):
    return render(request, 'events/Upcoming_year.html')

def How(request):
    return render(request, 'events/How.html')

def Home(request):
    return render(request, 'events/Home.html')

def CV(request):

    #if request.method == 'POST':
        #Item.objects.create(text=request.POST['item_text'])
        #return redirect('/')
    #else:
        #new_item_text = ''

    #items = Item.objects.all()
    #{'items': items}
    return render(request, 'events/CV.html')
