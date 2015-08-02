If you want to follow development or get involved, check out [this thread](http://forum.xbmc.org/showthread.php?t=90315) and the [Github Development Repositories](https://github.com/icefilms-xbmc).

# v1.1.0 #
Planned features, maybe a bit ambitious. Progress noted in brackets.
  * TVShow, Seasons and Episode metadata support. + tv meta in metadata container. (in progress, but 95% done thanks to westcoast13)
  * Displaying backdrops support, + backdrops contained in metadata container.
  * auto-view selection - make it look nice for skins by default (done)
there are more cool features also, but you'll have to check the changelog when it is released.

## To Do for Future Releases ##
  * megavid support
  * special handling for multi part files (queues parts, treats multi-part files as a video playlist)
  * 2shared

**NOTE:** I had previously thought that [this patch](http://trac.xbmc.org/ticket/10779) would provide a universal xbmc streaming cache.
This is not the case. I have since been told that video cache implementation in python _is_ possible through use of a http server.
BUT Tiben20 has started an awesome xbmc patch to enable in core a solution to the problems. when its completed it will also allow streaming and downloading simultaneously. we are hoping it will get accepted into xbmc nightly builds.

**Release Guide**
  * X.0.0 - Addon overhaul releases. Substantial overhaul of code or the introduction of a plethora of new features.
  * 0.X.0 - These releases are major added features that build upon the current code.
  * 0.0.X - Incremental releases. Usually bug-fixes or minor added features.