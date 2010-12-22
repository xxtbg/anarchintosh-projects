#!/usr/bin/python

#Icefilms.info v0.5 - anarchintosh 20/12/2010
# very convoluted code.
import sys,os
import urllib,urllib2,re,mechanize,cookielib,html2text
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,StringIO
from BeautifulSoup import BeautifulSoup

def xbmcpath(path,filename):
     translatedpath = os.path.join(xbmc.translatePath( path ), ''+filename+'')
     return translatedpath

       
def Notify(type,title,message,time):
     if type == 'small':
          xbmc.executebuiltin("XBMC.Notification("+title+","+message+","+time+",aas)")
     if type == 'big':
          dialog = xbmcgui.Dialog()
          dialog.ok(' '+title+' ', ' '+message+' ')

icepath = 'plugin://plugin.video.icefilms/'
icedatapath = 'special://profile/addon_data/plugin.video.icefilms'
art = icepath+'resources/art/'
megacookie = xbmcpath(icedatapath,'cookies.lwp')
loginfile = xbmcpath(icedatapath,'login')
premiumfile = xbmcpath(icedatapath,'premium')

homepagey = xbmcpath(art,'homepage.png')
moviesy = xbmcpath(art,'movies.png')
musicy = xbmcpath(art,'music.png')
tvshowsy = xbmcpath(art,'tvshows.png')
othery = xbmcpath(art,'other.png')
searchy = xbmcpath(art,'search.png')
standupy = xbmcpath(art,'standup.png')




#get settings
selfAddon = xbmcaddon.Addon(id='plugin.video.icefilms')
FlattenSrcType = selfAddon.getSetting('flatten-source-type')
FlattenMega = selfAddon.getSetting('flatten-megaupload')
HideHomepage = selfAddon.getSetting('hide-homepage')
AccountType = selfAddon.getSetting('account')
if AccountType == '2':
        megauser = selfAddon.getSetting('freeuser')
        megapass = selfAddon.getSetting('freepass')
        HideSuccessfulLogin = selfAddon.getSetting('hide-successful-free-login-messages')

if AccountType == '1':
        megauser = selfAddon.getSetting('premiumuser')
        megapass = selfAddon.getSetting('premiumpass')
        HideSuccessfulLogin = selfAddon.getSetting('hide-successful-premium-login-messages')

#hardcode DisableAtoZ to false to avoid overloading iceservers
DisableAtoZ = 'false'

#useful global strings:
iceurl = 'http://www.icefilms.info/'



def openfile(filename):
     fh = open(filename, 'r')
     contents=fh.read()
     fh.close()
     return contents

def save(filename, contents):  
     fh = open(filename, 'w')
     fh.write(contents)  
     fh.close()
     
#check for megaupload login and do it
def DoLogin():
        if AccountType == '0':
                login = 'none'
                save(loginfile,login)
        if AccountType == '1' or AccountType == '2':
                # Browser
                br = mechanize.Browser()

                # Cookie Jar
                cj = cookielib.LWPCookieJar()
                br.set_cookiejar(cj)

                # Browser options
                br.set_handle_equiv(True)
                br.set_handle_gzip(True)
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_robots(False)

                # Follows refresh 0 but not hangs on refresh > 0
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

                # User-Agent
                br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

                # The site we will navigate into, handling it's session
                br.open('http://www.megaupload.com/?c=login')

                # Select the first (index zero) form
                br.select_form('loginfrm')

                #User credentials
                br.form['username'] = megauser
                br.form['password'] = megapass
                br.submit()
                #checks if login worked
                loginerror="Username and password do not match" in br.response().read()
                cj.save(megacookie)
                if loginerror == True:
                        login = 'none'
                        save(loginfile,login)
                        print 'login failed'
                        Notify('big','Megaupload','Login failed. Megaupload will load with no account.','')
                elif loginerror == False:
                        print 'login succeeded'
                        if AccountType == '2':
                                login = 'free'
                                save(loginfile,login)
                                if HideSuccessfulLogin == 'false':
                                        Notify('small','Megaupload', 'Free-user login successful.','6000')
                        elif AccountType == '1':
                                login = 'premium'
                                save(loginfile,login)
                                if HideSuccessfulLogin == 'false':
                                        Notify('small','Megaupload', 'Premium login successful.','6000')
                                
                                


def CATEGORIES():
        DoLogin()
        if HideHomepage == 'false':
                addDir('Homepage',iceurl+'index',56,homepagey)
        addDir('TV Shows',iceurl+'tv/a-z/1',50,tvshowsy)
        addDir('Movies',iceurl+'movies/a-z/1',51,moviesy)
        addDir('Music',iceurl+'music/a-z/1',52,musicy)
        addDir('Stand Up Comedy',iceurl+'standup/a-z/1',53,standupy)
        addDir('Other',iceurl+'other/a-z/1',54,othery)
        addDir('Search',iceurl,55,searchy)

def ICEHOMEPAGE(url):
        addDir('Recently Added',iceurl+'index',60,'')
        addDir('Latest Releases',iceurl+'index',61,'')
        addDir('Being Watched Now',iceurl+'index',62,'')

def RECENT(url):
        link=GetURL(url)
        homepage=re.compile('<h1>Recently Added</h1>(.+?)<h1>Statistics</h1>').findall(link)
        for scrape in homepage:
                scrape='<h1>Recently Added</h1>'+scrape+'<h1>Statistics</h1>'
                recadd=re.compile('<h1>Recently Added</h1>(.+?)<h1>Latest Releases</h1>').findall(scrape)
                for scraped in recadd:
                        mirlinks=re.compile('<a href=(.+?)>(.+?)</a>').findall(scraped)
                        for url,name in mirlinks:
                                url='http://www.icefilms.info'+url
                                name=CLEANUP(name)
                                addDir(name,url,100,'')
    
def LATEST(url):
        link=GetURL(url)
        homepage=re.compile('<h1>Recently Added</h1>(.+?)<h1>Statistics</h1>').findall(link)
        for scrape in homepage:
                scrape='<h1>Recently Added</h1>'+scrape+'<h1>Statistics</h1>'
                latrel=re.compile('<h1>Latest Releases</h1>(.+?)<h1>Being Watched Now</h1>').findall(scrape)
                for scraped in latrel:
                        mirlinks=re.compile('<a href=(.+?)>(.+?)</a>').findall(scraped)
                        for url,name in mirlinks:
                                url='http://www.icefilms.info'+url
                                name=CLEANUP(name)
                                addDir(name,url,100,'')

def WATCHINGNOW(url):
        link=GetURL(url)
        homepage=re.compile('<h1>Recently Added</h1>(.+?)<h1>Statistics</h1>').findall(link)
        for scrape in homepage:
                scrapy='<h1>Recently Added</h1>'+scrape+'<h1>Statistics</h1>'
                watnow=re.compile('<h1>Being Watched Now</h1>(.+?)<h1>Statistics</h1>').findall(scrapy)
                for scraped in watnow:
                        mirlinks=re.compile('href=(.+?)>(.+?)</a>').findall(scraped)
                        for url,name in mirlinks:
                                url='http://www.icefilms.info'+url
                                name=CLEANUP(name)
                                addDir(name,url,100,'')        

def SEARCH(url):
        kb = xbmc.Keyboard('', 'Search Icefilms.info', False)
        kb.doModal()
        if (kb.isConfirmed()):
                search = kb.getText()
                search=re.sub(' ','+',search)
                nurl='http://www.google.co.uk/search?q='+search+'+site%3Ahttp%3A%2F%2Fwww.icefilms.info&hl=en&num=10&lr=&ft=i&cr=&safe=images&tbs='
                link=GetURL(nurl)
                match=re.compile('<h3 class="r"><a href="http://www.icefilms.info/(.+?)".+?">(.+?)</h3><button class=vspib>').findall(link)
                outputone = StringIO.StringIO()
                outputone.write(match)
                result = outputone.getvalue()
                if len(result) >3 and search is not '':
                        EPLIST(match[0])
                        EPLIST(match[1])
                        EPLIST(match[2])
                        EPLIST(match[3])
                        EPLIST(match[4])
                        EPLIST(match[5])
                        EPLIST(match[6])
                        EPLIST(match[7])
                        EPLIST(match[8])
                        EPLIST(match[9])
                
def EPLIST(setmatch):
        outputone = StringIO.StringIO()
        outputone.write(setmatch)
        setmatch = outputone.getvalue()
        checkforep=re.search('Episode List',setmatch)
        if checkforep is not None:
            split=re.compile("'(.+?)', '(.+?)'").findall(setmatch)
            for url,name in split:
                url=re.sub('&amp;','',url)
                surl=iceurl+url
                name=CLEANSEARCH(name)
                addDir(name,surl,12,'')
        checkforep2=re.search('Episode  List',setmatch)
        if checkforep2 is not None:
            split=re.compile("'(.+?)', '(.+?)'").findall(setmatch)
            for url,name in split:
                url=re.sub('&amp;','',url)
                surl=iceurl+url
                name=CLEANSEARCH(name)
                addDir(name,surl,12,'')
        if checkforep is None and checkforep2 is None:
            split=re.compile("'(.+?)', '(.+?)'").findall(setmatch)
            for url,name in split:
                url=re.sub('&amp;','',url)
                surl=iceurl+url
                name=CLEANSEARCH(name)
                addDir(name,surl,100,'')

def CLEANSEARCH(name):        
        name=re.sub('<em>','',name)
        name=re.sub('</em>','',name)
        name=re.sub('DivX - icefilms.info','',name)
        name=re.sub('</a>','',name)
        name=re.sub('<b>...</b>','',name)
        name=re.sub('- icefilms.info','',name)
        name=re.sub('DivX','',name)
        name=re.sub('&#39;',"'",name)
        name=re.sub('&amp;','&',name)
        name=re.sub('-  Episode  List','- Episode List',name)
        return name

def TVCATEGORIES(url):
        caturl = iceurl+'tv/'        
        setmode = '11'
        if DisableAtoZ == 'false':
                addDir('A-Z Directories',caturl+'a-z/1',10,'')
        if DisableAtoZ == 'true':
                addDir('A-Z List',caturl+'a-z/',13,'')                
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def MOVIECATEGORIES(url):
        caturl = iceurl+'movies/'        
        setmode = '2'
        if DisableAtoZ == 'false':
                addDir('A-Z Directories',caturl+'a-z/1',1,'')
        if DisableAtoZ == 'true':
                addDir('A-Z List',caturl+'a-z/',3,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def MUSICCATEGORIES(url):
        caturl = iceurl+'music/'        
        setmode = '2'
        addDir('A-Z List',caturl+'a-z/1',setmode,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def STANDUPCATEGORIES(url):
        caturl = iceurl+'standup/'        
        setmode = '2'
        addDir('A-Z List',caturl+'a-z/1',setmode,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def OTHERCATEGORIES(url):
        caturl = iceurl+'other/'        
        setmode = '2'
        addDir('A-Z List',caturl+'a-z/1',setmode,'')
        addDir('Popular',caturl+'popular/1',setmode,'')
        addDir('Highly Rated',caturl+'rating/1',setmode,'')
        addDir('Latest Releases',caturl+'release/1',setmode,'')
        addDir('Recently Added',caturl+'added/1',setmode,'')

def MOVIEA2ZList(url):
        MOVIEINDEX(url+'1')
        MOVIEINDEX(url+'A')
        MOVIEINDEX(url+'B')
        MOVIEINDEX(url+'C')
        MOVIEINDEX(url+'D')
        MOVIEINDEX(url+'E')
        MOVIEINDEX(url+'F')
        MOVIEINDEX(url+'G')
        MOVIEINDEX(url+'H')
        MOVIEINDEX(url+'I')
        MOVIEINDEX(url+'J')
        MOVIEINDEX(url+'K')
        MOVIEINDEX(url+'L')
        MOVIEINDEX(url+'M')
        MOVIEINDEX(url+'N')
        MOVIEINDEX(url+'O')
        MOVIEINDEX(url+'P')
        MOVIEINDEX(url+'Q')
        MOVIEINDEX(url+'R')
        MOVIEINDEX(url+'S')
        MOVIEINDEX(url+'T')
        MOVIEINDEX(url+'U')
        MOVIEINDEX(url+'V')
        MOVIEINDEX(url+'W')
        MOVIEINDEX(url+'X')
        MOVIEINDEX(url+'Y')
        MOVIEINDEX(url+'Z')
        
        
def TVA2ZList(url):
        TVINDEX(url+'1')
        TVINDEX(url+'A')
        TVINDEX(url+'B')
        TVINDEX(url+'C')
        TVINDEX(url+'D')
        TVINDEX(url+'E')
        TVINDEX(url+'F')
        TVINDEX(url+'G')
        TVINDEX(url+'H')
        TVINDEX(url+'I')
        TVINDEX(url+'J')
        TVINDEX(url+'K')
        TVINDEX(url+'L')
        TVINDEX(url+'M')
        TVINDEX(url+'N')
        TVINDEX(url+'O')
        TVINDEX(url+'P')
        TVINDEX(url+'Q')
        TVINDEX(url+'R')
        TVINDEX(url+'S')
        TVINDEX(url+'T')
        TVINDEX(url+'U')
        TVINDEX(url+'V')
        TVINDEX(url+'W')
        TVINDEX(url+'X')
        TVINDEX(url+'Y')
        TVINDEX(url+'Z')

        
def MOVIEA2ZDirectories(url):
        setmode = '2'
        caturl = iceurl+'movies/a-z/'
        addDir ('#1234',caturl+'1',setmode,'')
        addDir ('A',caturl+'A',setmode,'')
        addDir ('B',caturl+'B',setmode,'')
        addDir ('C',caturl+'C',setmode,'')
        addDir ('D',caturl+'D',setmode,'')
        addDir ('E',caturl+'E',setmode,'')
        addDir ('F',caturl+'F',setmode,'')
        addDir ('G',caturl+'G',setmode,'')
        addDir ('H',caturl+'H',setmode,'')
        addDir ('I',caturl+'I',setmode,'')
        addDir ('J',caturl+'J',setmode,'')
        addDir ('K',caturl+'K',setmode,'')
        addDir ('L',caturl+'L',setmode,'')
        addDir ('M',caturl+'M',setmode,'')
        addDir ('N',caturl+'N',setmode,'')
        addDir ('O',caturl+'O',setmode,'')
        addDir ('P',caturl+'P',setmode,'')
        addDir ('Q',caturl+'Q',setmode,'')
        addDir ('R',caturl+'R',setmode,'')
        addDir ('S',caturl+'S',setmode,'')
        addDir ('T',caturl+'T',setmode,'')
        addDir ('U',caturl+'U',setmode,'')
        addDir ('V',caturl+'V',setmode,'')
        addDir ('W',caturl+'W',setmode,'')
        addDir ('X',caturl+'X',setmode,'')
        addDir ('Y',caturl+'Y',setmode,'')
        addDir ('Z',caturl+'Z',setmode,'')



def TVA2ZDirectories(url):
        setmode = '11'
        caturl = iceurl+'tv/a-z/'
        addDir ('#1234',caturl+'1',setmode,'')
        addDir ('A',caturl+'A',setmode,'')
        addDir ('B',caturl+'B',setmode,'')
        addDir ('C',caturl+'C',setmode,'')
        addDir ('D',caturl+'D',setmode,'')
        addDir ('E',caturl+'E',setmode,'')
        addDir ('F',caturl+'F',setmode,'')
        addDir ('G',caturl+'G',setmode,'')
        addDir ('H',caturl+'H',setmode,'')
        addDir ('I',caturl+'I',setmode,'')
        addDir ('J',caturl+'J',setmode,'')
        addDir ('K',caturl+'K',setmode,'')
        addDir ('L',caturl+'L',setmode,'')
        addDir ('M',caturl+'M',setmode,'')
        addDir ('N',caturl+'N',setmode,'')
        addDir ('O',caturl+'O',setmode,'')
        addDir ('P',caturl+'P',setmode,'')
        addDir ('Q',caturl+'Q',setmode,'')
        addDir ('R',caturl+'R',setmode,'')
        addDir ('S',caturl+'S',setmode,'')
        addDir ('T',caturl+'T',setmode,'')
        addDir ('U',caturl+'U',setmode,'')
        addDir ('V',caturl+'V',setmode,'')
        addDir ('W',caturl+'W',setmode,'')
        addDir ('X',caturl+'X',setmode,'')
        addDir ('Y',caturl+'Y',setmode,'')
        addDir ('Z',caturl+'Z',setmode,'')      

def CLEANUP(name):
# clean names of annoying garbled text
                name=re.sub('&#xC6;','AE',name)
                name=re.sub('&#x27;',"'",name)
                name=re.sub('&#xED;','i',name)
                name=re.sub('&frac12;',' 1/2',name)
                name=re.sub('&#xBD;',' 1/2',name)
                name=re.sub('&#x26;','&',name)
                name=re.sub('&#x22;','',name)
                name=re.sub('</a>','',name)
                name=re.sub('<b>HD</b>',' *HD 720p*',name)
                name=re.sub('&#xF4;','o',name)
                name=re.sub('&#xE9;',"e",name)
                name=re.sub('&#xEB;',"e",name)
                return name

def MOVIEINDEX(url):
        link=GetURL(url)
# below is the original scraper that ignores HD tags.
#        match=re.compile('<img class=star><a href=/(.+?)>(.+?)</a>').findall(link)
        match=re.compile('<img class=star><a href=/(.+?)>(.+?)<br>').findall(link)
        for url,name in match:
                name=CLEANUP(name)
                addDir(name,iceurl+url,100,'')

def TVINDEX(url):
        link=GetURL(url)
        match=re.compile('<img class=star><a href=/(.+?)>(.+?)</a>').findall(link)
        for url,name in match:
                name=CLEANUP(name)
                addDir(name,iceurl+url,12,'')

def TVEPISODES(url):
# displays all episodes, with no unnecessary sub-directories for seasons. (this means it works even for 'the daily show with jon stewart' etc...)
        link=GetURL(url)
        match=re.compile('<img class=star><a href=/(.+?)>(.+?)</a>').findall(link)
        for url,name in match:
                name=CLEANUP(name)
                addDir(name,iceurl+url,100,'')
                
def LOADMIRRORS(url):
# This proceeds from the file page to the separate frame where the mirrors can be found,
# then executes code to scrape the mirrors
        link=GetURL(url)
        match=re.compile('/membersonly/components/com_iceplayer/(.+?)" width=').findall(link)
        match[0]=re.sub('%29',')',match[0])
        match[0]=re.sub('%28','(',match[0])
        for url in match:
            mirrorpageurl = iceurl+'membersonly/components/com_iceplayer/'+url
        GETMIRRORS(mirrorpageurl)

def GETMIRRORS(url):
# This scrapes the megaupload mirrors from the separate url used for the video frame.
# It also displays them in an informative fashion to user.
# Displays in three directory levels: HD or DVDRip, Source, PART
        link=GetURL(url)
#old scrape all mega links code
#        mulink=re.compile('http://www.megaupload.com/(.+?)>').findall(link)
#        for url in mulink:
#                fullmulink = 'http://www.megaupload.com/'+url
#                addDir(fullmulink,fullmulink,110,'')

        #strings for checking the existence of categories
        dvdrip=re.compile('<div class=ripdiv><b>DVDRip / (.+?)</b>').findall(link)
        hd720p=re.compile('<div class=ripdiv><b>HD (.+?)</b>').findall(link)
        dvdscreener=re.compile('<div class=ripdiv><b>DVD Sc(.+?)</b>').findall(link)
        r5r6=re.compile('<div class=ripdiv><b>R5/(.+?) DVDRip</b>').findall(link)

        #hacky buffers
        outputone = StringIO.StringIO()
        outputone.write(dvdrip)
        dvdrip = outputone.getvalue()

        outputone = StringIO.StringIO()
        outputone.write(hd720p)
        hd720p = outputone.getvalue()

        outputone = StringIO.StringIO()
        outputone.write(dvdscreener)
        dvdscreener = outputone.getvalue()

        outputone = StringIO.StringIO()
        outputone.write(r5r6)
        r5r6 = outputone.getvalue()

        #check that these categories exist, if they do set values to true.
        if len(dvdrip) >3:
                dvdrip = 'true'
        if len(hd720p) >3:
                hd720p = 'true'
        if len(dvdscreener) >3:
                dvdscreener = 'true'
        if len(r5r6) >1:
                r5r6 = 'true'
        #check that these categories exist, if they dont set values to false.
        if len(dvdrip) <1:
                dvdrip = 'false'
        if len(hd720p) <1:
                hd720p = 'false'
        if len(dvdscreener) <1:
                dvdscreener = 'false'
        if len(r5r6) <1:
             r5r6 = 'false'
             
        #only detect and proceed directly to adding sources if flatten sources setting is true
        if FlattenSrcType == 'true':
                #check if there is more than one directory
                if dvdrip == 'true' and hd720p == 'true':
                        only1 = 'false'
                if dvdrip == 'true' and dvdscreener == 'true':
                        only1 = 'false'
                if dvdrip == 'true' and r5r6 == 'true':
                        only1 = 'false'
                if dvdscreener == 'false' and r5r6 == 'false':
                        only1 = 'false'
                if hd720p == 'true' and dvdscreener == 'false':
                        only1 = 'false'
                if r5r6 == 'true' and hd720p == 'true':
                        only1 = 'false'
                #check if there is only one directory      
                if dvdrip == 'true' and hd720p == 'false' and dvdscreener == 'false' and r5r6 == 'false':
                        only1 = 'true'
                        DVDRip(url)
                if dvdrip == 'false' and hd720p == 'true' and dvdscreener == 'false' and r5r6 == 'false':
                        only1 = 'true'
                        HD720p(url)
                if dvdrip == 'false' and hd720p == 'false' and dvdscreener == 'true' and r5r6 == 'false':
                        only1 = 'true'
                        DVDScreener(url)
                if dvdrip == 'false' and hd720p == 'false' and dvdscreener == 'false' and r5r6 == 'true':
                        only1 = 'true'
                        R5R6(url)
                #add directories of source categories if only1 is false
                if only1 == 'false':
                        addCatDir(url,dvdrip,hd720p,dvdscreener,r5r6)
        #if flattensources is set to false, don't flatten                
        if FlattenSrcType == 'false':
                addCatDir(url,dvdrip,hd720p,dvdscreener,r5r6)     


                
def addCatDir(url,dvdrip,hd720p,dvdscreener,r5r6):
        if dvdrip == 'true':
                addDir('DVDRip',url,101,'')
        if hd720p == 'true':
                addDir('HD 720p',url,102,'')
        if dvdscreener == 'true':
                addDir('DVD Screener',url,103,'')
        if r5r6 == 'true':
                addDir('R5/R6 DVDRip',url,104,'') 
        
def PART(scrap,sourcenumber):
        #check for sources containing multiple parts
        source=re.compile('<p>Source #'+sourcenumber+': (.+?)PART 1(.+?)</i><p>').findall(scrap)
        for sourcescrape1,sourcescrape2 in source:
                sourcescrape=sourcescrape1+'PART 1'+sourcescrape2
                part=re.compile('&url=http://www.megaupload.com/?(.+?)>PART (.+?)</a>').findall(sourcescrape)
                for murl,name in part:
                        megaurl='http://www.megaupload.com/'+murl
                        partname='PART '+name
                        fullname='Source #'+sourcenumber+' | ['+partname+']'
                        VIDLINK(fullname,megaurl)
        outputone = StringIO.StringIO()
        outputone.write(source)
        source10 = outputone.getvalue()

        #if scraper for multiple parts returns nothing....
        if len(source10) <5:
                #check if source exists
                source3=re.compile('Source #'+sourcenumber+': ').findall(scrap)
                outputone = StringIO.StringIO()
                outputone.write(source3)
                source11 = outputone.getvalue()
                if len(source11) >0:
                        #find corresponding '<a rel=?' entry and add as a one-link source
                        source5=re.compile('<a rel='+sourcenumber+'.+?&url=(.+?)>Source #'+sourcenumber+':').findall(scrap)
                        for url in source5:
                                fullname='Source #'+sourcenumber+' | [Full]'
                                VIDLINK(fullname,url)


def SOURCE(scrape):
#check for sources containing multiple parts or just one part
        PART(scrape,'1')
        PART(scrape,'2')
        PART(scrape,'3')
        PART(scrape,'4')
        PART(scrape,'5')
        PART(scrape,'6')
        PART(scrape,'7')
        PART(scrape,'8')
        PART(scrape,'9')
        PART(scrape,'10')
        PART(scrape,'11')
        PART(scrape,'12')
        PART(scrape,'13')
        PART(scrape,'14')
        PART(scrape,'15')
        PART(scrape,'16')
                
def DVDRip(url):
        link=GetURL(url)
#string for all text under standard def border
        defcat=re.compile('<div class=ripdiv><b>DVDRip / Standard Def</b>(.+?)</div>').findall(link)
        for scrape in defcat:
                SOURCE(scrape)

def HD720p(url):
        link=GetURL(url)
#string for all text under hd720p border
        defcat=re.compile('<div class=ripdiv><b>HD 720p</b>(.+?)</div>').findall(link)
        for scrape in defcat:
                SOURCE(scrape)

def DVDScreener(url):
        link=GetURL(url)
#string for all text under dvd screener border
        defcat=re.compile('<div class=ripdiv><b>DVD Screener</b>(.+?)<p></div>').findall(link)
        for scrape in defcat:
                catdef = scrape+'<p></div>'
                SOURCE(catdef)

def R5R6(url):
        link=GetURL(url)
#string for all text under r5/r6 border
        defcat=re.compile('<div class=ripdiv><b>R5/R6 DVDRip</b>(.+?)<p></div>').findall(link)
        for scrape in defcat:
                catdef = scrape+'<p></div>'
                SOURCE(catdef)

def VIDEOLINKS(partname,url):
# loads megaupload page and scrapes and adds videolink, passes through partname.
        link=GetURL(url)
        avimatch=re.compile('id="downloadlink"><a href="(.+?).avi" class=').findall(link)
        for url in avimatch:
                fullurl=url+'.avi'                          
                addLink(partname,fullurl,'')
        #pretend to XBMC that divx is avi
        match1=re.compile('id="downloadlink"><a href="(.+?).divx" class=').findall(link)
        for surl in match1:
                sullurl=surl+'.avi'
                addLink(partname,sullurl,'')

def VIDEOLINKSWITHFILENAME(url):
# loads megaupload page and scrapes and adds videolink, and name of uploaded file from it
        link=GetURL(url)
        avimatch=re.compile('id="downloadlink"><a href="(.+?).avi" class=').findall(link)
        for url in avimatch:
                fullurl=url+'.avi'                          
                #get filname
                matchy=re.compile('id="downloadlink"><a href=".+?megaupload.com/files/.+?/(.+?).avi" class=').findall(link)
                for urlfilename in matchy:
                        addLink('VideoFile | '+urlfilename,fullurl,'')
        #pretend to XBMC that divx is avi
        match1=re.compile('id="downloadlink"><a href="(.+?).divx" class=').findall(link)
        for surl in match1:
                sullurl=surl+'.avi'
                #get filename
                matchy=re.compile('id="downloadlink"><a href=".+?megaupload.com/files/.+?/(.+?).divx" class=').findall(link)
                for urlfilename in matchy:
                        addLink('VideoFile | '+urlfilename,sullurl,'')
        
def GetURL(url):
        login=openfile(loginfile)
        print 'login is'+login
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')       
        if login == 'free' or login == 'premium':
                #load megaupload links with login cookie
                ismega = re.search('.megaupload.com/', url)
                if ismega is not 'None':
                         cj = cookielib.LWPCookieJar()
                         cooky=cj.load(megacookie)
                         print cooky
                         opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cooky))
                         response = opener.open(req)
                         link=response.read()
                         response.close()
                         return link
                if ismega is 'None':
                        response = urllib2.urlopen(req)
                        link=response.read()
                        response.close()
                        return link
        if login == 'none':
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                return link


def VIDLINK(name,url):
#video link preflight, pays attention to settings
        if FlattenMega == 'true':
                VIDEOLINKS(name,url)
        if FlattenMega == 'false':
                addDir(name,url,110,'')

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

elif mode==50:
        print ""+url
        TVCATEGORIES(url)

elif mode==51:
        print ""+url
        MOVIECATEGORIES(url)

elif mode==52:
        print ""+url
        MUSICCATEGORIES(url)

elif mode==53:
        print ""+url
        STANDUPCATEGORIES(url)

elif mode==54:
        print ""+url
        OTHERCATEGORIES(url)

elif mode==55:
        print ""+url
        SEARCH(url)

elif mode==56:
        print ""+url
        ICEHOMEPAGE(url)

elif mode==60:
        print ""+url
        RECENT(url)

elif mode==61:
        print ""+url
        LATEST(url)

elif mode==62:
        print ""+url
        WATCHINGNOW(url)

elif mode==1:
        print ""+url
        MOVIEA2ZDirectories(url)

elif mode==3:
        print ""+url
        MOVIEA2ZList(url)

elif mode==2:
        print ""+url
        MOVIEINDEX(url)
        
elif mode==10:
        print ""+url
        TVA2ZDirectories(url)

elif mode==13:
        print ""+url
        TVA2ZList(url)

elif mode==11:
        print ""+url
        TVINDEX(url)

elif mode==12:
        print ""+url
        TVEPISODES(url)

elif mode==100:
        print ""+url
        LOADMIRRORS(url)

elif mode==101:
        print ""+url
        DVDRip(url)

elif mode==102:
        print ""+url
        HD720p(url)

elif mode==103:
        print ""+url
        DVDScreener(url)

elif mode==104:
        print ""+url
        R5R6(url)

elif mode==110:
        print ""+url
        VIDEOLINKSWITHFILENAME(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
