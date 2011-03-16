from Products.Five import BrowserView

class TopicPlayList(BrowserView):
    """dewplayer support playlist.xml"""
    
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

class FolderPlayList(TopicPlayList):
    """Playlist view for folder"""
    
    def brains(self):
        return self.context.getFolderContents()
