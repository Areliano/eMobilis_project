from django.shortcuts import render, redirect

from .models import Restaurant, Customer, Aboutpage, Menu, Homepage, Stories

from django.utils import timezone

from django.http import HttpResponse

#from restaurant.models import Homepage



# Create your views

def index(request):
     index = Homepage.objects.all()
     return render(request, 'index.html', {"index": index})


def stories(request):
    stories = Stories.objects.all()
    return render(request, 'blog.html', {"index": index})


def about(request):
    about = Aboutpage.objects.all
    return render(request, "about.html", {"link": "about", "about":about})


def blog(request):
    stories = Stories.objects.all()
    return render(request, "blog.html", {"stories": stories})


# def blog-single(request):
#  return render(request, "blog-single.html", {"link":"blog-single"})


def contact(request):
    return render(request, "contact.html", {"link": "contact"})


# def index(request):
#     return render(request, "index.html", {"link":"index"})


def menu(request):
    return render(request, "menu.html", {"link": "menu"})


def reservation(request):
    return render(request, "reservation.html", {"link": "reservation"})

def booked(request):
    customers = Customer.objects.all()
    return render(request, "booked.html", {"link":"booked", "data":customers})

def dropdown(request):
    return render(request, "dropdown.html", {"link":"dropdown"})

def delete(request, id):
    satisfied_customer = Customer.objects.get(id=id)

    satisfied_customer.delete()

    return render(request, 'booked.html')


def insertdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        person = request.POST.get('person')

        Customer1 = Customer(name=name, email=email, phone=phone, date=date, time=time, person=person)
        Customer1.save()
        return redirect("/booked")

    return redirect("/booked")


def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        person = request.POST.get('person')

        satisfied_customer = Customer.objects.get(id=id)

        satisfied_customer.name=name
        satisfied_customer.email = email
        satisfied_customer.phone = phone
        satisfied_customer.datetime = date
        satisfied_customer.time = time
        satisfied_customer.person = person

        satisfied_customer.save()
    satisfied_customer = Customer.objects.get(id=id)

 #   customers = Customer.objects.all()

    return render(request, 'edit.html', {'Customer':satisfied_customer})
    return redirect("/booked")



#get.request.POST['name']

#    return render(request, 'booked.html')


def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu':menu})



