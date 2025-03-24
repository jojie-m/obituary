from django.shortcuts import render, get_object_or_404, redirect
from .models import Obituary
from .forms import ObituaryForm

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_obituaries')
    else:
        form = ObituaryForm()
    return render(request, 'submit_obituary.html', {'form': form})

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})

def view_obituary_detail(request, slug):
    obituary = get_object_or_404(Obituary, slug=slug)
    return render(request, 'obituary_detail.html', {'obituary': obituary})