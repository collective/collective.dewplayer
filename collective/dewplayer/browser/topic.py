import urllib

from collective.dewplayer import interfaces
from collective.dewplayer.browser import base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

class TopicView(base.BaseDewplayerView):
    """Base topic view"""
    
    __call__ = ViewPageTemplateFile('dewplayer.pt')
    settings_schema = interfaces.IDewPlayerMultiConfig

    def audio_type(self):
        return 'playlist'

    def flashvars(self):
        settings = self.settings
#        del settings["player_version"]
        return urllib.urlencode(settings)

    @property
    def settings(self):
        settings = super(TopicView,self).settings
        settings["xml"] = 'dewplayer_playlist.xml'
        return settings

class TopicPlayList(BrowserView):
    """dewplayer support playlist.xml"""
    
    __call__ = ViewPageTemplateFile('playlist.pt')

    def title(self):
        return self.context.Title()
    
    def creator(self):
        return "creator"
    
    def info(self):
        return self.context.Description()
    
    def tracks(self):
        brains = self.brains()
        tracks = []
        for brain in brains:
            url = brain.getURL() 
            if url.endswith('.mp3'):
                tracks.append({'location':url,
                               'title':brain.Title,
                               'creator':"creator",
                               'info':brain.Description})
        return tracks

    def brains(self):
        return self.context.queryCatalog()
