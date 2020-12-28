from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from memes.helper import store_consent, get_consent, get_session_object, get_memes


@login_required(login_url='/login')
def home_view(request):
    session_key = request.session.session_key
    session_obj = get_session_object(session_key)

    consent_value = get_consent(session_obj)

    if consent_value:
        response = render(request, template_name='memes/home.html', context={'memes': get_memes()})
        response.set_cookie('cookie-accepted', consent_value)

    elif request.COOKIES.get('cookie-accepted') == 'true':
        consent_value = request.COOKIES.get('cookie-accepted')
        response = render(request, template_name='memes/home.html', context={'memes': get_memes()})
        store_consent(session_obj, 'cookie-accepted', consent_value)
        response.set_cookie('cookie-accepted', consent_value)

    elif request.COOKIES.get('cookie-accepted') == 'false':
        response = render(request, template_name='memes/home.html', context={'memes': []})
        logout(request)
        # delete cookie
        response.delete_cookie('cookie-accepted')
        redirect(to='/login')

    else:
        response = render(request, template_name='memes/home.html', context={'memes': []})

    return response
