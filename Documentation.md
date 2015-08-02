

# Icefilms XBMC Add-on Help #

> ## Directories ##
_the following directories are referenced multiple times below, use them as appropriate_

**Repo**

Settings > Addons > Get Add-ons > anarchintosh addons

**Addon Settings**

Settings > Addons > Enabled Add-ons > Video Add-ons > Icefilms

# Technical #
_how to get the addon working_

> ## Installing the repo/addon ##
[Download the repository file zip](http://anarchintosh-projects.googlecode.com/files/repository.googlecode.anarchintosh-projects.1.0.1.zip)

Without extracting the file, move it into an easily findable location on your XBMC machine.

In XBMC, navigate to Settings > Addons > Install from zip file
Browse to the zipped repo and select it.
Repository installed!

Now you can install Icefilms.info from within XBMC, by navigating to the repo.

Notes:
  * 1.0.1 includes support for the 2nd generation Apple TV (ATV2).
  * For an Xbox version of the addon, refer to [tomatosoup's post](http://forum.xbmc.org/showthread.php?p=726286#post726286).

> ## Updating the repo/addon ##
Updates are pushed out via the repo. Users should be notified in XBMC when there are new updates.

If you know there is an update but the repo is listing an older version, you are most likely having an issue on your end.

To fix this, you have 2 options:
  1. Reinstall the add-on
  1. Reinstall the repo and addon (start over)


> ### Reinstalling the addon ###
Navigate to the addon settings. Select "Uninstall."
Navigate to the repo.
Hover over Anarchintosh Add-ons and bring up the context menu (press the "C" key on your keyboard). Select "Force Refresh."
Open the repo and reinstall Icefilms.

> ### Reinstalling the repo and addon ###
Uninstall the addon using the instructions above, go to your file system and delete the repo files and start over.


# Functionality #
_addon features_

> ## Context menu ##
The Icefilms addon takes advantage of the XBMC context menu feature. While in the addon, bring up the context menu by pressing the "C" key on your keyboard.

The context menu features include:
  * Download - Select this option to locally save a file for offline viewing (see below for additional instructions)
  * Check Mega Limits - this will inform you if you have reached the daily viewing limit allowed by Megauploads (see below for more Mega information)
  * Kill Streams - this will sever your current mega connections in an effort to  preserve your daily limit or to make streaming more efficient by cutting previously established streams

> ## Downloading files ##
Since version 1.0.0, you are now able to download files and store them locally for offline viewing. To set the download directory, navigate to the addon settings and click "Configure."

There will be 3 main tabs (Menus, Megaupload, and Downloads)
Go to the Downloads menu and set the Downloads Folder to the directory you want to store the files.

Note: Some skins will not display the Configure menu correctly (i.e., only showing the options of the first tab), use another skin for the correct functionality.

> ## Megaupload Premium ##
Although the free and member accounts are useable, premium has its benefits.
A few features include:
  * No 45 second wait time between streams
  * No download limit
  * Simultaneous downloads (especially good for homes with multiple boxes)

> ## Metadata ##

> ### Installation ###
When you first install the addon, you will be prompted to download the metadata container.
This file is a 230 mb zip that will serve as the source of the movie information and poster images. Metadata is not scraped via the normal routines as it would take forever each time you loaded the addon. It was designed this way as a system work around to long waits.

This feature is enabled by default, but can get disabled by navigating to the addon settings (Menus tab).

> ### Library Mode ###
To view the addon in its full meta'd glory, you must scan at least one item to your video library (XBMC limitation). Then enable Library mode.

Note: Metadata is currently only pulling the summary and poster for Movies. TV shows, fanart backdrops, and other information are planned to be included in a future release.

> ## Favourites ##
You are able to tag a movie as a favorite via the context menu and easily find it later from the home screen of the addon. The feature is not universal across platforms, each instance of the addon (separate machine) will have a unique list and is in no way associated with the favorites list from the Icefilms website.

> ## Icefilms Add-on Navigation ##
> _based on version 1.0.1_

> _see Known Bugs for branches notated with <sup>@</sup>_

| **TV Shows** | | | |
|:-------------|:|:|:|
|              | A-Z Directories | | |
|              | | #1234 | |
|              | | A | |
|              | | .. | |
|              | | Z | |
|              | Popular | | |
|              | Highly Rated | | |
|              | Latest Releases | | |
|              | Recently Added  | | |
|              | Genres | | |
|              | | Action | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Animation | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Comedy | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Documentary | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Drama | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Family | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Horror | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Romance | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Sci-Fi | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Thriller | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
| **Movies**   | | | |
|              | A-Z Directories | | |
|              | | #1234 | |
|              | | A | |
|              | | .. | |
|              | | Z | |
|              | HD 720p | | |
|              | | Popular | |
|              | | Highly Rated | |
|              | | Latest Releases | |
|              | | Recently Added | |
|              | Popular | | |
|              | Highly Rated | | |
|              | Latest Releases <sup>@</sup> | | |
|              | Recently Added <sup>@</sup>  | | |
|              | Genres | | |
|              | | Action | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Animation | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Comedy | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Documentary | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Drama | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Family | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Horror | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Romance | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Sci-Fi | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Thriller | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
| **Music**    | | | |
|              | A-Z List | | |
|              | Popular | | |
|              | Highly Rated | | |
|              | Latest Releases | | |
|              | Recently Added  | | |
|              | Genres | | |
|              | | Action | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Animation | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Comedy | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Documentary | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Drama | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Family | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Horror | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Romance | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Sci-Fi | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Thriller | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
| **Stand Up Comedy** | | | |
|              | A-Z List | | |
|              | Popular | | |
|              | Highly Rated | | |
|              | Latest Releases | | |
|              | Recently Added  | | |
|              | Genres | | |
|              | | Action | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Animation | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Comedy | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Documentary | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Drama | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Family | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Horror | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Romance | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Sci-Fi | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Thriller | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
| **Other**    | | | |
|              | A-Z List | | |
|              | Popular <sup>@</sup> | | |
|              | Highly Rated <sup>@</sup> | | |
|              | Latest Releases <sup>@</sup> | | |
|              | Recently Added <sup>@</sup>  | | |
|              | Genres | | |
|              | | Action | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Animation | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Comedy | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Documentary | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Drama | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Family | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Horror | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Romance | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Sci-Fi | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
|              | | Thriller | |
|              | | | Popular |
|              | | | Highly Rated |
|              | | | Latest Releases |
|              | | | Recently Added |
| **Homepage** | | | |
|              | Recently Added | | |
|              | Latest Releases | | |
|              | Being Watched Now | | |
| **Favourites** | | | |
| **Search**   | | | |


# Known Bugs #
_and workarounds_

  * A script error may prevent you from viewing certain subfolders (e.g., popular, recently added, etc.) - current fix is to go to Addon Settings and deselect Enable Metadata.
  * A script error may prevent you from viewing specific movie sources (e.g., Black Swan and King's Speech) - no workaround.
  * Certain files prompt you to enter a captcha - Entering the words in the image correctly will allow to continue as normal.
  * Buffering - XBMC has a limited cache. Kill streams or try other sources.
  * ATV2 720p stutter - Possibly a hardware issue when streaming; however, downloading the file locally and playing may work.