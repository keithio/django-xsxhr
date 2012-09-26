# django-xsxhr


Enables cross domain XmlHttpRequests.

## Usage

1. Add ``django-xsxhr`` to your Python path.

2. Edit your ``settings.py`` file to include the following line in your ``MIDDLEWARE_CLASSES``: 

    'xsxhr.middleware.XsXhrMiddleware',
    
## Reference

The following are specified anywhere in your ``settings.py``. If you have different settings for production and development use, you may specify accordingly.

``XS_XHR_ORIGINS``: domains allowed to access via cross-site XHR. Defaults to ``[]``.

``XS_XHR_METHODS``: methods that may be executed via XHR. Defaults to ``['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']``.

``XS_XHR_ALLOWCT``: allow the specification of the Content-Type via XHR. Defaults to ``True``.

###Usage:

    XS_XHR_ORIGINS = [
        'http://assets.mysite.com',
        'http://localhost:3000'  # Allows specification of ports
    ]
    
    XS_XHR_METHODS = ['GET', 'OPTIONS']  # Specifies read-only access
    
    XS_XHR_ALLOWCT = False  # Do not allow request to specify Content-Type header