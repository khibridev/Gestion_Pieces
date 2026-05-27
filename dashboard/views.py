from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_admin(request):
    return render(request, 'dashboard/admin.html')

@login_required
def dashboard_client(request):
    return render(request, 'dashboard/client.html')