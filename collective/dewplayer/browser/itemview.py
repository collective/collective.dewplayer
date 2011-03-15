from Products.Five import BrowserView
from zope import component
from zope import interface
from collective.portlet.itemview import vocabulary

class GalleryPortletViewEntry(object):
    interface.implements(vocabulary.IPortletView)
    
    id = "itemview_portlet_dewplayer"
    name = u"Dewplayer"

class DewplayerPortletView(BrowserView):
    """View used by collective.portlet.itemview"""

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.portal_state = component.queryMultiAdapter((context, request),
                                                        name='plone_portal_state')

    @property
    def title(self):
        return self.context.Title()

    def flashvars_value(self):
        return "mp3=%s&amp;showtime=1"%self.context.absolute_url()
    
    def player_url(self):
        return self.portal_state.portal_url()+'/++resource++collective.dewplayer/dewplayer.swf'
