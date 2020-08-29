
from django.shortcuts import redirect, render
from datetime import date
import smtplib
import imghdr
from PIL import Image, ImageDraw, ImageFont
import textwrap
import calendar
import re
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

    if request.method == 'POST':
        global template_loc, tmp, img_h, data
        data = request.POST

        template_loc = "myclub_site/static/Template.jpg"
        tmp = Image.open(template_loc)
        smallsz = 15
        textsz = 30
        mediumsz = 35
        iconsize = 50

        xName, yName = drawtxt(data['name'], 35, (0,0,0), 150, 250, 120, path="/myclub_site/static/Optima.ttc")
    #Drawing Icons -----------
        font = ImageFont.truetype("/myclub_site/static/Optima.ttc", mediumsz)
        img_h = font.getsize('I')[1]
        xIcon = 180
        yIcon = 330

        drawimage("myclub_site/static/mail.jpg", 180, yIcon)
        xIcon, yIcon = drawtxt(data['email'], 100, (0,0,0), mediumsz, xIcon + 85, yIcon)

        drawimage("myclub_site/static/Linkedin.png", 180, yIcon + 30)
        xIcon, yIcon = drawtxt(data['linkedin'], 100, (0,0,0), mediumsz, 180 + 85, yIcon + 30)

        drawimage("myclub_site/static/home.jpg", 180, yIcon + 40)
        xIcon, yIcon = drawtxt(data['address'], 100, (0,0,0), mediumsz, 180 + 85, yIcon + 40)

        drawimage("myclub_site/static/Phone.jpg", 800 , 330)
        xIcon, yIcon = drawtxt(data['number'], 100, (0,0,0), mediumsz, 800 + 85, 330)


    #Drawing Summary ----------
        xmary, ymary = drawtxt("Summary", 100, (0,0,0), iconsize, 180, 700)
        xmary, ymary = drawtxt(data['summary'], 100, (0,0,0), textsz, xmary + 20, ymary + 20)


    #Drawing Education ----------
        xEdu, yEdu = drawtxt("Education", 100, (0,0,0), iconsize, 180, ymary + 50)
        xEdu += 20
        for i in range(1,4):
            s = 'school' + " " + str(i)
            y = 'year' + " " + str(i)
            m = 'marks' + " " + str(i)

            if(data[s] != ''):

                xEdu, yEdu = drawtxt(data[s] + " - Graduated in " + data[y] + ", with an average of " + data[m], 100, (0,0,0), textsz, xEdu, yEdu + 20)


    #Drawing Experience ----------
        xExp,yExp = drawtxt("Experience and Projects", 100, (0,0,0), iconsize, 180, yEdu + 50)
        xExp,yExp = drawtxt(data['experience'], 70, (0,0,0), textsz, 180 + 20, yExp + 20)

    #Drawing Skills ----------
        xSkil, ySkil = drawtxt("Skills", 100, (0,0,0), iconsize, 180, yExp + 50)
        xSkil, ySkil = drawtxt(data['skills'], 100, (0,0,0), textsz, 180 + 20, ySkil)
        tmp.show()

        return render(request, 'events/sent.html')
    return render(request, 'events/CV.html')

def drawimage(fileloc, x, y):
    img = Image.open(fileloc).resize((img_h + 8, img_h + 8)).convert("L")
    tmp.paste(img, (x,y))

def drawtxt(text, numberWords,fontcolor, size, x, y, path="/myclub_site/static/Optima.ttc"):
    draw = ImageDraw.Draw(tmp)
    font = ImageFont.truetype(path, size)
    lines = textwrap.wrap(text, numberWords)

    for line in lines:
        p, j = font.getsize(line)
        draw.text(xy=(x, y), text = line, fill = fontcolor, font = font)
        y = y + j + 6

    return x, y
