from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip
import re
import bcrypt
import time
from datetime import date, datetime

def index(request):
    return render(request, "crud/index.html")

def register(request):
    noerrors = False
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    hashedpassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    pwconf = request.POST['pwconf']
    if(len(firstname)<3):
        noerrors = True
        messages.error(request, "First Name must be longer than 3 characters", extra_tags="firstname")
    if(len(lastname)<3):
        noerrors = True
        messages.error(request, "Last Name must be longer than 3 characters", extra_tags="lastname")
    if not EMAIL_REGEX.match(email):
        noerrors = True
        messages.error(request, "Must be a Valid Email", extra_tags = "email")
    if(len(password) < 8):
        noerrors = True
        messages.error(request, "Password must be longer than 8 characters", extra_tags ="password")
    if(password != pwconf):
        noerrors = True
        messages.error(request, "Your passwords do not match", extra_tags = "pwconf")
    # if not password.isalpha():
    #     noerrors = True
    #     messages.error(request, "Password must be characters")
    if noerrors:
        print "hello"
        return redirect('/')
    else:
        newuser = User.objects.create(firstname=firstname, lastname=lastname, email = email, password = hashedpassword)
        newdict = {"id": newuser.id, "firstname" : newuser.firstname, "lastname": newuser.lastname, "email":newuser.email}
        request.session['user'] = newdict
        return redirect('/travels')

def login(request):
    email = request.POST['login_email']
    password = request.POST['login_password']
    user = User.objects.filter(email = email)
    usercheck = user[0]
    if bcrypt.checkpw(password.encode(), usercheck.password.encode()):
        newdict = {"id": usercheck.id,"firstname" :usercheck.firstname, "lastname": usercheck.lastname, "email":usercheck.email}
        request.session['user'] = newdict
        return redirect('/travels')
    else:
        return redirect('/')

def travels(request):
    newlist2 = []
    newlist = []
    user = request.session['user']
    userid = user['id']
    creater = User.objects.get(id = userid)
    createrid = creater.id
    trips = Trip.objects.filter(creater=creater)
    othertrips = Trip.objects.all().exclude(creater=creater)
    # adds to the top list
    for trip in othertrips:
        tracker = True
        for user in trip.users.filter():
            if user.id != userid:
                continue
            else:
                newlist.append(trip)
                tracker = False
                break
        if tracker == True:
            newlist2.append(trip)
    print newlist2
        

    context = {
        "trips" : trips,
        "newlist" : newlist,
        "othertrips" : newlist2,
    }
    return render(request, "crud/travels.html", context)

def display_addtrip(request):
    return render(request,"crud/add.html")

def addprocess(request):
    noerrors = False
    user = request.session['user']
    userid = user['id']
    creater = User.objects.get(id = userid)
    destination = request.POST['destination']
    plan = request.POST['plan']
    startdate = request.POST['startdate']
    enddate = request.POST['enddate']
    if len(destination)<1:
        noerrors = True
        messages.error(request, "No Destination input")
    if len(plan)<1:
        noerrors = True
        messages.error(request, "No Description input")
    try:
        s = datetime.strptime(startdate, "%Y-%m-%d").date() 
        e = datetime.strptime(enddate, "%Y-%m-%d").date() 
    except:
        messages.error(request, "invalid datetime format")
        return redirect('/travels/add')

    now = datetime.now().date()
    if s>e or s<now:
        messages.error(request, "invalid datetime")
        return redirect('/travels/add')

    if noerrors:
        return redirect('/travels/add')

    newtrip = Trip.objects.create(destination = destination, plan = plan, startDate = startdate, endDate = enddate, creater = creater)
    return redirect('/travels')

def traveljoin(request, id):
    user = request.session['user']
    userid = user['id']
    user_to_be_added = User.objects.get(id = userid)
    trip = Trip.objects.get(id=id)
    trip.users.add(user_to_be_added)
    trip.save()
    return redirect('/travels')

def displaytrip(request, id):
    trip = Trip.objects.get(id=id)
    otherusers= trip.users.all()
    context = {
        "trip": trip,
        "otherUsers": otherusers
    }
    return render(request, "crud/destination.html", context)
def logout(request):
    del request.session['user']
    return redirect('/')