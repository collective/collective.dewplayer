from Products.Five import BrowserView

class File(BrowserView):
    """dewplayer browserview for File Plone content type"""
    
    def __init__(self, context, request):
        self.context = context
        self.request = request

    