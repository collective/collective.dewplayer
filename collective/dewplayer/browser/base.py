from zope import interface
from collective.configviews import ConfigurableBaseView
from collective.dewplayer import interfaces

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BaseDewplayerView(ConfigurableBaseView):
    """Base dewplayer view implementation. you must subclass this one"""

    interface.implements(interfaces.IDewplayerView)
    jsvarname = "dewplayer_flashvars"

    template = ViewPageTemplateFile('dewplayer.pt')

    def validate_content(self):
        raise NotImplementedError('you must implement this one')

    def player_size(self, version):
        if version == u"classic":
            width = 200
            height = 20
        elif version == 'mini':
            width = 160
            height = 20
        elif version == 'multi':
            width = 240
            height = 20
        elif version == 'playlist':
            width = 240
            height = 200
        elif version == 'playlist-cover':
            width = 240
            height = 500
        elif version == 'rect':
            width = 240
            height = 20
        elif version == 'bubble': 
            width = 250
            height = 65
        elif version == 'vinyl':
            width = 303
            height = 113
        elif version == 'vol':
            width = 240
            height = 20
        elif version == 'stream':
            width = 135
            height = 50
        else:
            width = 200
            height = 20
        return width, height

    def audio_type(self):
        raise NotImplementedError

    def width(self):
        version = self.settings['player_version']
        return self.player_size(version)[0]

    def height(self):
        version = self.settings['player_version']
        return self.player_size(version)[1]

    def player(self):
        version = self.settings['player_version']
        version = self.check_player(version)
        base = '++resource++collective.dewplayer/dewplayer-%s.swf'
        if version == u"classic":
            player = '++resource++collective.dewplayer/dewplayer.swf'
        else:
            player = base%version
        return player

    def check_player(self, version):
        audio_type = self.audio_type()
        if audio_type == 'file':
            if version in ('classic','mini','bubble', 'vol'):
                return version
            else:
                return 'classic'
        elif audio_type == 'streaming':
            return 'stream'
        elif audio_type == 'playlist':
            if version in ('multi','playlist', 'playslit_cover','rect','vinyl'):
                return version
            else:
                return 'multi'
        else:
            raise ValueError
