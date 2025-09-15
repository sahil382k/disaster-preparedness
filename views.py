from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def alerts_contacts(request):
    return render(request, 'alerts/alerts_contacts.html')