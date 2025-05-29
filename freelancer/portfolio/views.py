from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("This a freelancing project. I also have a portfolio app within")

def services(request):
    services_list = ['Python Developer', 'Front-end Developer', 'Virtual Assistant' ]
    return render(request, 'portfolio/services.html', {'services': services_list})

def testimonials(request):
    testimonials_data = {
        'Mr Solomon': 'Great experience.... I love his customer relations.',
        'Bro Ephraim': 'He delivered a superb service. I will like to deal more with him.',
        'Mr Samuel': 'Delivered the project on time and exceed expectation.',
    }
    return render(request, 'portfolio/testimonials.html', {'testimonials': testimonials_data})

def pricing(request):
    pricing_data = {
        'Python Development': '$1200',
        'Front-end Developer': '$800',
        'Virtual Assistant': '$100',
    }
    return render(request, 'portfolio/pricing.html', {'pricing': pricing_data})

def  blog(request):
    return render(request, 'portfolio/blog.html')

def case_studies(request):
    return render(request, 'portfolio/case_studies.html')