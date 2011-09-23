import urllib

from collective.dewplayer import interfaces
from collective.dewplayer.browser.base import BaseDewplayerView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class LinkView(BaseDewplayerView):
    """Special view for streaming link"""

    __call__ = ViewPageTemplateFile('dewplayer.pt')
    settings_schema = interfaces.IDewPlayerStreamingConfig

    def url(self):
        return self.context.getRemoteUrl()

    streming_url = url

    def audio_type(self):
        return 'streaming'

    def flashvars(self):
        settings = self.settings
#        del settings["player_version"]
        return urllib.urlencode(settings)

    @property
    def settings(self):
        settings = super(LinkView, self).settings
        settings['player_version'] = 'stream'
        settings['mp3'] = self.url()
        return settings

