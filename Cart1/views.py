from django.shortcuts import render
from .forms import RentdaysForm

# Create your views here.
def rentdays(request):
    dform = RentdaysForm(request.POST)
    if request.method == 'POST':
        if dform.is_valid():
            days = dform.cleaned_data['days']
            dform.save()

        else:
            dform = RentdaysForm()
    template = 'days.html'
    return render(request, template, {'form': dform})