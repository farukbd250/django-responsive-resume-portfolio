
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


from portfolio.models import About, Category, Global, Portfolio, Review, Service, Skills, Work

# Create your views here.
def index(request):
    global_data = Global.objects.all()[0]
    about = About.objects.all()[0]
    technical_skills = Skills.objects.filter(type = "Technical")
    proffesional_skills = Skills.objects.filter(type = "Proffesional")
    education = Work.objects.filter(type = "Education")
    work = Work.objects.filter(type = "Work")
    service = Service.objects.all()
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    review = Review.objects.all()
    
   
   
    context={
        "global":global_data,
        "about": about,
        "technical_skills":technical_skills,
        "proffesional_skills":proffesional_skills,
        "educations": education,
        "works": work,
        "sevices":service,
        "categories":categories,
        "portfolios":portfolios,
        "review":review,
    }
    return render (request,'portfolio/index.html',context)
#views.py


