from zope import schema
from zope import interface

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.i18nmessageid import MessageFactory
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
_ = MessageFactory("collective.dewplayer")

class IDewPlayerStreamingConfig(interface.Interface):
    
    autostart = schema.Bool(title=_(u"Auto start"),
                            default=True)
    
    volume = schema.Int(title=_(u"Volume"),
                        min=0, max=100,
                        default=100)
    
    autoreplay = schema.Bool(title=_(u"Auto replay"),
                             default=True)
        
    showtime = schema.Bool(title=_(u"Show time minutes:seconds"),
                           default=True)
    
    nopointer = schema.Bool(title=_(u"No pointer"),
                            default=True)

player_version_vocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'classic', title=_(u'Classic')),
     SimpleTerm(value=u'mini', title=_(u'Mini')),
     SimpleTerm(value=u'vol', title=_(u'Volume')),
     SimpleTerm(value=u'bubble', title=_(u'Buble'))]
    )

class IDewPlayerConfig(interface.Interface):
    
    player_version = schema.Choice(title=_(u"Version"),
                                   vocabulary=player_version_vocabulary,
                                   default=u"classic")
    
    autostart = schema.Bool(title=_(u"Auto start"),
                            default=True)
    
    volume = schema.Int(title=_(u"Volume"),
                        min=0, max=100,
                        default=100)
    
    autoreplay = schema.Bool(title=_(u"Auto replay"),
                             default=True)
        
    showtime = schema.Bool(title=_(u"Show time minutes:seconds"),
                           default=True)
    
    nopointer = schema.Bool(title=_(u"No pointer"),
                            default=True)


player_multi_version_vocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'multi', title=_(u'Multi')),
     SimpleTerm(value=u'rect', title=_(u'Multi rect')),
     SimpleTerm(value=u'playlist', title=_(u'Playlist')),
     SimpleTerm(value=u'playlist-cover', title=_(u'Playlist cover')),
     SimpleTerm(value=u'vinyl', title=_(u'Vinyl'))]
    )

class IDewPlayerMultiConfig(interface.Interface):
    
    player_version = schema.Choice(title=_(u"Version"),
                                   vocabulary=player_multi_version_vocabulary,
                                   default=u"multi")
    
    autostart = schema.Bool(title=_(u"Auto start"),
                            default=True)
    
    volume = schema.Int(title=_(u"Volume"),
                        min=0, max=100,
                        default=100)
    
    autoreplay = schema.Bool(title=_(u"Auto replay"),
                             default=True)
    
    randomplay = schema.Bool(title=_(u"Random play"),
                             default=True)
    
    showtime = schema.Bool(title=_(u"Show time minutes:seconds"),
                           default=True)
    
    nopointer = schema.Bool(title=_(u"No pointer"),
                            default=True)
    
    fading = schema.Int(title=_(u"Fading"),
                        default=3)

class IDewplayerView(interface.Interface):
    """common method a dewplayer view must implements"""
    
    def validate_content():
        """Return True or False depends if the content (the link, the file, ...)
        are valide according to current view"""
    
    def player():
        """Return the path from portal where to find the dewplayer"""
    
    def width():
        """Return the width the player should have"""
    
    def height():
        """Return the height the player should have"""