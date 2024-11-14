from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def about (request):
    return render (request,"about.html")


def projects (request):
    projects_show=[
        {
            'title': 'My Django Portfolio',
            'path': 'images/djangoport.jpg',
            'demoLink': 'https://adeshdsouza94494.github.io/My-Portfolio/',
            'code': 'https://github.com/Adeshdsouza94494/My-Portfolio',
        },
        {
            'title': 'My React Portfolio',
            'path': 'images/port.jpg',
            'demoLink': 'https://adeshdsouza94494.github.io/My-Portfolio/',
            'code': 'https://github.com/Adeshdsouza94494/My-Portfolio',
        },
        {
            'title': 'My Shopping Cart',
            'path': 'images/cartt.jpg',
            'demoLink': 'https://adeshdsouza94494.github.io/My-shopping-cart/',
            'code': 'https://github.com/Adeshdsouza94494/My-shopping-cart',
        },

        {
            'title': 'My Todo React Js',
            'path': 'images/mytt.webp',
            'demoLink': 'https://adeshdsouza94494.github.io/React-Todo/',
            'code': 'https://github.com/Adeshdsouza94494/React-Todo',
        }
        ,


          {
            'title': 'Todo Javascript',
            'path': 'images/tt.webp',
            'demoLink': 'https://adeshdsouza94494.github.io/Todo-List/',
            'code': 'https://github.com/Adeshdsouza94494/Todo-List',
        },
         {
            'title': 'Drum Kit',
            'path': 'images/drumkit.jpg',
             'demoLink': 'https://adeshdsouza94494.github.io/Drum-kit/',
            'code': 'https://github.com/Adeshdsouza94494/Drum-kit',
        },
         {
            'title': 'CRUD',
            'path': 'images/crud.webp',
             'demoLink': 'https://killer123.pythonanywhere.com/',
            'code': 'https://github.com/Adeshdsouza94494/Django-CRUD',
        },
         {
            'title': 'Watch Shop',
            'path': 'images/ww.jpg',
             'demoLink': 'https://developer256.pythonanywhere.com/',
            'code': 'https://github.com/Adeshdsouza94494/WatchShop',
        },

    ]
    return render (request,"project.html",{"projects_show": projects_show})


def experience(request):
    experience=[
        {"company":"Pratian Technologies",
         "exp":"images/pratian.png",
         "position":"Software Developer Intern"},
        {"company":"Vitvara Technologies",
          "exp":"images/vit.jpeg",
         "position":"Embedded system design and IOT"},

    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myresume/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
    