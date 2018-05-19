# -*- coding: utf-8 -*-

import CBW
from CBW.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
#from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
#from gtts import gTTS
#from googletrans import Translator

wN1 = CBW.LINE()
#wN1.login(qr=True)
wN1.login(token="")#1 
wN1.loginResult()

wN2 = CBW.LINE()
#wN2.login(qr=True)
wN2.login(token="")#2 
wN2.loginResult()

wN3 = CBW.LINE()
#wN3.login(qr=True)
wN3.login(token="")#3 
wN3.loginResult()

wN4 = CBW.LINE()
#wN4.login(qr=True)
wN4.login(token="")#4 
wN4.loginResult()

wN5 = CBW.LINE()
#wN5.login(qr=True)
wN5.login(token="")#5
wN5.loginResult()

wN6 = CBW.LINE()
#wN6.login(qr=True)
wN6.login(token="")#6
wN6.loginResult()

wN7 = CBW.LINE()
#wN7.login(qr=True)
wN7.login(token="")#7
wN7.loginResult()

wN8 = CBW.LINE()
#wN8.login(qr=True)
wN8.login(token="")#8
wN8.loginResult()

wN9 = CBW.LINE()
#wN9.login(qr=True)
wN9.login(token="")#9
wN9.loginResult()

wN10 = CBW.LINE()
#wN10.login(qr=True)
wN10.login(token="")#10
wN10.loginResult()

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ CBW BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣facebook
║╠❂➣Youtube
║╠❂➣Yt
║╠❂➣Music
║╠❂➣google (text)
║╠❂➣playstore (text)
║╠❂➣instagram (username)
║╠❂➣wikipedia (text)
║╠❂➣image (text)
║╠❂➣lirik (text)
║╠❂➣Cipok
║╠❂➣Gcreator
║╠❂➣idline (text)
║╠❂➣time
║╠❂➣Salam1/Salam2
║╠❂➣Creator
║╠❂➣Kelahiran
║╠❂➣Kalender/waktu
║╠❂➣say
║╠❂➣Gift8
║╠❂➣Gift/Gift1/2/3
║╠❂➣reinvite
║╠❂➣time
║╠❂➣Kapan
║╠❂➣Apakah
║╠❂➣Nah
║╠❂➣Absen
║╠❂➣runtime
║╠❂➣speed
║╠❂➣keybot
║╚════════════
╚═════════════"""

keymsg ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣keypro
║╠❂➣keyself
║╠❂➣keygrup
║╠❂➣keyset
║╠❂➣keytran
║╠❂➣mode on/off
║╚════════════
╚═════════════"""

helppro ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣mode on/off
║╠❂➣protect on/off
║╠❂➣qr on/off
║╠❂➣invite on/off
║╠❂➣cancel on/off
║╚════════════
╚═════════════"""

helpself ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣cctv on/off (Lurking)
║╠❂➣intip/toong (Lurkers)
║╠❂➣Setimage: (link)
║╠❂➣Papimage
║╠❂➣Setvideo: (link)
║╠❂➣Papvideo
║╠❂➣mymid
║╠❂➣Getcover @
║╠❂➣Myname
║╠❂➣Mybot
║╠❂➣Mybio
║╠❂➣Mypict
║╠❂➣Myvid
║╠❂➣Urlpict
║╠❂➣Mycover
║╠❂➣Urlcover
║╠❂➣Getmid @
║╠❂➣Getinfo @
║╠❂➣Getbio @
║╠❂➣Getname @
║╠❂➣Getprofile @
║╠❂➣Getcontact @
║╠❂➣Getpict @
║╠❂➣Getvid @
║╠❂➣Picturl @
║╠❂➣Getcover @
║╠❂➣Coverurl @
║╠❂➣Mycopy @
║╠❂➣Mybackup
║╠❂➣Testext: (text)
║╠❂➣Spam change:
║╠❂➣Spam add:
║╠❂➣Spam:
║╠❂➣Spam (text)
║╠❂➣Steal contact
║╠❂➣Auto add
║╠❂➣Spam change:
║╠❂➣Spam add:
║╠❂➣Spam:
║╠❂➣spam txt/on/jml
║╠❂➣Micadd @
║╠❂➣Micdel @
║╠❂➣Miclist
║╠❂➣Mimic target @
║╠❂➣Mimic on/off
║╚════════════
╚═════════════"""

helpset ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣Gurl
║╠❂➣Grup cancel:
║╠❂➣share on/off
║╠❂➣Poto on/off
║╠❂➣Sambut on/off
║╠❂➣Pergi on/off
║╠❂➣Tag on/off
║╠❂➣Tag2 on/off
║╠❂➣contact on/off
║╠❂➣autojoin on/off
║╠❂➣autoleave on/off
║╠❂➣autoadd on/off
║╠❂➣like friend
║╠❂➣Like me
║╠❂➣link on/off
║╠❂➣simisimi on/off
║╠❂➣Autoread on/off
║╠❂➣update
║╠❂➣Pesan set:
║╠❂➣Coment Set:
║╠❂➣Comment on/off
║╠❂➣Comment
║╠❂➣Com hapus Bl
║╠❂➣Com Bl cek
║╠❂➣jam on/off
║╠❂➣Jam say:
║╚════════════
╚═════════════"""

helpgrup ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣Link on
║╠❂➣Url
║╠❂➣Cancel
║╠❂➣Gcreator
║╠❂➣Kick @
║╠❂➣Cium @
║╠❂➣Gname:
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
║╠❂➣Infogrup
║╠❂➣Gruplist
║╠❂➣Friendlist
║╠❂➣Blacklist
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Clearban
║╠❂➣Banlist
║╠❂➣Contact ban
║╠❂➣Midban
║╠❂➣Kick @
║╠❂➣Cium @
║╠❂➣cancel
║╠❂➣friendpp:
║╠❂➣Checkmid:
║╠❂➣Checkid:
║╠❂➣Friendlist
║╠❂➣Memlist
║╠❂➣Friendinfo:
║╠❂➣Friendpict:
║╠❂➣Friendlistmid
║╠❂➣Blocklist
║╠❂➣Gruplist
║╠❂➣Gruplistmid
║╠❂➣Grupimage:
║╠❂➣Grupname
║╠❂➣Grupid
║╠❂➣Grupinfo:
║╠❂➣Gcreator
║╠❂➣invite:gcreator
║╠❂➣Gname:
║╠❂➣infogrup
║╠❂➣grup id
║╠❂➣Glist
║╠❂➣gcancel
║╠❂➣Asup/. (manggil bot)
║╠❂➣Kabur all
║╠❂➣Kr bye
║╠❂➣cipok/crot (tagall)
║╠❂➣cctv on/off
║╠❂➣Toong/Intip
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
║╠❂➣Getgrup image
║╠❂➣Urlgrup image
║╠❂➣status
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Ban:
║╠❂➣Unban:
║╠❂➣Clear
║╠❂➣Ban:on
║╠❂➣Unban:on
║╠❂➣Banlist
║╠❂➣Conban/Contact ban
║╠❂➣Midban
║╠❂➣scan blacklist
║╠❂➣Bcast
║╚════════════
╚═════════════"""

helptranslate ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣Translate-id
║╠❂➣Translate-en
║╠❂➣Translate-ar
║╠❂➣Translate-jp
║╠❂➣Translate-ko
║╠❂➣Id@en
║╠❂➣En@id
║╠❂➣Id@jp
║╠❂➣Jp@id
║╠❂➣Id@th
║╠❂➣Th@id
║╠❂➣Id@ar
║╠❂➣Ar@id
║╠❂➣Id@ko
║╠❂➣Ko@id
║╠❂➣Say-id
║╠❂➣Say-en
║╠❂➣Say-jp
║╠❂➣Say-ar
║╠❂➣Say-ko
║╠❂➣welcome
║╚════════════
╚═════════════"""

helprhs ="""
╔═════════════
║ ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰
╠═════════════
║ Owner : CBW
║ line://ti/p/~CBWsthea
╠═════════════
║╔════════════
║╠❂➣Dadas
║╠❂➣ifconfig
║╠❂➣system
║╠❂➣kernel
║╠❂➣cpu
║╠❂➣Restart
║╠❂➣Turn off
║╠❂➣Speed
║╠❂➣crash
║╠❂➣crash kontak @
║╠❂➣Attack
║╠❂➣Spamcontact @
║╠❂➣Spamtag @
║╠❂➣Kibar
║╠❂➣Kr kemari
║╠❂➣cab/cab1/2/3/4/5/6/7
║╠❂➣Logo
║╠❂➣Restart
║╠❂➣Invite/Undang/Jepit
║╠❂➣Namebot:(txt)
║╠❂➣Namebot1/2/3/4/5: 
║╠❂➣Biobot: (txt)
║╠❂➣Gcreator:inv
║╠❂➣Gcreator:kick
║╠❂➣Kr spamtag @
║╠❂➣Kr cium 
║╠❂➣Kr glist
║╠❂➣Kr glist2
║╠❂➣Kr asupka
║╠❂➣Kr bye
║╠❂➣Kr megs 
║╠❂➣#megs 
║╠❂➣recover
║╠❂➣Kr spin
║╠❂➣Remove all chat
║╠❂➣Kr muach
║╠❂➣Salam3
║╚════════════
╚═════════════"""

KAC=[wN1,wN2,wN3,wN4,wN5,wN6,wN7,wN8,wN9,wN10]
mid1 = wN1.getProfile().mid
Amid = wN2.getProfile().mid
Bmid = wN3.getProfile().mid
Cmid = wN4.getProfile().mid
Dmid = wN5.getProfile().mid
Emid = wN6.getProfile().mid
Fmid = wN7.getProfile().mid
Gmid = wN8.getProfile().mid
Hmid = wN9.getProfile().mid
Imid = wN10.getProfile().mid
#midd1=["u4a0f653ea757da7abcd41c15bf0f15da"]
#midd2=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
#midd3=["uad6cb020c5ca7afbecb4681675eb38cd"]
#midd4=["ud5262649376cbf7576e2dcac0331d481"]
#midd5=["u53c352134325f0c49e86534c57801bd7"]
#midd6=["ua2ea9f4c32848bc67644c5267bb91279"]
#midd7=["uadfd3a23698b71d17c64482d27dc2ed1"]
#midd8=["u45c6ce403f0acc28392c519028aae154"]
#midd9=["udcf44c4272d8209a8a5f2dd1afeea93f"]
#midd10=["u4a0be979fc73e88ebfe915bc917237b8"]


Bots=[mid1,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1","u0e881fcbda6a0d82974a775f8015f4fe","ud3065a5bd9cf0d6961d9c046a124761c","u9d4b18194ce5b48d86fa27e5fac1d606","u60694eabf6ae04073739b4c95777d04a","uc70b2f7f85d13c96e0f28ded3b3b13d6",mid1,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]##CBWna,CBW,

wait = {
    'likeOn':False,
    'detectMention':True, 
    'potoMention':True,
    'kickMention':False,
    'steal':False,
    'pap':{},
    'invite':{},
    'invite2':{},
    'spam':{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    #'message':"""Thx for add\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆""",
    "lang":"JP",
    #"comment":"
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames1":"↝↬₡αβ↫↜",
    "cNames2":"↝↬₡αβ↫↜",
    "cNames3":"↝↬₡αβ↫↜",
    "cNames4":"↝↬₡αβ↫↜",
    "cNames5":"↝↬₡αβ↫↜",
    "Wc":False,
    "Wc2":False,
    "Lv":False,
    "autoKick":True,
    "winvite":False,
    "MENTION":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
    "QrProtect":True,#<====
    "MProtection":True,
    "Protectguest":True,
    "Protectcancel":True,
    "Protectgr":True,
    "pname":{},
    "pro_name":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = wN1.getProfile()
mybackup = wN1.getProfile()
contact = wN2.getProfile()
mybackup = wN2.getProfile()
contact = wN3.getProfile()
mybackup = wN3.getProfile()
contact = wN4.getProfile()
mybackup = wN4.getProfile()
contact = wN5.getProfile()
mybackup = wN5.getProfile()
contact = wN6.getProfile()
mybackup = wN6.getProfile()
contact = wN7.getProfile()
mybackup = wN7.getProfile()
contact = wN8.getProfile()
mybackup = wN8.getProfile()
contact = wN9.getProfile()
mybackup = wN9.getProfile()
contact = wN10.getProfile()
mybackup = wN10.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = wN1.getProfile()
backup = wN1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = wN1.getProfile()
profile = wN1.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items


def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = wN1.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.wN1.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = wN1.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.wN1.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
def sendAudioWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
         raise e

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._wN1.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True

def sendVideoWithURL(self, to_, url):
      path = 'pythonLines.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendVideo(to_, path)
      except Exception as e:
         raise e

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "► @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         wN1.sendMessage(msg)
    except Exception as error:
        print error
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={"MENTION":'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       wN1.sendMessage(msg)
    except Exception as error:
       print error

def removeAllMessages(self, lastMessageId):
     return self._wN1.removeAllMessages(0, lastMessageId)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
     
def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            return
           # if wait['autoAdd'] == True:
            #    wN1.findAndAddContactsByMid(op.param1)
            #    if (wait['message'] in [""," ","\n",None]):
            #        pass
            #    else:
            #        wN1.sendText(op.param1,str(wait['message']))
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        wN1.sendText(msg.to,text)
#==========================[CBW]===========================
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==========================[CBW]===========================
        if op.type == 13:
           if wait["Protectguest"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==========================[CBW]===========================
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
#==========================[CBW]===========================
        if op.type == 11:
            if wait["QrProtect"] == True:
                if op.param2 in admin and Bots:
                    pass
                if op.param2 not in admin:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
                    
        if op.type == 11:
            if wait["Protectgr"] == True:
                if random.choice(KAC).getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        try:
                            random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Woyyyyy...!!!")
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            X = random.choice(KAC).getGroup(op.param1)
                            X.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(X)
                        except:
                            random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Woyyyyy...!!!")
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            Z = random.choice(KAC).getGroup(op.param1)
                            Z.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(Z)
#==========================[CBW]===========================
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = wN1.getGroup(op.param1)
                    except:
                        try:
                            G = wN2.getGroup(op.param1)
                        except:
                            try:
                                G = wN3.getGroup(op.param1)
                            except:
                                try:
                                    G = wN4.getGroup(op.param1)
                                except:
                                    pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        wN1.updateGroup(G)
                    except:
                        try:
                            wN2.updateGroup(G)
                        except:
                            try:
                                wN3.updateGroup(G)
                            except:
                                try:
                                    wN4.updateGroup(G)
                                except:
                                    pass
                    if op.param2 in admin or Bots:
                        pass
                    else:
                        try:
                            wN1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                wN2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    wN3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        wN4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                                    wN1.sendText(op.param1,"please do not change group name-_-")
#==========================[CBW]===========================
        if op.type == 13:
            print op.param3
            if op.param3 in mid1:
                if op.param2 in owner:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in owner:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in owner:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in owner:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in owner:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in owner:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in owner:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in owner:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in owner:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in owner:
                    wN10.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in mid1:
                if op.param2 in Amid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Bmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Cmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Dmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Emid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Fmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Gmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Hmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Imid:
                    wN1.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Amid:
                if op.param2 in mid1:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Cmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Dmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Emid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Fmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Gmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Hmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Imid:
                    wN2.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Bmid:
                if op.param2 in mid1:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Amid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Dmid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Emid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Fmid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Gmid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Hmid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Imid:
                    wN3.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Cmid:
                if op.param2 in mid1:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Amid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Emid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Fmid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Gmid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Hmid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Imid:
                    wN4.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Dmid:
                if op.param2 in mid1:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Amid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Bmid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Emid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Fmid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Gmid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Hmid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Imid:
                    wN5.acceptGroupInvitation(op.param1)
#==========================[CBW]=========================== 
            if op.param3 in Emid:
                if op.param2 in mid1:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Amid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Bmid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Cmid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Fmid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Gmid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Hmid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Imid:
                    wN6.acceptGroupInvitation(op.param1)
#==========================[CBW]=========================== 
            if op.param3 in Fmid:
                if op.param2 in mid1:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Amid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Bmid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Cmid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Dmid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Gmid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Hmid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Imid:
                    wN7.acceptGroupInvitation(op.param1)
#==========================[CBW]=========================== 
            if op.param3 in Gmid:
                if op.param2 in mid1:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Amid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Bmid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Cmid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Dmid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Emid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Hmid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Imid:
                    wN8.acceptGroupInvitation(op.param1)
#==========================[CBW]=========================== 
            if op.param3 in Hmid:
                if op.param2 in mid1:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Amid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Bmid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Cmid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Dmid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Emid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Fmid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Imid:
                    wN9.acceptGroupInvitation(op.param1)
#==========================[CBW]=========================== 
            if op.param3 in Imid:
                if op.param2 in mid1:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Amid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Bmid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Cmid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Dmid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Emid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Fmid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Gmid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Hmid:
                    wN10.acceptGroupInvitation(op.param1)
#==========================[CBW]=========================== 
        if op.type == 13:
            if mid1 in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN1.acceptGroupInvitation(op.param1)
                    else:
                        wN1.acceptGroupInvitation(op.param1)
                        wN1.kickoutFromGroup(op.param1,[op.param2])
                        wN1.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Amid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN2.acceptGroupInvitation(op.param1)
                    else:
                        wN2.acceptGroupInvitation(op.param1)
                        wN2.kickoutFromGroup(op.param1,[op.param2])
                        wN2.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Bmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN3.acceptGroupInvitation(op.param1)
                    else:
                        wN3.acceptGroupInvitation(op.param1)
                        wN3.kickoutFromGroup(op.param1,[op.param2])
                        wN3.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Cmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN4.acceptGroupInvitation(op.param1)
                    else:
                        wN4.acceptGroupInvitation(op.param1)
                        wN4.kickoutFromGroup(op.param1,[op.param2])
                        wN4.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                
            if Dmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN5.acceptGroupInvitation(op.param1)
                    else:
                        wN5.acceptGroupInvitation(op.param1)
                        wN5.kickoutFromGroup(op.param1,[op.param2])
                        wN5.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Emid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN6.acceptGroupInvitation(op.param1)
                    else:
                        wN6.acceptGroupInvitation(op.param1)
                        wN6.kickoutFromGroup(op.param1,[op.param2])
                        wN6.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Fmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN7.acceptGroupInvitation(op.param1)
                    else:
                        wN7.acceptGroupInvitation(op.param1)
                        wN7.kickoutFromGroup(op.param1,[op.param2])
                        wN7.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Gmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN8.acceptGroupInvitation(op.param1)
                    else:
                        wN8.acceptGroupInvitation(op.param1)
                        wN8.kickoutFromGroup(op.param1,[op.param2])
                        wN8.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Hmid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN9.acceptGroupInvitation(op.param1)
                    else:
                        wN9.acceptGroupInvitation(op.param1)
                        wN9.kickoutFromGroup(op.param1,[op.param2])
                        wN9.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
                    
            if Imid in op.param3:
                if wait['autoJoin'] == True:
                    if op.param2 in Bots or owner:
                        wN10.acceptGroupInvitation(op.param1)
                    else:
                        wN10.acceptGroupInvitation(op.param1)
                        wN10.kickoutFromGroup(op.param1,[op.param2])
                        wN10.leaveGroup(op.param1)
                else:
                    print "autoJoin is Off"
#==========================[CBW]===========================
        if op.type == 19:
            if wait["autoKick"] == True:
                if op.param2 in admin or Bots:
                    pass
                else:
                    try:
                        wN3.kickoutFromGroup(op.param1,[op.param2])
                        wN8.kickoutFromGroup(op.param1,[op.param2])
                        wN1.inviteIntoGroup(op.param1,[op.param3])
                        wN5.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                if op.param2 in wait["blacklist"]:
                    pass
                else:
                    if op.param2 in admin or Bots:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#==========================[CBW]===========================
            if mid1 in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN2.kickoutFromGroup(op.param1,[op.param2])
                        wN3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN3.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN3.updateGroup(G)
                    Ti = wN3.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN1.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Amid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN3.kickoutFromGroup(op.param1,[op.param2])
                        wN4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN4.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN4.updateGroup(G)
                    Ti = wN4.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN2.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Bmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN4.kickoutFromGroup(op.param1,[op.param2])
                        wN5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN5.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN5.updateGroup(G)
                    Ti = wN5.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN3.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Cmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN5.kickoutFromGroup(op.param1,[op.param2])
                        wN6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN6.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN6.updateGroup(G)
                    Ti = wN6.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN4.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Dmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN6.kickoutFromGroup(op.param1,[op.param2])
                        wN7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN7.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN7.updateGroup(G)
                    Ti = wN7.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN5.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN5.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Emid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN7.kickoutFromGroup(op.param1,[op.param2])
                        wN8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN8.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN8.updateGroup(G)
                    Ti = wN8.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN6.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN6.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
            if Fmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN8.kickoutFromGroup(op.param1,[op.param2])
                        wN9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN9.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN9.updateGroup(G)
                    Ti = wN9.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN7.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN7.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Gmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN9.kickoutFromGroup(op.param1,[op.param2])
                        wN10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN10.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN10.updateGroup(G)
                    Ti = wN10.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN8.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN8.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Hmid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN10.kickoutFromGroup(op.param1,[op.param2])
                        wN1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN1.updateGroup(G)
                    Ti = wN1.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN9.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN9.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

            if Imid in op.param3:
                if op.param2 in Bots or admin:
                    pass
                else:
                    try:
                        wN1.kickoutFromGroup(op.param1,[op.param2])
                        wN2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                    G = wN2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    wN2.updateGroup(G)
                    Ti = wN2.reissueGroupTicket(op.param1)
                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN6.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN7.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN8.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN9.acceptGroupInvitationByTicket(op.param1,Ti)
                    wN10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = wN10.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN10.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

#==========================[CBW]===========================
        if op.type == 19:
            if op.param3 in admin:
                if op.param2 not in admin:
                    try:
                        wN3.kickoutFromGroup(op.param1,[op.param2])
                        wN1.inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True
                                
            if op.param3 not in admin:
                if op.param2 not in admin:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        
            if op.param3 in admin:
                if op.param2 in admin:
                    try:
                        wN1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

    #    if op.type == 19:
    #        if op.param3 in Bots:
    #            if op.param2 not in admin:
    #                try:
    #                    wN3.kickoutFromGroup(op.param1,[op.param2])
    #                    mid1=["u4a0f653ea757da7abcd41c15bf0f15da"]
    #                    midd1 = (mid1)
    #                    wN2.findAndAddContactsByMid(midd1)
    #                    wN2.inviteIntoGroup(op.param1,[midd1])
    #                    wN1.acceptGroupInvitation(op.param1)
    #                except:
    #                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
    #                    mid1=["u4a0f653ea757da7abcd41c15bf0f15da"]
    #                    midd1 = (mid1)
    #                    random.choice(KAC).findAndAddContactsByMid(midd1)
    #                    random.choice(KAC).inviteIntoGroup(op.param1,[midd1])
    #                    wN1.acceptGroupInvitation(op.param1)
    #                
    #        if op.param3 in Bots:
    #            if op.param2 not in admin:
    #                try:
    3                    wN4.kickoutFromGroup(op.param1,[op.param2])        
    #                    Amid=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
    #                    midd2 = (Amid)
    #                    wN3.findAndAddContactsByMid(midd2)
    #                    wN3.inviteIntoGroup(op.param1,[midd2])
    #                    wN2.acceptGroupInvitation(op.param1)
    #                except:
    #                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])        
    #                    Amid=["udb0b6b2c1f32887d23bd3e4dfb302ed1"]
    #                    midd2 = (Amid)
    #                    random.choice(KAC).findAndAddContactsByMid(midd2)
    #                    random.choice(KAC).inviteIntoGroup(op.param1,[midd2])
     #                   wN2.acceptGroupInvitation(op.param1)
     #                   
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN5.kickoutFromGroup(op.param1,[op.param2])
     #                   Bmid=["uad6cb020c5ca7afbecb4681675eb38cd"]
     #                   midd3 = (Bmid)
     #                   wN4.findAndAddContactsByMid(midd3)
     #                   wN4.inviteIntoGroup(op.param1,[midd3])
     #                   wN3.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Bmid=["uad6cb020c5ca7afbecb4681675eb38cd"]
     #                   midd3 = (Bmid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd3)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd3])
     #                   wN3.acceptGroupInvitation(op.param1)
     #               
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN6.kickoutFromGroup(op.param1,[op.param2])
     #                   Cmid=["ud5262649376cbf7576e2dcac0331d481"]
     #                   midd4 = (Cmid)
     #                   wN5.findAndAddContactsByMid(midd4)
     #                   wN5.inviteIntoGroup(op.param1,[midd4])
     #                   wN4.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Cmid=["ud5262649376cbf7576e2dcac0331d481"]
     #                   midd4 = (Cmid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd4)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd4])
     #                   wN4.acceptGroupInvitation(op.param1)
                    
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN7.kickoutFromGroup(op.param1,[op.param2])
     #                   Dmid=["u53c352134325f0c49e86534c57801bd7"]
     #                   midd5 = (Dmid)
     #                   wN6.findAndAddContactsByMid(midd5)
     #                   wN6.inviteIntoGroup(op.param1,[midd5])
     #                   wN5.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Dmid=["u53c352134325f0c49e86534c57801bd7"]
     #                   midd5 = (Dmid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd5)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd5])
     #                   wN5.acceptGroupInvitation(op.param1)
     #               
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN8.kickoutFromGroup(op.param1,[op.param2])
     #                   Emid=["ua2ea9f4c32848bc67644c5267bb91279"]
     #                   midd6 = (Emid)
     #                   wN7.findAndAddContactsByMid(midd6)
     #                   wN7.inviteIntoGroup(op.param1,[midd6])
     #                   wN6.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Emid=["ua2ea9f4c32848bc67644c5267bb91279"]
     #                   midd6 = (Emid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd6)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd6])
     #                   wN6.acceptGroupInvitation(op.param1)
     #               
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN9.kickoutFromGroup(op.param1,[op.param2])
     #                   Fmid=["uadfd3a23698b71d17c64482d27dc2ed1"]
     #                   midd7 = (Fmid)
     #                   wN8.findAndAddContactsByMid(midd7)
     #                   wN8.inviteIntoGroup(op.param1,[midd7])
     #                   wN7.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Fmid=["uadfd3a23698b71d17c64482d27dc2ed1"]
     #                   midd7 = (Fmid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd7)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd7])
     #                   wN7.acceptGroupInvitation(op.param1)
     #               
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN10.kickoutFromGroup(op.param1,[op.param2])
     #                   Gmid=["u45c6ce403f0acc28392c519028aae154"]
     #                   midd8 = (Gmid)
     #                   wN9.findAndAddContactsByMid(midd8)
     #                   wN9.inviteIntoGroup(op.param1,[midd8])
     #                   wN8.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Gmid=["u45c6ce403f0acc28392c519028aae154"]
     #                   midd8 = (Gmid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd8)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd8])
     #                   wN8.acceptGroupInvitation(op.param1)
     #               
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN1.kickoutFromGroup(op.param1,[op.param2])
     #                   Hmid=["udcf44c4272d8209a8a5f2dd1afeea93f"]
     #                   midd9 = (Hmid)
     #                   wN10.findAndAddContactsByMid(midd9)
     #                   wN10.inviteIntoGroup(op.param1,[midd9])
     #                   wN9.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Hmid=["udcf44c4272d8209a8a5f2dd1afeea93f"]
     #                   midd9 = (Hmid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd9)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd9])
     #                   wN9.acceptGroupInvitation(op.param1)
     #               
     #       if op.param3 in Bots:
     #           if op.param2 not in admin:
     #               try:
     #                   wN2.kickoutFromGroup(op.param1,[op.param2])
     #                   Imid=["u4a0be979fc73e88ebfe915bc917237b8"]
     #                   midd10 = (Imid)
     #                   wN1.findAndAddContactsByMid(midd10)
     #                   wN1.inviteIntoGroup(op.param1,[midd10])
     #                   wN10.acceptGroupInvitation(op.param1)
     #               except:
     #                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
     #                   Imid=["u4a0be979fc73e88ebfe915bc917237b8"]
     #                   midd10 = (Imid)
     #                   random.choice(KAC).findAndAddContactsByMid(midd10)
     #                   random.choice(KAC).inviteIntoGroup(op.param1,[midd10])
     #                   wN10.acceptGroupInvitation(op.param1)
#====#======================[CBW]===========================
        if op.type == 19:
            if mid1 in op.param3:
                wait["blacklist"][op.param2] = True
#==========================[CBW]===========================
        if op.type == 22:
            if wait['leaveRoom'] == True:
                wN1.leaveRoom(op.param1)
                wN2.leaveRoom(op.param1)
                wN3.leaveRoom(op.param1)
                wN4.leaveRoom(op.param1)
                wN5.leaveRoom(op.param1)
                wN6.leaveRoom(op.param1)
                wN7.leaveRoom(op.param1)
                wN8.leaveRoom(op.param1)
                wN9.leaveRoom(op.param1)
                wN10.leaveRoom(op.param1)
#==========================[CBW]===========================
        if op.type == 24:
            if wait['leaveRoom'] == True:
                wN1.leaveRoom(op.param1)
                wN2.leaveRoom(op.param1)
                wN3.leaveRoom(op.param1)
                wN4.leaveRoom(op.param1)
                wN5.leaveRoom(op.param1)
                wN6.leaveRoom(op.param1)
                wN7.leaveRoom(op.param1)
                wN8.leaveRoom(op.param1)
                wN9.leaveRoom(op.param1)
                wN10.leaveRoom(op.param1)
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message

            if msg.toType == 1:
                if wait['leaveRoom'] == True:
                    wN1.leaveRoom(msg.to)
                    wN2.leaveRoom(msg.to)
                    wN3.leaveRoom(msg.to)
                    wN4.leaveRoom(msg.to)
                    wN5.leaveRoom(msg.to)
                    wN6.leaveRoom(msg.to)
                    wN7.leaveRoom(msg.to)
                    wN8.leaveRoom(msg.to)
                    wN9.leaveRoom(msg.to)
                    wN10.leaveRoom(msg.to)
#==========================[CBW]===========================
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                wN1.like(url[25:58], url[66:], likeType=1001)
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        wN1.sendText(msg.to,text)
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data["status"] == 200:
                            if data['result']['result'] == 100:
                                wN1.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
#==========================[CBW]===========================
            if "MENTION" in msg.contentMetadata.keys() != None:
                if wait['detectMention'] == True:
                    contact = wN1.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "Kangenkah sampai ngetag mulu?",cName + " nah mending pc aja klo penting..!", "kenapa, ", cName + " kangen ya?","kangen bilang, gak usah ngetag mulu, " + cName, "sekali lagi ngetag, bayar ya..!!! " + cName, "Tuh kan" + cName + "ngetag lagi, mojok aja yux...!!!"]
                    ret_ = "[Auto Respon] " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in Bots:
                            wN1.sendText(msg.to,ret_)
                            msg.contentType = 7
                            msg.text = None
                            msg.contentMetadata = {
                                                        "STKID": "11866873",
                                                        "STKPKGID": "1293049",
                                                        "STKVER": "1" }
                            wN1.sendMessage(msg)
                            break            
#==========================[CBW]===========================
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['potoMention'] == True:
                     contact = wN1.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in Bots:
                                  wN1.sendImageWithURL(msg.to,ret_)
                                  break  
#==========================[CBW]===========================
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['kickMention'] == True:
                     contact = wN1.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + "Kangenkah sampai ngetag mulu?",cName + " nah mending pc aja klo penting..!", "kenapa, ", cName + " kangen ya?","kangen bilang, gak usah ngetag mulu, " + cName, "sekali lagi ngetag, bayar ya..!!! " + cName, "Tuh kan" + cName + "ngetag lagi, mojok aja yux...!!!"]
                     ret_ = "[Auto Respon] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN1.sendText(msg.to,ret_)
                                  wN1.kickoutFromGroup(msg.to,[msg.from_])
                                  wN1.inviteIntoGroup(msg.to, admin)
                                  break
#==========================[CBW]===========================
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = wN1.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             wN1.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 wN1.findAndAddContactsByMid(target)
                                 wN1.inviteIntoGroup(msg.to,[target])
                                 wN1.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      wN1.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            if msg.contentType == 13:
                if wait['invite2'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = random.choice(KAC).getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             random.choice(KAC).sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 random.choice(KAC).findAndAddContactsByMid(target)
                                 random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite2 " + _name)
                                 wait['invite2'] = False
                                 break                              
                             except:             
                                      random.choice(KAC).sendText(msg.to,"Error")
                                      wait['invite2'] = False
                                      break
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = wN1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                wN1.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                wN1.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                wN1.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    wN1.findAndAddContactsByMid(target)
                                    wN1.inviteIntoGroup(msg.to,[target])
                                    wN1.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        wN1.findAndAddContactsByMid(invite)
                                        wN1.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        wN1.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break
#==========================[CBW]===========================
                    if msg.from_ in admin or owner:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = wN2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                wN2.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                wN2.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                wN2.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    wN2.findAndAddContactsByMid(target)
                                    wN2.inviteIntoGroup(msg.to,[target])
                                    wN2.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        wN2.findAndAddContactsByMid(invite)
                                        wN2.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        wN2.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
#==========================[CBW]===========================
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        wN1.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        wN1.sendText(msg.to,"Nothing")
#==========================[CBW]===========================
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        wN1.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        wN1.sendText(msg.to,"Not in Blacklist")
#==========================[CBW]===========================
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        wN1.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        wN1.sendText(msg.to,"Done")
#==========================[CBW]===========================
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        wN1.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        wN1.sendText(msg.to,"Done")
#==========================[CBW]===========================
                elif wait['contact'] == True:
                    msg.contentType = 0
                    wN1.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = wN1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = wN1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        wN1.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = wN1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = wN1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        wN1.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#==========================[CBW]===========================
            elif msg.contentType == 16:
                if wait['timeline'] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    wN1.sendText(msg.to,msg.text)
#==========================[CBW]===========================
            elif msg.text is None:
                return
#==========================[CBW]===========================
            elif msg.text.lower() == 'help':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpmsg)
                    else:
                        wN1.sendText(msg.to,helpmsg)
#==========================[CBW]===========================
            elif msg.text.lower() == 'keybot':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,keymsg)
                    else:
                        wN1.sendText(msg.to,keymsg)
#==========================[CBW]===========================
            elif msg.text.lower() == 'keypro':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helppro)
                    else:
                        wN1.sendText(msg.to,helppro)
#==========================[CBW]===========================
            elif msg.text.lower() == 'keyself':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpself)
                    else:
                        wN1.sendText(msg.to,helpself)
#==========================[CBW]===========================
            elif msg.text.lower() == 'keygrup':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpgrup)
                    else:
                        wN1.sendText(msg.to,helpgrup)
#==========================[CBW]===========================
            elif msg.text.lower() == 'keyset':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpset)
                    else:
                        wN1.sendText(msg.to,helpset)
#==========================[CBW]===========================
            elif msg.text.lower() == 'keytran':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helptranslate)
                    else:
                        wN1.sendText(msg.to,helptranslate)
#==========================[CBW]===========================
            elif msg.text.lower() == 'keyrhs':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helprhs)
                    else:
                        wN1.sendText(msg.to,helprhs)
#==========================[CBW]===========================
            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                    start = time.time()
                    wN1.sendText(msg.to, "❂➣Proses.....")
                    elapsed_time = time.time() - start
                    wN1.sendText(msg.to, "%sseconds" % (elapsed_time))
#==========================[CBW]===========================
            elif msg.text.lower() == 'crash':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN2.sendMessage(msg)
                    wN2.sendMessage(msg)
#==========================[CBW]===========================
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                wN1.sendMessage(msg)
#==========================[CBW]===========================
            elif msg.text.lower() == 'bot':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid1}
                    wN1.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Amid}
                    wN2.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Bmid}
                    wN3.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Cmid}
                    wN4.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Dmid}
                    wN5.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Emid}
                    wN6.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Fmid}
                    wN7.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Gmid}
                    wN8.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Hmid}
                    wN9.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Imid}
                    wN10.sendMessage(msg)
                    random.choice(KAC).sendImageWithURL(msg.to, url123)
                    random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Owner Bots ↩↥↥↥↥↥")
#==========================[CBW]===========================
            elif "facebook " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("facebook ","")
                    b = urllib.quote(a)
                    wN1.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    wN1.sendText(msg.to, "https://www.facebook.com" + b)
                    wN1.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")    
#==========================[CBW]===========================
            elif msg.text.lower() == 'mode on':
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protecion Already On")
                        else:
                            wN1.sendText(msg.to,"Protecion Already On")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protecion Already On")
                        else:
                            wN1.sendText(msg.to,"Protecion Already On")
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already On")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already On")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already On")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already On")
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Invite already On")
                        else:
                            wN1.sendText(msg.to,"Protection Invite already On")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    if wait["QrProtect"] == True:#<==========
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect QR On")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect QR On")
                        else:
                            wN1.sendText(msg.to,"done")
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Member Protection On")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Member Protection On")
                        else:
                            wN1.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        wN1.sendText(msg.to,"TURN ON")
                    else:
                        wN1.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = wN1.getGroup(msg.to).name
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already on")
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already on")
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Guest Stranger On")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Guest Stranger On")
                        else:
                            wN1.sendText(msg.to,"done")
                    if wait["Protectgr"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect Link On")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect Link On")
                        else:
                            wN1.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text.lower() == 'mode off':
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection already Off")
                        else:
                            wN1.sendText(msg.to,"Protection already Off")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                        else:
                            wN1.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already off")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already off")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already Off")
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Invite already Off")
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Cancel already Off")
                    if wait["QrProtect"] == False:#<===
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect QR Off")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect QR Off")
                        else:
                            wN1.sendText(msg.to,"done")
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Member Protection Off")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Member Protection Off")
                        else:
                            wN1.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        wN1.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        wN1.sendText(msg.to,"ALREADY OFF")
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect already oғғ")
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Kick already oғғ")
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Guest Stranger Off")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Guest Stranger Off")
                        else:
                            wN1.sendText(msg.to,"done")
                    if wait["Protectgr"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect Link Off")
                        else:
                            wN1.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protect Link Off")
                        else:
                            wN1.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text.lower() == 'contact on':
                if msg.from_ in admin:
                    if wait['contact'] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        wait['contact'] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == 'contact off':
                if msg.from_ in admin:
                    if wait['contact'] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                    else:
                        wait['contact'] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            wN1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
#==========================[CBW]===========================
            elif msg.text.lower() == 'protect on':
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protecion Already On")
                        else:
                            wN1.sendText(msg.to,"Protecion Already On")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protecion Already On")
                        else:
                            wN1.sendText(msg.to,"Protecion Already On")
#==========================[CBW]===========================
            elif msg.text.lower() == 'qr on':
                if msg.from_ in admin:
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already On")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already On")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already On")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already On")
#==========================[CBW]===========================
            elif msg.text.lower() == 'invite on':
                if msg.from_ in admin:
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Invite already On")
                        else:
                            wN1.sendText(msg.to,"Protection Invite already On")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
#==========================[CBW]===========================
            elif msg.text.lower() == 'cancel on':
                if msg.from_ in admin:
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
#==========================[CBW]===========================
            elif msg.text.lower() == 'autojoin on':
                if msg.from_ in admin:
                    if wait['autoJoin'] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                    else:
                        wait['autoJoin'] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            wN1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
#==========================[CBW]===========================
            elif msg.text.lower() == 'autojoin off':
                if msg.from_ in admin:
                    if wait['autoJoin'] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            wN1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                    else:
                        wait['autoJoin'] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            wN1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
#==========================[CBW]===========================
            elif msg.text.lower() == 'protect off':
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection already Off")
                        else:
                            wN1.sendText(msg.to,"Protection already Off")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                        else:
                            wN1.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
#==========================[CBW]===========================
            elif msg.text.lower() == 'qr off':
                if msg.from_ in admin:
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already off")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already off")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Qr already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Qr already Off")
#==========================[CBW]===========================
            elif msg.text.lower() == 'invit off':
                if msg.from_ in admin:
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Invite already Off")
#==========================[CBW]===========================
            elif msg.text.lower() == 'cancel off':
                if msg.from_ in admin:
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            wN1.sendText(msg.to,"Protection Cancel already Off")
#==========================[CBW]===========================
            elif "Grup cancel:" in msg.text:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Grup cancel:","")
                        if strnum == "off":
                            wait['autoCancel']["on"] = False
                            if wait["lang"] == "JP":
                                wN1.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                            else:
                                wN1.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                        else:
                            num =  int(strnum)
                            wait['autoCancel']["on"] = True
                            if wait["lang"] == "JP":
                                wN1.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                            else:
                                wN1.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                    except:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Nilai tidak benar")
                        else:
                            wN1.sendText(msg.to,"Weird value")
#==========================[CBW]===========================
            elif msg.text.lower() == 'autoleave on':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            wN1.sendText(msg.to,"Auto Leave room already on")
                    else:
                        wait['leaveRoom'] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            wN1.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            wN1.sendText(msg.to,"Auto Leave room already off")
                    else:
                        wait['leaveRoom'] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            wN1.sendText(msg.to,"Auto Leave room already off")
#==========================[CBW]===========================
      #      elif msg.text.lower() == 'share on':
      #          if msg.from_ in admin:
      #              if wait['timeline'] == True:
      #                  if wait["lang"] == "JP":
      #                      wN1.sendText(msg.to,"Share set to on")
      #                  else:
      #                      wN1.sendText(msg.to,"Share already on")
      #              else:
      #                  wait['timeline'] = True
      #                  if wait["lang"] == "JP":
      #                      wN1.sendText(msg.to,"Share set to on")
      #                  else:
      #                      wN1.sendText(msg.to,"Share already on")
#==========================[CBW]===========================
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif msg.text.lower() == 'share off':
                if msg.from_ in admin:
                    if wait['timeline'] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Share set to off")
                        else:
                            wN1.sendText(msg.to,"Share already off")
                    else:
                        wait['timeline'] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Share set to off")
                        else:
                            wN1.sendText(msg.to,"Share already off")
#==========================[CBW]===========================
            elif msg.text.lower() == "status":
                if msg.from_ in admin:
                    md = """╔═════════════\n"""
                    if wait['contact'] == True: md+="╠❂➣Contact:on [✅]\n"
                    else: md+="╠❂➣Contact:off [❌]\n"
                    if wait['autoJoin'] == True: md+="╠❂➣Auto Join:on [✅]\n"
                    else: md +="╠❂➣Auto Join:off [❌]\n"
                    if wait['autoCancel']["on"] == True:md+="╠❂➣Auto cancel:" + str(wait['autoCancel']["members"]) + "[✅]\n"
                    else: md+= "╠❂➣Group cancel:off [❌]\n"
                    if wait['leaveRoom'] == True: md+="╠❂➣Auto leave:on [✅]\n"
                    else: md+="╠❂➣Auto leave:off [❌]\n"
                    if wait['timeline'] == True: md+="╠❂➣Share:on [✅]\n"
                    else:md+="╠❂➣Share:off [❌]\n"
                    if wait['autoAdd'] == True: md+="╠❂➣Auto add:on [✅]\n"
                    else:md+="╠❂➣Auto add:off [❌]\n"
                    if wait["protect"] == True: md+="╠❂➣Protect:on [✅]\n"
                    else:md+="╠❂➣Protect:off [❌]\n"
                    if wait["linkprotect"] == True: md+="╠❂➣Link Protect:on [✅]\n"
                    else:md+="╠❂➣Link Protect:off [❌]\n"
                    if wait["inviteprotect"] == True: md+="╠❂➣Invitation Protect:on [✅]\n"
                    else:md+="╠❂➣Invitation Protect:off [❌]\n"
                    if wait["cancelprotect"] == True: md+="╠❂➣Cancel Protect:on [✅]\n"
                    else:md+="╠❂➣Cancel Protect:off [❌]\n╚═════════════"
                    wN1.sendText(msg.to,md)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
                    wN1.sendMessage(msg)
#==========================[CBW]===========================
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
                wN1.sendMessage(msg)
                wN1.sendText(msg.to,'❂➣ Creator yang manis kalem  􀜁􀄯􏿿')
#==========================[CBW]===========================
          #  elif msg.text.lower() == 'autoadd on':
          #
          #      if msg.from_ in admin:
          #          if wait['autoAdd'] == True:
          #              if wait["lang"] == "JP":
          #                  wN1.sendText(msg.to,"Auto add set to on")
          #              else:
          #                  wN1.sendText(msg.to,"Auto add already on")
          #          else:
          #              wait['autoAdd'] = True
          #              if wait["lang"] == "JP":
          #                  wN1.sendText(msg.to,"Auto add set to on")
          #              else:
          #                  wN1.sendText(msg.to,"Auto add already on")
          #  elif msg.text.lower() == 'autoadd off':
          #      if msg.from_ in admin:
          #          if wait['autoAdd'] == False:
          #              if wait["lang"] == "JP":
          #                  wN1.sendText(msg.to,"Auto add set to off")
          #              else:
          #                  wN1.sendText(msg.to,"Auto add already off")
          #          else:
          #              wait['autoAdd'] = False
          #              if wait["lang"] == "JP":
          #                  wN1.sendText(msg.to,"Auto add set to off")
          #              else:
          #                  wN1.sendText(msg.to,"Auto add already off")
#==========================[CBW]===========================
            elif "Pesan set:" in msg.text:
                if msg.from_ in admin:
                    wait['message'] = msg.text.replace("Pesan set:","")
                    wN1.sendText(msg.to,"We changed the message")
#==========================[CBW]===========================
            elif msg.text.lower() == 'pesan cek':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
                    else:
                        wN1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
#==========================[CBW]===========================
            elif "Coment Set:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Coment Set:","")
                    if c in [""," ","\n",None]:
                        wN1.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                    else:
                        wait["comment"] = c
                        wN1.sendText(msg.to,"Ini telah diubah\n\n" + c)
#==========================[CBW]===========================
    #        elif msg.text in ["Comment on"]:
    #            if msg.from_ in admin:
    #                if wait["commentOn"] == True:
    #                    if wait["lang"] == "JP":
    #                        wN1.sendText(msg.to,"Aku berada di")
    #                    else:
    #                        wN1.sendText(msg.to,"To open")
    #                else:
    #                    wait["commentOn"] = True
    #                    if wait["lang"] == "JP":
    #                        wN1.sendText(msg.to,"Comment Actived")
    #                    else:
    #                        wN1.sendText(msg.to,"Comment Has Been Active")
    #        elif msg.text in ["Comment off"]:
    #            if msg.from_ in admin:
    #                if wait["commentOn"] == False:
    #                    if wait["lang"] == "JP":
     #                       wN1.sendText(msg.to,"Hal ini sudah off")
     #                   else:
     #                       wN1.sendText(msg.to,"It is already turned off")
     #               else:
     #                   wait["commentOn"] = False
     #                   if wait["lang"] == "JP":
     #                       wN1.sendText(msg.to,"Off")
     #                   else:
     #                       wN1.sendText(msg.to,"To turn off")
#==========================[CBW]===========================
            elif msg.text in ["Com","Comment"]:
                if msg.from_ in admin:
                    wN1.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                if msg.from_ in admin:
                    wait["wblack"] = True
                    wN1.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                if msg.from_ in admin:
                    wait["dblack"] = True
                    wN1.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if msg.from_ in admin:
                    if wait["commentBlack"] == {}:
                        wN1.sendText(msg.to,"Nothing in the blacklist")
                    else:
                        wN1.sendText(msg.to,"The following is a blacklist")
                        mc = ""
                        for mi_d in wait["commentBlack"]:
                            mc += "ãƒ»" +wN1.getContact(mi_d).displayName + "\n"
                        wN1.sendText(msg.to,mc)
#==========================[CBW]===========================
      #      elif msg.text.lower() == 'jam on':
      #          if msg.from_ in admin:
      #              if wait["clock"] == True:
      #                  wN1.sendText(msg.to,"Jam already on")
      #              else:
       #                 wait["clock"] = True
    #                    now2 = datetime.now()
     #                   nowT = datetime.strftime(now2,"?%H:%M?")
      #                  profile = wN1.getProfile()
       #                 profile.displayName = wait["cName"] + nowT
        #                wN1.updateProfile(profile)
         #               wN1.sendText(msg.to,"Jam set on")
         #   elif msg.text.lower() == 'jam off':
          #      if msg.from_ in admin:
          #          if wait["clock"] == False:
           #             wN1.sendText(msg.to,"Jam already off")
        #            else:
         #               wait["clock"] = False
          #              wN1.sendText(msg.to,"Jam set off")
        #    elif "Jam say:" in msg.text:
        #        if msg.from_ in admin:
        #            n = msg.text.replace("Jam say:","")
        #            if len(n.decode("utf-8")) > 30:
        #                wN1.sendText(msg.to,"terlalu lama")
        #            else:
        #                wait["cName"] = n
        3                wN1.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = wN1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        wN1.updateProfile(profile)
                        wN1.sendText(msg.to,"Diperbarui")
                    else:
                        wN1.sendText(msg.to,"Silahkan Aktifkan Jam")
#==========================[CBW]===========================
            elif "Image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        wN1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#==========================[CBW]===========================
            elif "Spam change:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam change:","")
                        wN1.sendText(msg.to,"spam changed")
#==========================[CBW]===========================
            elif "Spam add:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam add:","")
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"spam changed")
                        else:
                            wN1.sendText(msg.to,"Done")
#==========================[CBW]===========================
            elif "Spam:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        strnum = msg.text.replace("Spam:","")
                        num = int(strnum)
                        for var in range(0,num):
                            wN1.sendText(msg.to, wait['spam'])
#==========================[CBW]===========================
            elif ".spam " in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        bctxt = msg.text.replace(".spam ", "")
                        t = wN1.getAllContactIds()
                        t = 500
                        while(t):
                            wN1.sendText(msg.to, (bctxt))
#==========================[CBW]===========================
            elif "Spamcontact @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Spamcontact @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(g.mid,'spam')
                            wN1.sendText(msg.to, "Selesai di Spam")
                            print " Spammed !"
#==========================[CBW]===========================
#            elif "crashkontak @" in msg.text:
#                if msg.from_ in owner:
#                    _name = msg.text.replace("crashkontak @","")
#                    _nametarget = _name.rstrip(' ')
#                    gs = wN1.getGroup(msg.to)
#                    for g in gs.members:
#                        if _nametarget == g.displayName:
#                            xname = g.displayName + g.mid
#                            xlen = str(len(xname)+1)
#                            msg.contentType = 13
#                            msg.text = 'mid'+xname+''
#                            msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
#                            wN1.sendMessage(msg)
#                            wN1.sendText("crash kontak selesai")
#                            print " Spammed crash !"
#==========================[CBW]===========================
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    wN1.sendText(msg.to,"Kirim Contact")
#==========================[CBW]===========================
            elif msg.text in ["Jepit"]:
                if msg.from_ in admin:
                    wait["invite2"] = True
                    random.choice(KAC).sendText(msg.to,"Kirim Contact")
#==========================[CBW]===========================
            elif msg.text in ["Undang"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    wN2.sendText(msg.to,"Kirim Contact")
#==========================[CBW]===========================
            elif msg.text in ["Steal contact"]:
                if msg.from_ in admin:
                    wait['contact'] = True
                    wN1.sendText(msg.to,"Send Contact")
#==========================[CBW]===========================
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    wN1.sendText(msg.to,"Like Status Owner")
                    try:
                        likeme()
                    except:
                        pass
#==========================[CBW]===========================
         #   elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
         #       if msg.from_ in admin:
         #           print "[Command]Like executed"
         #           wN1.sendText(msg.to,"Like Status Teman")
         #           try:
         #               likefriend()
         #           except:
         #               pass
#==========================[CBW]===========================
         #   elif msg.text in ["Like:on","Like on"]:
         #       if msg.from_ in admin:
         #           if wait['likeOn'] == True:
         #               if wait["lang"] == "JP":
         #                   wN1.sendText(msg.to,"Done")
         #           else:
         #               wait['likeOn'] = True
         #               if wait["lang"] == "JP":
         #                   wN1.sendText(msg.to,"Already")
#==========================[CBW]===========================  
            elif msg.text in ["Like off","Like:off"]:
                if msg.from_ in admin:
                    if wait['likeOn'] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Already")
#==========================[CBW]===========================  
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = True
                    wN1.sendText(msg.to,"Simi mode On")
#==========================[CBW]=========================== 
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = False
                    wN1.sendText(msg.to,"Simi mode Off")
#==========================[CBW]===========================  
            elif msg.text in ["Tag on","tag on"]:
                if msg.from_ in admin:
                    wait['detectMention'] = True
                    wN1.sendText(msg.to,"Auto respon tag On")
#==========================[CBW]===========================
            elif msg.text in ["Tag off","tag off"]:
                if msg.from_ in admin:
                    wait['detectMention'] = False
                    wN1.sendText(msg.to,"Auto respon tag Off")
#==========================[CBW]===========================
            elif msg.text in ["Poto on","poto on"]:
                if msg.from_ in admin:
                    wait['potoMention'] = True
                    wN1.sendText(msg.to,"Auto respon tag poto On")
#==========================[CBW]===========================   
            elif msg.text in ["Poto off","poto off"]:
                if msg.from_ in admin:
                    wait['potoMention'] = False
                    wN1.sendText(msg.to,"Auto respon tag poto Off")
#==========================[CBW]===========================
            elif msg.text in ["Tag2 on","tag2 on"]:
                if msg.from_ in admin:
                    wait['kickMention'] = True
                    wN1.sendText(msg.to,"Auto Kick tag ON")
#==========================[CBW]=========================== 
            elif msg.text in ["Tag2 off","tag2 off"]:
                if msg.from_ in admin:
                    wait['kickMention'] = False
                    wN1.sendText(msg.to,"Auto Kick tag OFF")
#==========================[CBW]===========================
            elif "Time" in msg.text:
                if msg.toType == 2:
                    wN1.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==========================[CBW]===========================
            elif msg.text in ["Sambut on","sambut on"]:
                if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"noтιғ yg joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already on")
            elif msg.text in ["Sambut off","sambut off"]:
                if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"noтιғ yg joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
            elif msg.text in ["Sambut2 on","sambut2 on"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"noтιғ yg joιn poto on")
                    else:
                        wait["Wc2"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already on")
            elif msg.text in ["Sambut2 off","sambut2 off"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"noтιғ yg joιn poto oғғ")
                    else:
                        wait["Wc2"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
            elif msg.text in ["Pergi on","pergi on"]:
                if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"noтιғ yg leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","pergi off"]:
                if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"noтιғ yg leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
            elif ".bubar99" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        if msg.toType == 2:
                            print "ok"
                            _name = msg.text.replace(".bubar99","")
                            gs = wN1.getGroup(msg.to)
                            gs = wN2.getGroup(msg.to)
                            gs = wN3.getGroup(msg.to)
                            gs = wN4.getGroup(msg.to)
                            gs = wN5.getGroup(msg.to)
                            gs = wN6.getGroup(msg.to)
                            gs = wN7.getGroup(msg.to)
                            gs = wN8.getGroup(msg.to)
                            gs = wN9.getGroup(msg.to)
                            wN1.sendText(msg.to,"Jangan panik, santai aja ya ô")
                            wN2.sendText(msg.to,"Group di bersihkan...!!")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                wN1.sendText(msg.to,"Tidak di temukan")
                                wN2.sendText(msg.to,"Tidak di temukan")
                            else:
                                for target in targets:
                                    if target not in admin:
                                        try:
                                            klist=[wN1,wN2,wN3,wN4,wN5,wN6,wN7,wN8,wN9]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                            wN1.sendText(msg.to,"Group Bersih")
                                            wN2.sendText(msg.to,"Group Bersih")
#==========================[CBW]===========================
            elif msg.text in ["Salam1"]:
                wN1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN2.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                wN1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN2.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif msg.text in ["#bubar99"]:
                if msg.from_ in owner:
                    wN1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                    wN2.sendText(msg.to,"Assalamu'alaikum")
                    wN3.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                    wN4.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("#bubar99","")
                        gs = wN1.getGroup(msg.to)
                        gs = wN2.getGroup(msg.to)
                        gs = wN3.getGroup(msg.to)
                        gs = wN4.getGroup(msg.to)
                        gs = wN5.getGroup(msg.to)
                        gs = wN6.getGroup(msg.to)
                        gs = wN7.getGroup(msg.to)
                        gs = wN8.getGroup(msg.to)
                        gs = wN9.getGroup(msg.to)
                        wN1.sendText(msg.to,"maaf kalo gak sopan")
                        wN2.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                        wN3.sendText(msg.to,"hehehhehe")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            wN1.sendText(msg.to,"Tidak di temukan")
                        else:
                            for target in targets:
                                if target not in admin:
                                    try:
                                        klist=[wN1,wN2,wN3,wN4,wN5,wN6,wN7,wN8,wN9]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        wN1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                        wN2.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                        wN3.sendText(msg.to,"Nah salamnya jawab sendiri jadinya wkwkwk..!!")
#==========================[CBW]===========================
            elif ("Kick " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wN1.kickoutFromGroup(msg.to,[target])
                       except:
                           wN1.sendText(msg.to,"Error")
#==========================[CBW]===========================
            elif ("Nk " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target not in admin:
                            try:
                                wN1.kickoutFromGroup(msg.to,[target])
                                #wN1.inviteIntoGroup(msg.to,[admin])
                                wN1.cancelGroupInvitation(msg.to,[target])
                            except:
                                wN1.sendText(msg.to,"Error")
#==========================[CBW]===========================
#            elif "Tajong " in msg.text:
#                if msg.from_ in admin:
#                    nk0 = msg.text.replace("Tajong ","")
#                    nk1 = nk0.lstrip()
#                    nk2 = nk1.replace("@","")
#                    nk3 = nk2.rstrip()
#                    _name = nk3
#                    gs = wN1.getGroup(msg.to)
#                    ginfo = wN1.getGroup(msg.to)
#                    gs.preventJoinByTicket = False
#                    wN1.updateGroup(gs)
#                    invsend = 0
#                    Ticket = wN1.reissueGroupTicket(msg.to)
#                    wN6.acceptGroupInvitationByTicket(msg.to,Ticket)
#                    time.sleep(0.01)
#                    targets = []
#                    for s in gs.members:
#                        if _name in s.displayName:
#                           targets.append(s.mid)
#                    if targets == []:
#                       sendMessage(msg.to,"user does not exist")
#                       pass
#                    else:
#                       for target in targets:
#                          try:
#                            wN6.kickoutFromGroup(msg.to,[target])
#                            print (msg.to,[g.mid])
#                          except:
#                            wN6.leaveGroup(msg.to)
#                            gs = wN1.getGroup(msg.to)
#                            gs.preventJoinByTicket = True
#                            wN1.updateGroup(gs)
#                            gs.preventJoinByTicket(gs)
#                            wN1.updateGroup(gs)
#==========================[CBW]===========================
            elif "Kick: " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick: ","")
                    wN1.kickoutFromGroup(msg.to,[midd])
#==========================[CBW]===========================
            elif 'invite ' in msg.text.lower():
                if msg.from_ in admin:
                    key = msg.text[-33:]
                    wN1.findAndAddContactsByMid(key)
                    wN1.inviteIntoGroup(msg.to, [key])
                    contact = wN1.getContact(key)
#==========================[CBW]===========================
            elif msg.text.lower() == 'cancel':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = wN1.getGroup(msg.to)
                        if group.invitee is not None:
                            gInviMids = [contact.mid for contact in group.invitee]
                            wN1.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                wN1.sendText(msg.to,"Tidak ada undangan")
                            else:
                                wN1.sendText(msg.to,"Invitan tidak ada")
                    else:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Tidak ada undangan")
                        else:
                            wN1.sendText(msg.to,"Invitan tidak ada")
#==========================[CBW]===========================
            elif msg.text.lower() == 'link on':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = wN1.getGroup(msg.to)
                        group.preventJoinByTicket = False
                        wN1.updateGroup(group)
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"URL open")
                        else:
                            wN1.sendText(msg.to,"URL open")
                    else:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            wN1.sendText(msg.to,"Can not be used for groups other than")
#==========================[CBW]===========================
            elif msg.text.lower() == 'link off':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = wN1.getGroup(msg.to)
                        group.preventJoinByTicket = True
                        wN1.updateGroup(group)
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"URL close")
                        else:
                            wN1.sendText(msg.to,"URL close")
                    else:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            wN1.sendText(msg.to,"Can not be used for groups other than")
#==========================[CBW]===========================
            elif msg.text in ["Url","Gurl"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        g = wN1.getGroup(msg.to)
                        if g.preventJoinByTicket == True:
                            g.preventJoinByTicket = False
                            wN1.updateGroup(g)
                        gurl = wN1.reissueGroupTicket(msg.to)
                        wN1.sendText(msg.to,"line://ti/g/" + gurl)
#==========================[CBW]===========================   
            elif "Gcreator" == msg.text:
                try:
                    group = wN1.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    wN1.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    wN1.sendMessage(M)
                    wN1.sendText(msg.to,"Creator Grup")
#==========================[CBW]===========================
            elif msg.text.lower() == 'invite:gcreator':
                if msg.from_ in admin:
                    if msg.toType == 2:
                           ginfo = wN1.getGroup(msg.to)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if wait["lang"] == "JP":
                               wN1.inviteIntoGroup(msg.to,[gcmid])
                           else:
                               wN1.inviteIntoGroup(msg.to,[gcmid])
#==========================[CBW]===========================  
            elif ("Gname: " in msg.text):
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = wN1.getGroup(msg.to)
                        X.name = msg.text.replace("Gname: ","")
                        wN1.updateGroup(X)
#==========================[CBW]===========================  
            elif msg.text.lower() == 'infogrup':
                if msg.from_ in admin:
                    group = wN1.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    wN1.sendText(msg.to,md)
#==========================[CBW]===========================
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
#==========================[CBW]===========================
            elif msg.text.lower() == 'grup id':
                if msg.from_ in owner:
                    gid = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (wN1.getGroup(i).name,i)
                    wN1.sendText(msg.to,h)
#==========================[CBW]===========================
            elif msg.text in ["Glist"]:
                if msg.from_ in admin:
                    gid = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (wN1.getGroup(i).name +" ? ["+str(len(wN1.getGroup(i).members))+"]")
                    wN1.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
#==========================[CBW]===========================
            elif msg.text.lower() == 'gcancel':
                if msg.from_ in admin:
                    gid = wN1.getGroupIdsInvited()
                    for i in gid:
                        wN1.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Aku menolak semua undangan")
                    else:
                        wN1.sendText(msg.to,"He declined all invitations")
#==========================[CBW]===========================  
         #   elif "Auto add" in msg.text:
         #       if msg.from_ in admin:
         #           thisgroup = wN1.getGroups([msg.to])
         #           Mids = [contact.mid for contact in thisgroup[0].members]
         #           mi_d = Mids[:33]
         #           wN1.findAndAddContactsByMids(mi_d)
         #           wN1.sendText(msg.to,"Success Add all")
#==========================[CBW]===========================
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = wN1.getGroup(msg.to)
                gs = wN2.getGroup(msg.to)
                gs = wN3.getGroup(msg.to)
                gs = wN4.getGroup(msg.to)
                gs = wN5.getGroup(msg.to)
                gs = wN6.getGroup(msg.to)
                gs = wN7.getGroup(msg.to)
                gs = wN8.getGroup(msg.to)
                gs = wN9.getGroup(msg.to)
                gs = wN10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            wN1.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                wN1.sendText(msg.to,"Perintah Ditolak.")
                wN1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
#==========================[CBW]===========================
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = wN1.getGroup(msg.to)
                gs = wN2.getGroup(msg.to)
                gs = wN3.getGroup(msg.to)
                gs = wN4.getGroup(msg.to)
                gs = wN5.getGroup(msg.to)
                gs = wN6.getGroup(msg.to)
                gs = wN7.getGroup(msg.to)
                gs = wN8.getGroup(msg.to)
                gs = wN9.getGroup(msg.to)
                gs = wN10.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            wN1.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                wN1.sendText(msg.to,"Perintah Ditolak.")
                wN1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
#==========================[CBW]=========================== 
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  wN1.sendText(msg.to,"The stafflist is empty")
              else:
                  wN1.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════\n║Admin ✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰\n╠═════════════\n"
                  for mi_d in admin:
                      mc += "║••>" +wN1.getContact(mi_d).displayName + "\n╠═════════════\n"
                  wN1.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
#==========================[CBW]===========================
            elif msg.text in [".join","."]: #Panggil Semua Bot
                if msg.from_ in owner:
                    G = wN1.getGroup(msg.to)
                    ginfo = wN1.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    wN1.updateGroup(G)
                    invsend = 0
                    Ticket = wN1.reissueGroupTicket(msg.to)
                    wN2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN9.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN10.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    G = wN1.getGroup(msg.to)
                    ginfo = wN1.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    wN1.updateGroup(G)
                    wN5.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
                    print "Semua Sudah Lengkap"
#==========================[CBW]=========================== 
  #          elif msg.text in [".."]: #Panggil Semua Bot
  #              if msg.from_ in owner:
  #                  G = wN1.getGroup(msg.to)
  #                  ginfo = wN1.getGroup(msg.to)
  #                  midd2 = msg.text.replace("..","udb0b6b2c1f32887d23bd3e4dfb302ed1")
  #                  midd3 = msg.text.replace("..","uad6cb020c5ca7afbecb4681675eb38cd")
  #                  midd4 = msg.text.replace("..","ud5262649376cbf7576e2dcac0331d481")
  #                  midd5 = msg.text.replace("..","u53c352134325f0c49e86534c57801bd7")
  #                  midd6 = msg.text.replace("..","ua2ea9f4c32848bc67644c5267bb91279")
  #                  midd7 = msg.text.replace("..","uadfd3a23698b71d17c64482d27dc2ed1")
  #                  midd8 = msg.text.replace("..","u45c6ce403f0acc28392c519028aae154")
  #                  midd9 = msg.text.replace("..","udcf44c4272d8209a8a5f2dd1afeea93f")
  #                  midd10 = msg.text.replace("..","u4a0be979fc73e88ebfe915bc917237b8")
  #                  wN1.findAndAddContactsByMid(midd2)
  #                  wN1.findAndAddContactsByMid(midd3)
  #                  wN1.findAndAddContactsByMid(midd4)
  #                  wN1.findAndAddContactsByMid(midd5)
  #                  wN1.findAndAddContactsByMid(midd6)
  #                  wN1.findAndAddContactsByMid(midd7)
  #                  wN1.findAndAddContactsByMid(midd8)
  #                  wN1.findAndAddContactsByMid(midd9)
  #                  wN1.findAndAddContactsByMid(midd10)
  #                  wN1.inviteIntoGroup(msg.to,[midd2])
  #                  wN1.inviteIntoGroup(msg.to,[midd3])
  #                  wN1.inviteIntoGroup(msg.to,[midd4])
  #                  wN1.inviteIntoGroup(msg.to,[midd5])
  #                  wN1.inviteIntoGroup(msg.to,[midd6])
  #                  wN1.inviteIntoGroup(msg.to,[midd7])
  #                  wN1.inviteIntoGroup(msg.to,[midd8])
  #                  wN1.inviteIntoGroup(msg.to,[midd9])
  #                  wN1.inviteIntoGroup(msg.to,[midd10])
  #                  wN2.acceptGroupInvitation(msg.to)
  #                  wN3.acceptGroupInvitation(msg.to)
  #                  wN4.acceptGroupInvitation(msg.to)
  #                  wN5.acceptGroupInvitation(msg.to)
  #                  wN6.acceptGroupInvitation(msg.to)
  #                  wN7.acceptGroupInvitation(msg.to)
  #                  wN8.acceptGroupInvitation(msg.to)
  #                  wN9.acceptGroupInvitation(msg.to)
  #                  wN10.acceptGroupInvitation(msg.to)
  #                  wN10.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
  #                  print "Semua Sudah Lengkap"
   #3         elif msg.text in ["."]: #Panggil Bot induk
    #            if msg.from_ in owner:
    #                G = wN2.getGroup(msg.to)
    #                G = wN3.getGroup(msg.to)
    #                G = wN4.getGroup(msg.to)
    #                G = wN5.getGroup(msg.to)
    #                G = wN7.getGroup(msg.to)
    #                G = wN8.getGroup(msg.to)
    #                G = wN9.getGroup(msg.to)
    #                G = wN10.getGroup(msg.to)
    #                ginfo = wN2.getGroup(msg.to)
    #                ginfo = wN3.getGroup(msg.to)
    #                ginfo = wN4.getGroup(msg.to)
    #                ginfo = wN5.getGroup(msg.to)
    #                ginfo = wN6.getGroup(msg.to)
    #                ginfo = wN7.getGroup(msg.to)
    #                ginfo = wN8.getGroup(msg.to)
    #                ginfo = wN9.getGroup(msg.to)
    #                ginfo = wN10.getGroup(msg.to)
    #                midd1 = msg.text.replace(".","u4a0f653ea757da7abcd41c15bf0f15da")
    #                random.choice(KAC).findAndAddContactsByMid(midd1)
    #                random.choice(KAC).inviteIntoGroup(msg.to,[midd1])
    #                wN1.acceptGroupInvitation(msg.to)
    #                print "Induk Sudah Masuk"
#==========================[CBW]===========================
            elif msg.text in ["Kabur all","Kr kabur"]:#keluar semua bots
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = wN1.getGroup(msg.to)
                        ginfo = wN2.getGroup(msg.to)
                        ginfo = wN3.getGroup(msg.to)
                        ginfo = wN4.getGroup(msg.to)
                        ginfo = wN5.getGroup(msg.to)
                        ginfo = wN6.getGroup(msg.to)
                        ginfo = wN7.getGroup(msg.to)
                        ginfo = wN8.getGroup(msg.to)
                        ginfo = wN9.getGroup(msg.to)
                        ginfo = wN10.getGroup(msg.to)
                        try:
                            wN10.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN10.leaveGroup(msg.to)
                            wN9.leaveGroup(msg.to)
                            wN8.leaveGroup(msg.to)
                            wN7.leaveGroup(msg.to)
                            wN6.leaveGroup(msg.to)
                            wN5.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN2.leaveGroup(msg.to)
                            wN1.leaveGroup(msg.to)
                        except:
                            pass
#==========================[CBW]===========================
            elif msg.text in [".bye"]:#keluar bot kecuali bot induk
                if msg.from_ in owner:
                    if msg.toType == 2:
                        #ginfo = wN1.getGroup(msg.to)
                        ginfo = wN2.getGroup(msg.to)
                        ginfo = wN3.getGroup(msg.to)
                        ginfo = wN4.getGroup(msg.to)
                        ginfo = wN5.getGroup(msg.to)
                        ginfo = wN6.getGroup(msg.to)
                        ginfo = wN7.getGroup(msg.to)
                        ginfo = wN8.getGroup(msg.to)
                        ginfo = wN9.getGroup(msg.to)
                        ginfo = wN10.getGroup(msg.to)
                        try:
                            wN10.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN10.leaveGroup(msg.to)
                            wN9.leaveGroup(msg.to)
                            wN8.leaveGroup(msg.to)
                            wN7.leaveGroup(msg.to)
                            wN6.leaveGroup(msg.to)
                            wN5.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN2.leaveGroup(msg.to)
                            #wN1.leaveGroup(msg.to)
                        except:
                            pass
#==========================[CBW]===========================
            elif "hai" == msg.text.lower():
                if msg.from_ in admin:
                    group = wN1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 500:
                         print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    wN1.sendMessage(cnt)
#==========================[CBW]===========================
            elif "sepi" == msg.text.lower():
                if msg.from_ in admin:
                    group = wN1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 500:
                         print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    wN1.sendMessage(cnt)
#==========================[CBW]===========================
            elif "cctv on" == msg.text.lower():
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                            wN1.sendText(msg.to,"Setpoint already on")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                            wN1.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                            print wait2
#==========================[CBW]===========================
         #   elif msg.text.lower() == 'Bot':
         #       random.choice(KAC).sendImageWithURL(msg.to, url123)
        #        random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
                    
            elif "cctv off" == msg.text.lower():
                if msg.from_ in admin:
                    if msg.to not in wait2['readPoint']:
                        wN1.sendText(msg.to,"Setpoint already off")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                             pass
                        wN1.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
#==========================[CBW]===========================
            elif msg.text in ["lihat","Toong"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "\nRead aktif..."
                        if msg.to in wait2['readPoint']:
                            if wait2['ROM'][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2['ROM'][msg.to].items():
                                    print rom
                                    chiya += rom[1] + "\n"
                            wN1.sendText(msg.to, "╔═════════════ \n╠❂➣Sider :\n╠═════════════                     %s\n╠\n╠═════════════\n╠❂➣Reader :\n╠═════════════ %s\n╠\n╠═════════════\n╠In the last seen point:\n╠[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                            print "\nReading Point Set..."
                            try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                            except:
                                pass
                            wait2['readPoint'][msg.to] = msg.id
                            wait2['readMember'][msg.to] = ""
                            wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                            wait2['ROM'][msg.to] = {}
                            print "toong ready"
                            wN1.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                        else:
                            wN1.sendText(msg.to, "Ketik [Cctv on] dulu, baru ketik [Toong]")
#==========================[CBW]===========================
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
                    
            elif "intip" == msg.text.lower():
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                            wN1.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = wN1.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                            wN1.sendMessage(msg)
                        except Exception as error:
                            print error
                        pass

                    else:
                        wN1.sendText(msg.to, "Lurking has not been set.")
#==========================[CBW]===========================
            elif "Gbroadcast: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Gbroadcast: ","")
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        wN1.sendText(i, bc)
#==========================[CBW]=========================== 
            elif "Cbroadcast: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Cbroadcast: ","")
                    gid = wN1.getAllContactIds()
                    for i in gid:
                        wN1.sendText(i, bc)
#==========================[CBW]===========================
            elif "Spam change: " in msg.text:
                if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam change: ","")
                    wN1.sendText(msg.to,"spam changed")
#==========================[CBW]===========================
            elif "Spam add: " in msg.text:
                if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam add: ","")
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"spam changed")
                    else:
                        wN1.sendText(msg.to,"Done")
            
#==========================[CBW]===========================
            elif "Spamtag @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                        else:
                            pass
#==========================[CBW]=========================== 
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               wN1.sendText(msg.to, teks)
                        else:
                           wN1.sendText(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            wN1.sendText(msg.to, tulisan)
                        else:
                            wN1.sendText(msg.to, "Out Of Range!")
#==========================[CBW]===========================  
            elif ("Micadd " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            wN1.sendText(msg.to,"Target ditambahkan!")
                            break
                        except:
                            wN1.sendText(msg.to,"Fail !")
                            break
#==========================[CBW]===========================  
            elif ("Micdel " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            wN1.sendText(msg.to,"Target dihapuskan!")
                            break
                        except:
                            wN1.sendText(msg.to,"Fail !")
                            break
#==========================[CBW]=========================== 
            elif msg.text in ["Miclist"]:
                if msg.from_ in admin:
                    if mimic["target"] == {}:
                        wN1.sendText(msg.to,"nothing")
                    else:
                        mc = "Target mimic user\n"
                        for mi_d in mimic["target"]:
                            mc += "?? "+wN1.getContact(mi_d).displayName + "\n"
                        wN1.sendText(msg.to,mc)
#==========================[CBW]===========================
            elif "Mimic target " in msg.text:
                if msg.from_ in admin:
                    if mimic["copy"] == True:
                        siapa = msg.text.replace("Mimic target ","")
                        if siapa.rstrip(' ') == "me":
                            mimic["copy2"] = "me"
                            wN1.sendText(msg.to,"Mimic change to me")
                        elif siapa.rstrip(' ') == "target":
                            mimic["copy2"] = "target"
                            wN1.sendText(msg.to,"Mimic change to target")
                        else:
                            wN1.sendText(msg.to,"I dont know")
#==========================[CBW]===========================
            elif "Mimic " in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            wN1.sendText(msg.to,"Reply Message on")
                        else:
                            wN1.sendText(msg.to,"Sudah on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            wN1.sendText(msg.to,"Reply Message off")
                        else:
                            wN1.sendText(msg.to,"Sudah off")
#==========================[CBW]===========================
            elif "Setimage: " in msg.text:
                if msg.from_ in admin:
                    wait['pap'] = msg.text.replace("Setimage: ","")
                    wN1.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim",'pap']:
                if msg.from_ in admin:
                    wN1.sendImageWithURL(msg.to,wait['pap'])
            elif "Setvideo: " in msg.text:
                if msg.from_ in admin:
                    wait['pap'] = msg.text.replace("Setvideo: ","")
                    wN1.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                if msg.from_ in admin:
                    wN1.sendVideoWithURL(msg.to,wait['pap'])
            elif "TL:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        tl_text = msg.text.replace("TL:","")
                        wN1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+wN1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==========================[CBW]===========================
            elif msg.text.lower() == 'mymid':
                wN1.sendText(msg.to,mid)
#==========================[CBW]===========================
            elif "Timeline: " in msg.text:
                if msg.from_ in admin:
                    tl_text = msg.text.replace("Timeline: ","")
                    wN1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+wN1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==========================[CBW]===========================
            elif "Namebot: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN1.getProfile()
                        profile.displayName = string
                        wN1.updateProfile(profile)
                        wN1.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN2.getProfile()
                        profile.displayName = string
                        wN2.updateProfile(profile)
                        wN2.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN3.getProfile()
                        profile.displayName = string
                        wN3.updateProfile(profile)
                        wN3.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN4.getProfile()
                        profile.displayName = string
                        wN4.updateProfile(profile)
                        wN4.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN5.getProfile()
                        profile.displayName = string
                        wN5.updateProfile(profile)
                        wN5.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN6.getProfile()
                        profile.displayName = string
                        wN6.updateProfile(profile)
                        wN6.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN7.getProfile()
                        profile.displayName = string
                        wN7.updateProfile(profile)
                        wN7.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN8.getProfile()
                        profile.displayName = string
                        wN8.updateProfile(profile)
                        wN8.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN9.getProfile()
                        profile.displayName = string
                        wN9.updateProfile(profile)
                        wN9.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN10.getProfile()
                        profile.displayName = string
                        wN10.updateProfile(profile)
                        wN10.sendText(msg.to,"Changed " + string + "")
#==========================[CBW]===========================
            elif "Namebot1: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot1: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN1.getProfile()
                        profile.displayName = string
                        wN1.updateProfile(profile)
                        wN1.sendText(msg.to,"Changed " + string + "")
            elif "Namebot2: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot2: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN2.getProfile()
                        profile.displayName = string
                        wN2.updateProfile(profile)
                        wN2.sendText(msg.to,"Changed " + string + "")
            elif "Namebot3: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot3: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN3.getProfile()
                        profile.displayName = string
                        wN3.updateProfile(profile)
                        wN3.sendText(msg.to,"Changed " + string + "")
            elif "Namebot4: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot4: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN4.getProfile()
                        profile.displayName = string
                        wN4.updateProfile(profile)
                        wN4.sendText(msg.to,"Changed " + string + "")
            elif "Namebot5: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot5: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN5.getProfile()
                        profile.displayName = string
                        wN5.updateProfile(profile)
                        wN5.sendText(msg.to,"Changed " + string + "")
            elif "Namebot6: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot6: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN6.getProfile()
                        profile.displayName = string
                        wN6.updateProfile(profile)
                        wN6.sendText(msg.to,"Changed " + string + "")
            elif "Namebot7: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot7: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN7.getProfile()
                        profile.displayName = string
                        wN7.updateProfile(profile)
                        wN7.sendText(msg.to,"Changed " + string + "")
            elif "Namebot8: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot8: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN8.getProfile()
                        profile.displayName = string
                        wN8.updateProfile(profile)
                        wN8.sendText(msg.to,"Changed " + string + "")
            elif "Namebot9: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot9: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN9.getProfile()
                        profile.displayName = string
                        wN9.updateProfile(profile)
                        wN9.sendText(msg.to,"Changed " + string + "")
            elif "Namebot10: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot10: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN10.getProfile()
                        profile.displayName = string
                        wN10.updateProfile(profile)
                        wN10.sendText(msg.to,"Changed " + string + "")
#==========================[CBW]===========================
            elif "Biobot: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Biobot: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN1.getProfile()
                        profile.statusMessage = string
                        wN1.updateProfile(profile)
                        wN1.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN2.getProfile()
                        profile.statusMessage = string
                        wN2.updateProfile(profile)
                        wN2.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN3.getProfile()
                        profile.statusMessage = string
                        wN3.updateProfile(profile)
                        wN3.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN4.getProfile()
                        profile.statusMessage = string
                        wN4.updateProfile(profile)
                        wN4.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN5.getProfile()
                        profile.statusMessage = string
                        wN5.updateProfile(profile)
                        wN5.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN6.getProfile()
                        profile.statusMessage = string
                        wN6.updateProfile(profile)
                        wN6.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN7.getProfile()
                        profile.statusMessage = string
                        wN7.updateProfile(profile)
                        wN7.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN8.getProfile()
                        profile.statusMessage = string
                        wN8.updateProfile(profile)
                        wN8.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN9.getProfile()
                        profile.statusMessage = string
                        wN9.updateProfile(profile)
                        wN9.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN10.getProfile()
                        profile.statusMessage = string
                        wN10.updateProfile(profile)
                        wN10.sendText(msg.to,"Changed " + string)
#==========================[CBW]===========================
            elif msg.text in ["Myname"]:
                    h = wN1.getContact(mid)
                    wN1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybot"]:
                    h = wN1.getContact(mid)
                    h = wN2.getContact(Amid)
                    h = wN3.getContact(Bmid)
                    h = wN4.getContact(Cmid)
                    h = wN5.getContact(Dmid)
                    h = wN6.getContact(Emid)
                    h = wN7.getContact(Fmid)
                    h = wN8.getContact(Gmid)
                    h = wN9.getContact(Hmid)
                    h = wN10.getContact(Imid)
                    wN1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN2.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN3.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN4.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN5.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN6.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN7.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN8.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN9.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN10.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = wN1.getContact(mid)
                    wN1.sendText(msg.to,"═══[StatusMessage]═══\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = wN1.getContact(mid)
                    wN1.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = wN1.getContact(mid)
                    wN1.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = wN1.getContact(mid)
                    wN1.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif msg.text in ["Mycover"]:
                    h = wN1.getContact(mid)
                    cu = wN1.channel.getCover(mid)          
                    path = str(cu)
                    wN1.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = wN1.getContact(mid)
                    cu = wN1.channel.getCover(mid)          
                    path = str(cu)
                    wN1.sendText(msg.to, path)
#==========================[CBW]===========================
            elif "Getmid @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Getmid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            wN1.sendText(msg.to, g.mid)
                        else:
                            pass
            elif "Getinfo" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = wN1.getContact(key1)
                    cu = wN1.channel.getCover(key1)
                    try:
                        wN1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                    except:
                        wN1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = wN1.getContact(key1)
                    cu = wN1.channel.getCover(key1)
                    try:
                        wN1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                    except:
                        wN1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = wN1.getContact(key1)
                    cu = wN1.channel.getCover(key1)
                    try:
                        wN1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                    except:
                        wN1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = wN1.getContact(key1)
                    cu = wN1.channel.getCover(key1)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        wN1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        wN1.sendText(msg.to,"Profile Picture " + contact.displayName)
                        wN1.sendImageWithURL(msg.to,image)
                        wN1.sendText(msg.to,"Cover " + contact.displayName)
                        wN1.sendImageWithURL(msg.to,path)
                    except:
                        pass
            elif "Getcontact" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]                
                    mmid = wN1.getContact(key1)
                    msg.contentType = 13
                    msg.contentMetadata = {"mid": key1}
                    wN1.sendMessage(msg)
            elif "Getpict @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = wN1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                wN1.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getvid @","")
                    _nametarget = _name.rstrip('  ')
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = wN1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                wN1.sendVideoWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Picturl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = wN1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                wN1.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Getcover @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = wN1.getContact(target)
                                cu = wN1.channel.getCover(target)          
                                path = str(cu)
                                wN1.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Coverurl @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = wN1.getContact(target)
                                cu = wN1.channel.getCover(target)          
                                path = str(cu)
                                wN1.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                if msg.from_ in admin:
                    group = wN1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    wN1.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                if msg.from_ in admin:
                    group = wN1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    wN1.sendText(msg.to,path)
#==========================[CBW]===========================
            elif "Mycopy @" in msg.text:
                if msg.from_ in admin:
                    print "[COPY] Ok"
                    _name = msg.text.replace("Mycopy @","")
                    _nametarget = _name.rstrip('  ')
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN1.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                                wN1.CloneContactProfile(target)
                                wN1.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:
                if msg.from_ in admin:
                    try:
                        wN1.updateDisplayPicture(backup.pictureStatus)
                        wN1.updateProfile(backup)
                        wN1.sendText(msg.to, "Refreshed.")
                    except Exception as e:
                        wN1.sendText(msg.to, str(e))
#==============================================================================#
            elif "Testext: " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.replace("Testext: ", "")
                    wN1.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"
#==========================[CBW]===========================   
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                wN1.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                wN1.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                wN1.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                wN1.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                wN1.sendText(msg.to, A)
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN1.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
#==========================[CBW]===========================
            elif msg.text.lower() == 'welcome':
                ginfo = wN1.getGroup(msg.to)
                wN1.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                wN1.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                wN1.sendAudio(msg.to,'tts.mp3')
#==========================[CBW]===========================
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN1.sendAudio(msg.to,"hasil.mp3")
#==========================[CBW]=========================== 
            elif "#Kapan " in msg.text:
                tanya = msg.text.replace("#Kapan ","")
                jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                wN1.sendAudio(msg.to,'tts.mp3')
                wN1.sendText(msg.to,jawaban)
                wN2.sendText(msg.to,jawaban)
                wN2.sendText(msg.to,jawaban)
#==========================[CBW]===========================
         #   elif "Apakah " in msg.text:
         #       tanya = msg.text.replace("Apakah ","")
         #       jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
         #       jawaban = random.choice(jawab)
         #       tts = gTTS(text=jawaban, lang='id')
         #       tts.save('tts.mp3')
         #       wN1.sendAudio(msg.to,'tts.mp3')
         #       wN1.sendText(msg.to,jawaban)
         #       wN2.sendText(msg.to,jawaban)
         #       wN2.sendText(msg.to,jawaban)
#==========================[CBW]=========================== 
            elif msg.text in ["#Nah","#nah"]:
                wN1.sendText(msg.to,"Kan")
                wN1.sendText(msg.to,"Kan")
                wN1.sendText(msg.to,"Kan")
#==========================[CBW]===========================
            elif msg.text in ["Absen","absen"]:
                if msg.from_ in admin:
                    wN1.sendText(msg.to,"👉★★√")
                    wN2.sendText(msg.to,"👉★★√")
                    wN3.sendText(msg.to,"👉★★√")
                    wN4.sendText(msg.to,"👉★★√")
                    wN5.sendText(msg.to,"👉★★√")
                    wN6.sendText(msg.to,"👉★★√")
                    wN7.sendText(msg.to,"👉★★√")
                    wN8.sendText(msg.to,"👉★★√")
                    wN9.sendText(msg.to,"👉★★√")
                    wN10.sendText(msg.to,"👉★★√")
                    wN10.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
#==========================[CBW]===========================
            elif "Bcast " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Bcast ","")
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        wN1.sendText(i,"●▬▬▬▬ஜ۩[BROADCAST]۩ஜ▬▬▬▬●\n\n"+bc+"\n\n#BROADCAST!!")
#==========================[CBW]===========================
            elif 'Youtube ' in msg.text:
                if msg.from_ in admin:
                    try:
                        textToSearch = (msg.text).replace('Youtube ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        wN1.sendVideoWithURL(msg.to, ght)
                    except:
                        wN1.sendText(msg.to, "Could not find it")
            
            elif "Yt " in msg.text:
                if msg.from_ in admin:
                    query = msg.text.replace("Yt ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        wN1.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
#==========================[CBW]=========================== 
            elif "Lirik " in msg.text:
                if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace("Lirik ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            wN1.sendText(msg.to, hasil)
                    except Exception as wak:
                            wN1.sendText(msg.to, str(wak))
#==========================[CBW]===========================
            elif "Wikipedia " in msg.text:
                if msg.from_ in admin:
                    try:
                        wiki = msg.text.lower().replace("Wikipedia ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=1)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        wN1.sendText(msg.to, pesan)
                    except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            wN1.sendText(msg.to, pesan)
                        except Exception as e:
                            wN1.sendText(msg.to, str(e))
#==========================[CBW]===========================
            elif "Music " in msg.text:
                if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace("Music ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'This is Your Music\n'
                            hasil += 'Judul : ' + song[0]
                            hasil += '\nDurasi : ' + song[1]
                            hasil += '\nLink Download : ' + song[4]
                            wN1.sendText(msg.to, hasil)
                            wN1.sendText(msg.to, "Please Wait for audio...")
                            wN1.sendAudioWithURL(msg.to, song[4])
                    except Exception as njer:
                        wN1.sendText(msg.to, str(njer))
#==========================[CBW]===========================
            elif "Image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        wN1.sendImageWithURL(msg.to,path)
                    except:
                        pass           
#==========================[CBW]===========================
            elif "Instagram " in msg.text:
                if msg.from_ in admin:
                    try:
                        instagram = msg.text.replace("Instagram ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        wN1.sendImageWithURL(msg.to, profileIG)
                        wN1.sendText(msg.to, str(text))
                    except Exception as e:
                        wN1.sendText(msg.to, str(e))
#==========================[CBW]===========================
            elif "Kelahiran " in msg.text:
                if msg.from_ in admin:
                    tanggal = msg.text.replace("Kelahiran ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    lahir = data["data"]["lahir"]
                    usia = data["data"]["usia"]
                    ultah = data["data"]["ultah"]
                    zodiak = data["data"]["zodiak"]
                    wN1.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")
#==========================[CBW]===========================
            elif msg.text in ["Kalender"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                wN1.sendText(msg.to, rst)
#==========================[CBW]===========================
            elif msg.text.lower() == 'Bot':
                random.choice(KAC).sendImageWithURL(msg.to, url123)
                random.choice(KAC).sendText(msg.to,"↥↥↥↥↥↪ Pembuat Bots ↩↥↥↥↥↥")
            elif msg.text.lower() == 'ifconfig':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#==========================[CBW]===========================
            elif "Restart" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Restart"
                    try:
                        wN1.sendText(msg.to,"Restarting...")
                        wN1.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        wN1.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
#==========================[CBW]===========================
            elif "Kr turn off" in msg.text:
                if msg.from_ in owner:
                    try:
                        import sys
                        sys.exit()
                    except:
                        pass
#==========================[CBW]===========================
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot has been active "+waktu(eltime)
                    wN1.sendText(msg.to,van)
#==========================[CBW]===========================
            elif msg.text in ["Kr pulang]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
                if msg.from_ in owner:
                    gid = wN1.getGroupIdsJoined()
                    gid = wN2.getGroupIdsJoined()
                    gid = wN3.getGroupIdsJoined()
                    gid = wN4.getGroupIdsJoined()
                    gid = wN5.getGroupIdsJoined()
                    gid = wN6.getGroupIdsJoined()
                    gid = wN7.getGroupIdsJoined()
                    gid = wN8.getGroupIdsJoined()
                    gid = wN9.getGroupIdsJoined()
                    gid = wN10.getGroupIdsJoined()
                    for i in gid:
                        wN1.sendText(i,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                        wN1.leaveGroup(i)
                        wN2.leaveGroup(i)
                        wN3.leaveGroup(i)
                        wN4.leaveGroup(i)
                        wN5.leaveGroup(i)
                        wN6.leaveGroup(i)
                        wN7.leaveGroup(i)
                        wN8.leaveGroup(i)
                        wN9.leaveGroup(i)
                        wN10.leaveGroup(i)
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        wN1.sendText(msg.to,"He declined all invitations")
#==========================[CBW]=========================== 
            elif msg.text in ["cab","Cab"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab1","Cab1"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab2","Cab2"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab3","Cab3"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab4","Cab4"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab5","Cab5"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab6","Cab6"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab7","Cab7"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    wN1.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["Team","Logo"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url2 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                    url3 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                    url4 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                    url5 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    wN1.sendImageWithURL(msg.to, url)
                    wN1.sendImageWithURL(msg.to, url1)
                    wN1.sendImageWithURL(msg.to, url2)
                    wN1.sendImageWithURL(msg.to, url3)
                    wN1.sendImageWithURL(msg.to, url4)
                    wN1.sendImageWithURL(msg.to, url5)
                    wN1.sendImageWithURL(msg.to, url6)
                    wN1.sendImageWithURL(msg.to, url7)
                
            elif msg.text in ["Kibar","kibar"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    wN1.sendImageWithURL(msg.to, url)
                    wN1.sendImageWithURL(msg.to, url1)
                    wN1.sendImageWithURL(msg.to, url6)
                    wN1.sendImageWithURL(msg.to, url7)
#==========================[CBW]===========================
            elif "google " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    wN1.sendText(msg.to,"Sedang Mencari om...")
                    wN1.sendText(msg.to, "https://www.google.com/" + b)
                    wN1.sendText(msg.to,"Ketemu om ^")
#==========================[CBW]===========================
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN1.sendMessage(msg)
#==========================[CBW]===========================
            elif "friendpp: " in msg.text:
                if msg.from_ in admin:
                    suf = msg.text.replace('friendpp: ','')
                    gid = wN1.getAllContactIds()
                    for i in gid:
                        h = wN1.getContact(i).displayName
                        gna = wN1.getContact(i)
                        if h == suf:
                            wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[CBW]===========================
            elif "Checkmid: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace("Checkmid: ","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":saya}
                    wN1.sendMessage(msg)
                    contact = wN1.getContact(saya)
                    cu = wN1.channel.getCover(saya)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        wN1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        wN1.sendText(msg.to,"Profile Picture " + contact.displayName)
                        wN1.sendImageWithURL(msg.to,image)
                        wN1.sendText(msg.to,"Cover " + contact.displayName)
                        wN1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#==========================[CBW]===========================
            elif "Checkid: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace("Checkid: ","")
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        h = wN1.getGroup(i).id
                        group = wN1.getGroup(i)
                        if h == saya:
                            try:
                                creator = group.creator.mid 
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': creator}
                                md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                                else: md += "\n\nKode Url : Diblokir"
                                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                                wN1.sendText(msg.to,md)
                                wN1.sendMessage(msg)
                                wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                            except:
                                creator = "Error"
#==========================[CBW]===========================
            elif msg.text in ["Friendlist"]:
                if msg.from_ in owner:
                    contactlist = wN1.getAllContactIds()
                    kontak = wN1.getContacts(contactlist)
                    num=1
                    msgs="═════════List Friend═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                    wN1.sendText(msg.to, msgs)
#==========================[CBW]===========================
            elif msg.text in ["Memlist"]:
                if msg.from_ in owner:
                    kontak = wN1.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════-"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    wN1.sendText(msg.to, msgs)
#==========================[CBW]===========================
            elif "Friendinfo: " in msg.text:
                if msg.from_ in owner:
                    saya = msg.text.replace('Friendinfo: ','')
                    gid = wN1.getAllContactIds()
                    for i in gid:
                        h = wN1.getContact(i).displayName
                        contact = wN1.getContact(i)
                        cu = wN1.channel.getCover(i)
                        path = str(cu)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        if h == saya:
                            wN1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                            wN1.sendText(msg.to,"Profile Picture " + contact.displayName)
                            wN1.sendImageWithURL(msg.to,image)
                            wN1.sendText(msg.to,"Cover " + contact.displayName)
                            wN1.sendImageWithURL(msg.to,path)
#==========================[CBW]===========================
            elif "Friendpict: " in msg.text:
                if msg.from_ in owner:
                    saya = msg.text.replace('Friendpict: ','')
                    gid = wN1.getAllContactIds()
                    for i in gid:
                        h = wN1.getContact(i).displayName
                        gna = wN1.getContact(i)
                        if h == saya:
                            wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[CBW]===========================
            elif msg.text in ["Friendlistmid"]:
                if msg.from_ in owner:
                    gruplist = wN1.getAllContactIds()
                    kontak = wN1.getContacts(gruplist)
                    num=1
                    msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                    wN1.sendText(msg.to, msgs)
#==========================[CBW]===========================
            elif msg.text in ["Blocklist"]:
                if msg.from_ in admin:
                    blockedlist = wN1.getBlockedContactIds()
                    kontak = wN1.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    wN1.sendText(msg.to, msgs)
#==========================[CBW]===========================
            elif msg.text in ["Gruplist"]:
                if msg.from_ in admin:
                    gruplist = wN1.getGroupIdsJoined()
                    kontak = wN1.getGroups(gruplist)
                    num=1
                    msgs="═════════List Grup═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.name)
                        num=(num+1)
                    msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                    wN1.sendText(msg.to, msgs)
#==========================[CBW]===========================
            elif msg.text in ["Gruplistmid"]:
                if msg.from_ in owner:
                    gruplist = wN1.getGroupIdsJoined()
                    kontak = wN1.getGroups(gruplist)
                    num=1
                    msgs="═════════List GrupMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.id)
                        num=(num+1)
                    msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                    wN1.sendText(msg.to, msgs)
#==========================[CBW]===========================  
            elif "Grupimage: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupimage: ','')
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        h = wN1.getGroup(i).name
                        gna = wN1.getGroup(i)
                        if h == saya:
                            wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#==========================[CBW]===========================  
            elif "Grupname" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupname','')
                    gid = wN1.getGroup(msg.to)
                    wN1.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
#==========================[CBW]=========================== 
            elif "Grupid" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupid','')
                    gid = wN1.getGroup(msg.to)
                    wN1.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
#==========================[CBW]===========================      
            elif "Grupinfo: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupinfo: ','')
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        h = wN1.getGroup(i).name
                        group = wN1.getGroup(i)
                        if h == saya:
                            try:
                                creator = group.creator.mid 
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': creator}
                                md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                                else: md += "\n\nKode Url : Diblokir"
                                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                                wN1.sendText(msg.to,md)
                                wN1.sendMessage(msg)
                                wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                            except:
                                creator = "Error"
#==========================[CBW]===========================
#            elif "Spamtag @" in msg.text:
#                _name = msg.text.replace("Spamtag @","")
#                _nametarget = _name.rstrip(' ')
#                gs = wN1.getGroup(msg.to)
#                for g in gs.members:
#                    if _nametarget == g.displayName:
#                        xname = g.displayName
#                        xlen = str(len(xname)+1)
#                        msg.contentType = 0
#                        msg.text = "@"+xname+" "
#                        msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        wN1.sendMessage(msg)
#                        print "Spamtag Berhasil."
#==========================[CBW]===========================
            elif "playstore " in msg.text.lower():
                if msg.from_ in admin:
                    tob = msg.text.lower().replace("playstore ","")
                    wN1.sendText(msg.to,"Sedang Mencari boss...")
                    wN1.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    wN1.sendText(msg.to,"Ketemu boss ^")
#==========================[CBW]===========================
            elif 'wikipedia ' in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        wiki = msg.text.lower().replace("wikipedia ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=3)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        wN1.sendText(msg.to, pesan)
                    except:
                            try:
                                pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                                pesan+=wikipedia.page(wiki).url
                                wN1.sendText(msg.to, pesan)
                            except Exception as e:
                                wN1.sendText(msg.to, str(e))    
#==========================[CBW]===========================
            elif "say " in msg.text.lower():
                if msg.from_ in admin:
                    say = msg.text.lower().replace("say ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    wN1.sendAudio(msg.to,"hasil.mp3")
#==========================[CBW]===========================
            elif msg.text in ["Gift 8","Gift8","gift8"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)

                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)

                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '7'}
                    msg.text = None
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
    #==========================[CBW]===========================
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                wN1.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                wN1.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                wN1.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                wN1.sendMessage(msg)
#==========================[CBW]===========================
            elif msg.text in ["Gcreator:inv"]:
                if msg.from_ in admin:
                    ginfo = wN1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       wN1.findAndAddContactsByMid(gCreator)
                       wN1.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#==========================[CBW]===========================
            elif msg.text in ["Gcreator:kick"]:
                if msg.from_ in admin:
                    ginfo = wN1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       wN1.findAndAddContactsByMid(gCreator)
                       wN1.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#==========================[CBW]===========================
            elif 'lirik ' in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace('lirik ','')
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            wN1.sendText(msg.to, hasil)
                    except Exception as wak:
                            wN1.sendText(msg.to, str(wak))       
#==========================[CBW]===========================
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getcover @","")
                    _nametarget = _name.rstrip('  ')
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN2.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = wN1.getContact(target)
                                cu = wN1.channel.getCover(target)
                                path = str(cu)
                                wN1.sendImageWithURL(msg.to, path)
                            except:
                                pass
                    print "[Command]dp executed"
#==========================[CBW]===========================
            elif "idline: " in msg.text:
                if msg.from_ in admin:
                    msgg = msg.text.replace('idline: ','')
                    conn = wN1.findContactsByUserid(msgg)
                    if True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': conn.mid}
                        wN1.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                        wN1.sendMessage(msg)
#==========================[CBW]===========================   
            elif "reinvite" in msg.text.split():
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = wN1.getGroup(msg.to)
                        if group.invitee is not None:
                            try:
                                grCans = [contact.mid for contact in group.invitee]
                                wN1.findAndAddContactByMid(msg.to, grCans)
                                wN1.cancelGroupInvitation(msg.to, grCans)
                                wN1.inviteIntoGroup(msg.to, grCans)
                            except Exception as error:
                                print error
                        else:
                            if wait["lang"] == "JP":
                                wN1.sendText(msg.to,"No Invited")
                            else:
                                wN1.sendText(msg.to,"Error")
                    else:
                        pass
#==========================[CBW]=========================== 
            elif msg.text in ["Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                wN1.sendText(msg.to, rst)
#==========================[CBW]=========================== 
            elif "image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        wN1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#==========================[CBW]===========================
            elif 'instagram ' in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        instagram = msg.text.lower().replace("instagram ","")
                        html = requests.get('https://www.instagram.com/' + instagram + '/?')
                        soup = BeautifulSoup(html.text, 'html5lib')
                        data = soup.find_all('meta', attrs={'property':'og:description'})
                        text = data[0].get('content').split()
                        data1 = soup.find_all('meta', attrs={'property':'og:image'})
                        text1 = data1[0].get('content').split()
                        user = "Name: " + text[-2] + "\n"
                        user1 = "Username: " + text[-1] + "\n"
                        followers = "Followers: " + text[0] + "\n"
                        following = "Following: " + text[2] + "\n"
                        post = "Post: " + text[4] + "\n"
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        detail = "**INSTAGRAM INFO USER**\n"
                        details = "\n**INSTAGRAM INFO USER**"
                        wN1.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                        wN1.sendImageWithURL(msg.to, text1[0])
                    except Exception as njer:
                    	wN1.sendText(msg.to, str(njer))    
#==========================[CBW]===========================	
            elif msg.text in ["###","///"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
#==========================[CBW]===========================
            elif msg.text.lower() == '#...':
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN1.sendMessage(msg)    
#==========================[CBW]===========================
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Ban @","")
                        _nametarget = _name.rstrip()
                        gs = wN1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            wN1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    wN1.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                                except:
                                    wN1.sendText(msg.to,"Error")
#==========================[CBW]===========================
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip()
                        gs = wN1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            wN1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    wN1.sendText(msg.to,_nametarget + " Delete From Blacklist")
                                except:
                                    wN1.sendText(msg.to,_nametarget + " Not In Blacklist")
#==========================[CBW]===========================
            elif "Ban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Ban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                wN1.sendText(msg.to,_name + " Succes Add to Blacklist")
                            except:
                                wN1.sendText(msg.to,"Error")
#==========================[CBW]===========================
            elif "Unban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Unban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = wN1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                wN1.sendText(msg.to,_name + " Delete From Blacklist")
                            except:
                                wN1.sendText(msg.to,_name + " Not In Blacklist")
#==========================[CBW]===========================
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    wN1.sendText(msg.to,"Blacklist Telah Dibersihkan")
#==========================[CBW]===========================
            elif msg.text in ["Ban:on"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    wN1.sendText(msg.to,"Send Contact")
#==========================[CBW]===========================
            elif msg.text in ["Unban:on"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    wN1.sendText(msg.to,"Send Contact")
#==========================[CBW]===========================
            elif msg.text in ["Banlist"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        wN1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        wN1.sendText(msg.to,"Daftar Banlist")
                        num=1
                        msgs="*Blacklist*"
                        for mi_d in wait["blacklist"]:
                            msgs+="\n[%i] %s" % (num, wN1.getContact(mi_d).displayName)
                            num=(num+1)
                        msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                        wN1.sendText(msg.to, msgs)
#==========================[CBW]===========================
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        wN1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        wN1.sendText(msg.to,"Daftar Blacklist")
                        h = ""
                        for i in wait["blacklist"]:
                            h = wN1.getContact(i)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': i}
                            wN1.sendMessage(M)
#==========================[CBW]===========================
            elif msg.text in ["Midban","Mid ban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = wN1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        num=1
                        cocoa = "══════════List Blacklist═════════"
                        for mm in matched_list:
                            cocoa+="\n[%i] %s" % (num, mm)
                            num=(num+1)
                            cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                        wN1.sendText(msg.to,cocoa)
#==========================[CBW]===========================
            elif msg.text.lower() == 'scan blacklist':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = wN1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            wN1.sendText(msg.to,"Tidak ada Daftar Blacklist")
                            return
                        for jj in matched_list:
                            try:
                                wN1.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass       
#==========================[CBW]===========================
            elif "Kr spamtag @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Kr spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                        else:
                            pass
#==========================[CBW]===========================
            elif ("Kr cium " in msg.text):
                if msg.from_ in owner:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wN1.kickoutFromGroup(msg.to,[target])
                           #wN1.inviteIntoGroup(msg.to,[target])
                           wN1.cancelGroupInvitation(msg.to,[target])
                       except:
                           wN1.sendText(msg.to,"Error")
                           
            elif ("##Aah " in msg.text):
                if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                            wN1.sendMessage(msg)
                            wN1.kickoutFromGroup(msg.to,[target])
                            #wN1.inviteIntoGroup(msg.to,[target])
                            wN1.cancelGroupInvitation(msg.to,[target])
                        except:
                            wN1.sendText(msg.to,"Error")
                           
                    
#==========================[CBW]===========================
            elif msg.text in ["Kr glist"]: #Melihat List Group
                if msg.from_ in owner:
                    gids = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = wN1.getGroup(i).name
                      h += "[•]%s Member\n" % (wN1.getGroup(i).name   +"👉"+str(len(wN1.getGroup(i).members)))
                      wN1.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["Kr glist2"]: 
                if msg.from_ in owner:
                    gid = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                      h += "[%s]:%s\n" % (wN1.getGroup(i).name,i)
                      wN1.sendText(msg.to,h)
#==========================[CBW]===========================
            elif "Kr asupka " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("Kr asupka ","")
                    if gid == "":
                        wN1.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            wN1.findAndAddContactsByMid(msg.from_)
                            wN1.inviteIntoGroup(gid,[msg.from_])
                            wN1.sendText(msg.to,"succes di invite boss, silahkan masuk...!!")
                        except:
                            wN1.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#==========================[CBW]===========================
            elif "Kr megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("Kr megs ","")
                    ap = wN1.getGroups([msg.to])
                    semua = [contact.mid for contact in ap[0].members]
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
#==========================[CBW]===========================
            elif "#megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("#megs ","")
                    ap = wN1.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[kr]
                        team=random.choice(klis)
                        wN1.findAndAddContactsByMid(Mi_d)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        team.findAndAddContactsByMid(Mi_d)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
#==========================[CBW]===========================
            elif "recover" in msg.text:
                if msg.from_ in owner:
                    thisgroup = wN1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    wN1.createGroup("recover", mi_d)
                    wN1.sendText(msg.to,"Success recover")
#==========================[CBW]===========================
            elif "Kr spin" in msg.text:
                if msg.from_ in owner:
                    thisgroup = wN1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN1.sendText(msg.to,"Success...!!!!")
#==========================[CBW]===========================
            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    wN1.removeAllMessages(op.param2)
                    wN1.removeAllMessages(op.param2)
                    wN1.sendText(msg.to,"Removed all chat Finish")
#==========================[CBW]===========================
            elif msg.text in ["Kr muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN1.sendMessage(msg)
#==========================[CBW]===========================
        if op.type == 17:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        wN1.kickoutFromGroup(op.param1,[op.param2])
                        G = wN1.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        wN1.updateGroup(G)
                    except:
                        try:
                            wN1.kickoutFromGroup(op.param1,[op.param2])
                            G = wN1.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            wN1.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    wN1.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in admin:
                        if op.param2 in Bots or admin:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            wN1.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in admin:
                                if op.param2 in Bots or admin:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    wN1.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in admin:
                if op.param2 in Bots or admin:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = wN1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN1.updateGroup(G)
                    wN1.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait['autoAdd'] == True:
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    wN1.sendText(op.param1,str(wait['message']))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = wN1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    wN1.updateGroup(G)
        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = wN1.getGroup(op.param1)
               wN1.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc2"] == True:
                if op.param2 in Bots:
                    return
                G = wN1.getGroup(op.param1)
                h = wN1.getContact(op.param2)
                wN1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                wN1.sendText(op.param1, "╔═════════════\n║Baper Tuh Orang :v \n║Semoga Bahagia ya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#------------------------------------------------------------------------------#

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error


while True:
    try:
        Ops = wN1.fetchOps(wN1.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(wN1.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            wN1.Poll.rev = max(wN1.Poll.rev, Op.revision)
            bot(Op)
