from memes.models import Cookie
from django.contrib.sessions.models import Session
import requests

__all__ = ('store_consent', 'get_consent', 'get_session_object', 'get_memes')


def store_consent(session_obj, name, value):
    """
        store user consent value in Cookie model
    """
    Cookie.objects.create(session=session_obj, name=name, value=value)


def get_consent(session):
    """
        retrieve User Cookie consent value from Cookie model
    """
    cookie = session.session_cookies.filter(name='cookie-accepted').first()
    if cookie:
        return cookie.value
    return None


def get_session_object(session_key):
    """
        get session object
    """
    session = Session.objects.get(session_key=session_key)
    return session


def get_memes():
    """
        upto 5 memes in list format
    """
    url = 'https://api.imgflip.com/get_memes'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('data', {}).get('memes', [])[:5]
        return data
    else:
        return []
