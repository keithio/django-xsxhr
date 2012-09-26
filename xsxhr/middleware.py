from django import http
from django.conf import settings

"""
Provides means for allowing Cross-site XmlHttpRequests.

``XS_XHR_ORIGINS``: domains allowed to access via cross-site XHR
``XS_XHR_METHODS``: methods that may be executed via XHR
``XS_XHR_ALLOWCT``: allow the specification of the Content-Type via XHR
"""

XS_XHR_ORIGINS = getattr(settings, 'XS_XHR_ORIGINS', [])  # Set to '*' for wildcard
XS_XHR_METHODS = getattr(settings, 'XS_XHR_METHODS',
    ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE'])
XS_XHR_ALLOWCT = getattr(settings, 'XS_XHR_ALLOWCT', True)


class XsXhrMiddleware(object):
    """
    This middleware allows cross-domain XmlHttpRquests using the HTML5
    postMessage API.

    More info: http://www.w3.org/TR/html5/comms.html.

    Based on code from https://gist.github.com/426829.
    """
    def process_request(self, request):
        """
        Adds the allowed options upon request.
        """
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = ' '.join(XS_XHR_ORIGINS)
            response['Access-Control-Allow-Methods'] = ','.join(XS_XHR_METHODS)
            if XS_XHR_ALLOWCT:
                response['Access-Control-Allow-Headers'] = 'Content-Type'
            return response
        return None

    def process_response(self, request, response):
        """
        Adds allowed headers upon response.
        """
        if not response.has_header('Access-Control-Allow-Origin'):
            response['Access-Control-Allow-Origin'] = ' '.join(XS_XHR_ORIGINS)
        if not response.has_header('Access-Control-Allow-Methods'):
            response['Access-Control-Allow-Methods'] = ','.join(XS_XHR_METHODS)
        return response