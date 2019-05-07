import logging


class TrackAccessMiddleware:
    """This was created more like PoC don't get it too serious.
    
    Class gets users ip address from a request headers, and logs it to a access.log file.
    """
    
    
    LOGGER = logging.getLogger('access')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
        if ip:
            self.LOGGER.debug(ip)
        else:
            self.LOGGER.debug('anonymous')
        return self.get_response(request)