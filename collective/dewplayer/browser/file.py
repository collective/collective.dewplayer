import urllib

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.dewplayer import interfaces
from collective.dewplayer.browser import base

class FileView(base.BaseDewplayerView):
    """dewplayer browserview for File Plone content type"""


    __call__ = ViewPageTemplateFile('dewplayer.pt')
    settings_schema = interfaces.IDewPlayerConfig

    def validate_content(self):
        try:
            self.audio_type()
            return True
        except NotImplementedError:
            #TODO: add msg
            return False
    
    @property
    def settings(self):
        settings = super(FileView,self).settings
        audio_type = self.audio_type()
        if audio_type == 'file':
            settings["mp3"] = self.context.absolute_url()+'/at_download/file'
        elif audio_type == "playlist":
            settings["xml"] = 'dewplayer_playlist.xml'
        elif audio_type == 'streaming':
            settings['mp3'] = self.streaming_url()

        return settings

    def flashvars(self):
        settings = self.settings
#        del settings["player_version"]
        return urllib.urlencode(settings)

    def audio_type(self):
        file = self.context.getFile()
        filename = file.filename
        if filename.endswith('mp3'):
            return 'file'
        elif filename.endswith('pls'):
            data = file.data
            if type(data) is str:
                if data.startswith('playlist'):
                    if 'http://' in data:
                        return 'streaming'
            return 'playlist'
        elif filename.endswith('m3u'):
            return 'playlist'
        raise NotImplementedError

    def streaming_url(self):
        return ""


class FileMultiView(FileView):
    """Manage playlist file types"""

    settings_schema = interfaces.IDewPlayerMultiConfig

class FilePlaylist():
    """dewplayer_playlist.xml"""
    
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

    def files(self):
        data = self.context.getFile().data
        lines = data.split('\n')
#        for line in lines:
#            if Line.starts

class FileStreamingView(FileView):
    """Base view for *.pls files
    
    example of a pls content:
    [playlist]
    NumberOfEntries=16
    File1=http://scfire-ntc-aa04.stream.aol.com:80/stream/1025
    Title1=Electro House
    Length1=-1
    File2=http://scfire-mtc-aa06.stream.aol.com:80/stream/1025
    Title2=Electro House
    Length2=-1
    """

    settings_schema = interfaces.IDewPlayerConfig

    def audio_type(self):
        return 'streaming'

    @property
    def settings(self):
        settings = super(FileStreamingView,self).settings
        streaming_url = self.streaming_url()
        if streaming_url:
            settings['mp3'] = streaming_url
        settings['player_version'] = 'stream'
        return settings

    def streaming_url(self):
        data = self.context.getFile().data
        lines = data.split('\n')
        for line in lines:
            if 'http://' in line or 'https://' in line:
                return line.split('=')[-1]
