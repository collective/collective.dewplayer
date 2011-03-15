Introduction
============

This module registers a zope directory resource containing the wonderful mp3 flash player Dewplayer,
developed by alsacreation (http://www.alsacreations.fr/dewplayer-en), and add a dewplayer view for File content type.

Dewplayer version - downloaded 2010-10-25
Tested with: : Plone 3, Plone 4.0

.. contents::

Credits
===============
|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com


Installation
============

Add collective.dewplayer to your buildout as normal. See
http://plone.org/documentation/tutorial/buildout. 

Install it throw the QuickInstaller to add a 'dewplayer' view to File content type.
This view let's you listen to any mp3 file and can be set as default with the display 
drop down menu.

Usage
=======

Dewplayer offer several flash players included in the directory resource:

   * Mini (160x20) - dewplayer-mini.swf
   * Classic (200x20) - dewplayer.swf
   * Multi (240x20) - dewplayer-multi.swf
   * Multi Rect (240x20) - dewplayer-rect.swf
   * Playlist (240x200) - dewplayer-playlist.swf
   * Bubble (250x65) - dewplayer-bubble.swf
   * Vinyl (303x113) - dewplayer-vinyl.swf

For example, to include a classic player (using dewplayer.swf) for http://mysite.com/myaudio.mp3 :

    <object type="application/x-shockwave-flash" data="++resource++collective.dewplayer/dewplayer.swf" width="200" height="20">
    <param name="wmode" value="transparent" />
    <param name="movie" value="dewplayer.swf" />
    <param name="flashvars" value="mp3=http://mysite.com/myaudio.mp3&amp;showtime=1" />
    </object>

See alsacreations.fr for full documentation: http://www.alsacreations.fr/dewplayer-en [english]
or http://www.alsacreations.fr/dewplayer [french]


Todo
=====

   * Add some python helpers for the differents players.

