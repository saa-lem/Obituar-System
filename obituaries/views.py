from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Obituary
from datetime import datetime
def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        slug = name.lower().replace(" ", "-")

        # Create the obituary
        obituary = Obituary.objects.create(
            name=name, date_of_birth=date_of_birth,
            date_of_death=date_of_death, content=content,
            author=author, slug=slug
        )
        return HttpResponse("Obituary submitted successfully!")
    
    return render(request, 'obituary_form.html')
def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})
def homepage(request):
    # Redirect to the obituary submission or viewing page, or render a welcome page
    return redirect('view_obituaries')  # or 'submit_obituary'
def homepage(request):
    return render(request, 'home.html')
def view_obituaries(request):
    obituaries = Obituary.objects.all()
    context = {
        'obituaries': obituaries,
        'current_year': datetime.now().year
    }
    return render(request, 'view_obituaries.html', context)
