from collective.dewplayer.browser import topic
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class FolderView(topic.TopicView):
    pass

class FolderPlayList(topic.TopicPlayList):
    """Playlist view for folder"""

    def brains(self):
        return self.context.getFolderContents()
