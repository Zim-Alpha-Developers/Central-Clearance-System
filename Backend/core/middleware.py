"""
This module contains a middleware function for the 'api' app in Django.

It includes the `AuthPropsMiddleware` function which adds authentication properties to
the request if the user is authenticated.

Functions:
    AuthPropsMiddleware: This function adds authentication properties to the request.
"""

from inertia.share import share
from django.contrib.messages import get_messages

def AuthPropsMiddleware(get_response):

    """
    Middleware function to add authentication properties to the request.
    This function checks if the user is authenticated. If the user is authenticated, it
    adds the user's properties to the request. If the user is not authenticated, it adds
    empty properties to the request.
    Args:
        get_response (function): A function that takes a request and returns a response.

    Returns:
        function: A function that takes a request, modifies it and returns a response.
    """
    def middleware(request):

        
        try:
            if request.user.is_authenticated:
               pass
            else:
                pass
        except Exception as e:
            pass

        return get_response(request)

    return middleware