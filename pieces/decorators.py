from django.shortcuts import redirect
from django.contrib import messages

def role_required(*roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            try:
                role = request.user.profile.role
            except:
                return redirect('login')
            if role not in roles and role != 'admin':
                messages.error(request, "Accès refusé. Vous n'avez pas les permissions.")
                return redirect('dashboard')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator