Introduction
============

This collective module register a zope directory resource containing the
wonderful mp3 flash player Dewplayer, developed by alsacreation (http://www.alsacreations.fr/dewplayer-en).

Dewplayer version - downloaded 2009-12-08

Installation
------------

Add collective.dewplayer to your buildout as normal. See
http://plone.org/documentation/tutorial/buildout. Don't forget to load the
configure.zcml file.

At the moment this module doesn't add any feature to Plone. It is primary use as
resource package.

Usage
-----

Dewplayer offer several flash players included in the directory resource:

   * Mini (160x20) - dewplayer-mini.swf
   * Classic (200x20) - dewplayer.swf
   * Multi (240x20) - dewplayer-multi.swf
   * Playlist (240x200) - dewplayer-playlist.swf
   * Bubble (250x65) - dewplayer-bubble.swf

For example, to include a classic player (using dewplayer.swf) for http://mysite.com/myaudio.mp3 :

    <object type="application/x-shockwave-flash" data="++resource++collective.dewplayer/dewplayer.swf" width="200" height="20">
    <param name="wmode" value="transparent" />
    <param name="movie" value="dewplayer.swf" />
    <param name="flashvars" value="mp3=http://mysite.com/myaudio.mp3&amp;showtime=1" />
    </object>

See alsacreations.fr for full documentation: http://www.alsacreations.fr/dewplayer-en [english]
or http://www.alsacreations.fr/dewplayer [french]

Todo
----

   * Add some python helpers for the differents players.

