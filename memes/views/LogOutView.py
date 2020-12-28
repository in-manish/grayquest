from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    response = redirect(to='/login')
    response.delete_cookie('cookie-accepted')
    return response
