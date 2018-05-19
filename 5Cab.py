# -*- coding: utf-8 -*-

import CBW
from.lib.curve.ttypes import *
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
wN1.login(token="Ep0AAwrkRJcgmDLyVD79.MuVPKSPTNJEmucSTO0EgMq.y/AY76kbpKgapbEM2If+yYh3SxBgMeuSDl6Nz9S7koc=")#1
wN1.loginResult()

wN2 = CBW.LINE()
#wN2.login(qr=True)
wN2.login(token="EpcTOVZHiUX1gTDSTYk0.rp3iy6AHhJAe6ULdRlS0Ga.Btx0aotiKeXVs6Kj+eXVOQCMNN20QY68egJiWMOVLm0=")#2
wN2.loginResult()

wN3 = CBW.LINE()
#wN3.login(qr=True)
wN3.login(token="EpSxQj58O78LTOEVDYS1.khW7clxXW6mpPpUIVAvOaq.N66BEQH4drJAzD/fX1bm4mGqgMX9ect9RPxyrJVbcfk=")#3
wN3.loginResult()

wN4 = CBW.LINE()
#wN4.login(qr=True)
wN4.login(token="Ep1oJF9PiITUgdZx7Y26.cFCuv1sJG0t3IQ+DSFO4XG.wwBSNStnbOgIXVct+cbLZvjQY4iKZf/2hW4EJliVX+4=")#4
wN4.loginResult()

wN5 = CBW.LINE()
#wN5.login(qr=True)
wN5.login(token="EpmpGTZ9iBsiCplV90xb.dGfnLg8q+kntKKhBdBzBwW.vBmz6Glxybki6q8AznOY64BWNwNh+BtchI0aaQIuqYU=")#5
wN5.loginResult()

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ CBW BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

keymsg ="""
╔═════════════
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║ ☔ 🎃w🎃N🎃 ☔
╠═════════════
║╔════════════
║╠❂➣Cipok
║╠❂➣Gcreator
║╠❂➣time
║╠❂➣Creator
║╠❂➣reinvite
║╠❂➣Absen
║╠❂➣runtime
║╠❂➣speed
║╠❂➣keybot
║╚════════════
╚═════════════"""

helpmsg ="""
╔═════════════
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
╠═════════════
║╔════════════
║╠❂➣keypro
║╠❂➣keyself
║╠❂➣keygrup
║╠❂➣keyset
║╠❂➣keytran
║╠❂➣mode on/off
║╠❂➣sider  on/off
║╚════════════
╚═════════════"""

helppro ="""
╔═════════════
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
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
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
╠═════════════
║╔════════════
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
║╚════════════
╚═════════════"""

helpset ="""
╔═════════════
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
╠═════════════
║╔════════════
║╠❂➣Gurl
║╠❂➣Grup cancel:
║╠❂➣contact on/off
║╠❂➣autojoin on/off
║╠❂➣autoleave on/off
║╠❂➣link on/off
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
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
╠═════════════
║╔════════════
║╠❂➣Link on/off
║╠❂➣Url
║╠❂➣Cancel
║╠❂➣Gcreator
║╠❂➣Kick @
║╠❂➣Cium @
║╠❂➣cancel
║╠❂➣Checkmid:
║╠❂➣Checkid:
║╠❂➣Blocklist
║╠❂➣Gruplist
║╠❂➣Grupinfo:
║╠❂➣Gcreator
║╠❂➣invite:gcreator
║╠❂➣Gname:
║╠❂➣infogrup
║╠❂➣grup id
║╠❂➣Glist
║╠❂➣gcancel
║╠❂➣CBW/. (manggil bot)
║╠❂➣Kabur all
║╠❂➣CBW bye
║╠❂➣Gbroadcast:
║╠❂➣Cbroadcast:
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

helprhs ="""
╔═════════════
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
╠═════════════
║╔════════════
║╠❂➣Dadas
║╠❂➣Restart
║╠❂➣Turn off
║╠❂➣Speed
║╠❂➣Bot kemari
║╠❂➣Restart
║╠❂➣Invite/Undang/Jepit
║╠❂➣Namebot:(txt)
║╠❂➣Namebot1/2/3/4/5: 
║╠❂➣Biobot: (txt)
║╠❂➣Gcreator:inv
║╠❂➣Gcreator:kick
║╠❂➣Kr cium 
║╠❂➣Kr glist
║╠❂➣Kr glist2
║╠❂➣Kr asupka
║╠❂➣Kr bye
║╠❂➣recover
║╠❂➣Remove all chat
║╠❂➣Kr muach
║╠❂➣Kr
║╚════════════
╚═════════════"""

KAC=[wN1,wN2,wN3,wN4,wN5]
mid = wN1.getProfile().mid
mid2 = wN2.getProfile().mid
mid3 = wN3.getProfile().mid
mid4 = wN4.getProfile().mid
mid5 = wN5.getProfile().mid
#mid6 = kr6.getProfile().mid

Bots=[mid,mid2,mid3,mid4,mid5]
owner=["uc301fa8f0962f52b1f2d83dc251589cb","u986c71616f66e33497b7426fb613cf03"]
admin=['uc301fa8f0962f52b1f2d83dc251589cb','uaecc760911be47db56c5d0cc3ae14a27','ufdedeacc6a6e547f11f36078a15acc7d','ued6685c48b974db65601f3df45ea8c88','udb7654c85bf03026c67eb58484a01e19','u0018100c35195db59f8e3e54f1c8458d','u4cf6ca2823590e1b591fc40e1f5f8d4b','u7e13848eb338e231ff8fd60ce1c3abde','u6d977673ac79a387754ea5bc66367258','u15d5edadf5f28e287467ebae5d49e08b','u835bb5cf7f37225b549183f1a3c95e6b','u500646b28f41c2e5da65be5d49f34611','u42c1d04491a86bd13b96a46b29a26624','u294c2a269514357dbd72942a6a5de92f','ueb2d19f1c0d360c554d4c6f3b0b21f57','u67ae6c3f22681db446f82a543dd17166','ud546a226737468be8b1bce9c2f117dc8','u88e75a99d2189494cc02c9219c56995f','u957a85dcde23fcb00df66646789b623f','u1e271a4a1c08a415a436d9b79bd44261','u68b7a12702d71c6bf9f2554c48942ed9','u7d8beb4e479b95f79402edfa5fb4a8dd','ud34c6c8afc9d2ae14a699cd1af8b99ca','u9a0a464f2d205820b4abb2af405a464e','u975332c6943b4cae49897378803213c7','u34b0e6d5be989ba2aac630d71b688a15','u90b064009b993edead05a0407698ab0c','uc71c7102d096738ff75e4ba4c6b58082','u9735a8e241bc721cc03a7b0c04183680','u88fa651d4bcaaac993dd2e2bd0573741','u44889826780c08da632c2e38730513bd','ud60a7d9e5fc384c87a39bd9bb0a249db','ueacd0d338652f31414983581c503314d','uf3279cc84a1b17b143d78d4cff7116c8','ufc7cd154d0ca1a1aaac03935a332ac18','uad55198e562bf893fdab53bcfc1e19be','u5cb9be1b7f51a9567542f498f5e8c611','ua8772ebd3b367e4579364be9101bfd8d','u9e16d4fd71f6b7dd1580ad9d6317187b','u3c7900254e12882bfd82e37c692f1e9f','u209a6dcf84c63b12e4ba636ea19f8531',mid,mid2,mid3,mid4,mid5]

wait = {
    'likeOn':False,
    'alwayRead':True,
    'removeAllChat':True,
    'detectMention':True, 
    'potoMention':False,
    'kickMention':False,
    'steal':True,
    'pap':{},
    'invite':{},
    'spam':{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':False,
   # 'autoAdd':False,
    'message':"""Thx for add\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆""",
    "lang":"JP",
   # "comment":"",
    #"commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames1":"↝↬₡αβ↫↜",
    "cNames2":"↝↬₡αβ↫↜",
    "cNames3":"↝↬₡αβ↫↜",
    "cNames4":"↝↬₡αβ↫↜",
    "cNames5":"↝↬₡αβ↫↜",
    "Wc":True,
    "Lv":True,
    "MENTION":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
    "Sider":{},
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
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

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
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


mulai = time.time()

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

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
#            if wait['autoAdd'] == True:
#                wN1.findAndAddContactsByMid(op.param1)
#                if (wait['message'] in [""," ","\n",None]):
#                    pass
#                else:
#                    wN1.sendText(op.param1,str(wait['message']))
#        if op.type == 26:
#            msg = op.message
#            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
#                    text = msg.text
#                    if text is not None:
#                        wN1.sendText(msg.to,text)
        if op.type == 13:
            print op.param3
            if op.param3 in mid:
                if op.param2 in owner:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in owner:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in owner:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in owner:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in owner:
                    wN5.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid:
                if op.param2 in mid2:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid3:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid4:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid5:
                    wN1.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid2:
                if op.param2 in mid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid3:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid4:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid5:
                    wN2.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid3:
                if op.param2 in mid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid2:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid4:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid5:
                    wN3.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid4:
                if op.param2 in mid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid2:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid3:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid5:
                    wN4.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid5:
                if op.param2 in mid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid2:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid3:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid4:
                    wN5.acceptGroupInvitation(op.param1)
                    
        if op.type == 13:
            if mid in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN1.acceptGroupInvitation(op.param1)
                else:
                  wN1.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid2 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN2.acceptGroupInvitation(op.param1)
                else:
                  wN2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid3 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN3.acceptGroupInvitation(op.param1)
                else:
                  wN3.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid4 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN4.acceptGroupInvitation(op.param1)
                else:
                  wN4.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid5 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN5.acceptGroupInvitation(op.param1)
                else:
                  wN5.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
        if op.type == 19: #bot Ke Kick
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = wN2.getGroup(op.param1)
                  G = wN3.getGroup(op.param1)
                  wN2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN3.updateGroup(G)
                  Ticket = wN3.reissueGroupTicket(op.param1)
                  wN1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN1.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid2:
              if op.param2 not in Bots or admin:
                try:
                  G = wN3.getGroup(op.param1)
                  G = wN4.getGroup(op.param1)
                  wN3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN4.updateGroup(G)
                  Ticket = wN4.reissueGroupTicket(op.param1)
                  wN2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN2.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid3:
              if op.param2 not in Bots or admin:
                try:
                  G = wN4.getGroup(op.param1)
                  G = wN5.getGroup(op.param1)
                  wN4.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN5.updateGroup(G)
                  Ticket = wN5.reissueGroupTicket(op.param1)
                  wN3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN3.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid4:
              if op.param2 not in Bots or admin:
                try:
                  G = wN5.getGroup(op.param1)
                  G = wN1.getGroup(op.param1)
                  wN5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN1.updateGroup(G)
                  Ticket = wN1.reissueGroupTicket(op.param1)
                  wN4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN4.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid5:
              if op.param2 not in Bots or admin:
                try:
                  G = wN1.getGroup(op.param1)
                  G = wN2.getGroup(op.param1)
                  wN2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN1.updateGroup(G)
                  Ticket = wN1.reissueGroupTicket(op.param1)
                  wN5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in admin:
              if op.param2 not in admin:
                try:
                  wN1.kickoutFromGroup(op.param1,[op.param2])
                  wN1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  try:
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    wN1.inviteIntoGroup(op.param1,[owner])
                    wait["blacklist"][op.param2] = True
                  except:
                    try:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[owner])
                      wait["blacklist"][op.param2] = True

            if op.param3 in admin or Bots:
                if op.param2 in admin or Bots:
                    try:
                        wN1.inviteIntoGroup(op.param1,owner)
                        wN1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,[owner])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

            if op.param3 in admin or owner:
              if op.param2 not in Bots:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  wN1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                  
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait['leaveRoom'] == True:
                wN1.leaveRoom(op.param1)
                wN2.leaveRoom(op.param1)
                wN3.leaveRoom(op.param1)
                wN4.leaveRoom(op.param1)
                wN5.leaveRoom(op.param1)
        if op.type == 24:
            if wait['leaveRoom'] == True:
                wN1.leaveRoom(op.param1)
                wN2.leaveRoom(op.param1)
                wN3.leaveRoom(op.param1)
                wN4.leaveRoom(op.param1)
                wN5.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            wN1.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = wN1.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            wN1.updateGroup(G)
                        except:
                            wN1.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait['leaveRoom'] == True:
                    wN1.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                wN1.like(url[25:58], url[66:], likeType=1001)
        
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

            if wait['alwayRead'] == True:
                if msg.toType == 0:
                    wN1.sendChatChecked(msg.from_,msg.id)
                else:
                    wN1.sendChatChecked(msg.to,msg.id)
                if msg.toType == 0:
                    wN2.sendChatChecked(msg.from_,msg.id)
                else:
                    wN2.sendChatChecked(msg.to,msg.id)    
                if msg.toType == 0:
                    wN3.sendChatChecked(msg.from_,msg.id)
                else:
                    wN3.sendChatChecked(msg.to,msg.id)    
                if msg.toType == 0:
                    wN4.sendChatChecked(msg.from_,msg.id)
                else:
                    wN4.sendChatChecked(msg.to,msg.id)    
                if msg.toType == 0:
                    wN5.sendChatChecked(msg.from_,msg.id)
                else:
                    wN5.sendChatChecked(msg.to,msg.id)        
                    
            if wait['removeAllChat'] == True:        
                if msg.toType == 0:    
                     wN1.removeAllMessages(op.param2)
                else:    
                     wN1.sendText(msg.to,"Removed all chat Finish")
                    
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        wN1.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        wN1.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        wN1.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        wN1.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        wN1.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        wN1.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        wN1.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        wN1.sendText(msg.to,"Done")
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
            elif msg.contentType == 16:
                if wait['timeline'] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    wN1.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpmsg)
                    else:
                        wN1.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'keybot':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,keymsg)
                    else:
                        wN1.sendText(msg.to,keymsg)
            elif msg.text.lower() == 'keypro':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helppro)
                    else:
                        wN1.sendText(msg.to,helppro)
            elif msg.text.lower() == 'keyself':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpself)
                    else:
                        wN1.sendText(msg.to,helpself)
            elif msg.text.lower() == 'keygrup':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpgrup)
                    else:
                        wN1.sendText(msg.to,helpgrup)
            elif msg.text.lower() == 'keyset':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helpset)
                    else:
                        wN1.sendText(msg.to,helpset)
#            elif msg.text.lower() == 'keytran':
#                if msg.from_ in admin:
#                    if wait["lang"] == "JP":
#                        wN1.sendText(msg.to,helptranslate)
#                    else:
#                        wN1.sendText(msg.to,helptranslate)
            elif msg.text.lower() == 'keyrhs':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helprhs)
                    else:
                        wN1.sendText(msg.to,helprhs)
                        
            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                    start = time.time()
                    wN1.sendText(msg.to, "❂➣Proses.....")
                    elapsed_time = time.time() - start
                    wN1.sendText(msg.to, "%sseconds" % (elapsed_time))
           
#======================== FOR COMMAND MODE ON STARTING ==========================#
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
#======================== FOR COMMAND MODE OFF STARTING ==========================#
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
#========================== FOR COMMAND BOT STARTING =============================#
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
            elif msg.text.lower() == '#share on':
                if msg.from_ in admin:
                    if wait['timeline'] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Share set to on")
                        else:
                            wN1.sendText(msg.to,"Share already on")
                    else:
                        wait['timeline'] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Share set to on")
                        else:
                            wN1.sendText(msg.to,"Share already on")
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
                    msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                    wN1.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN1.sendMessage(msg)
                wN1.sendText(msg.to,'❂➣ Creator yang manis kalem  􀜁􀄯􏿿')
 
            elif "Pesan set:" in msg.text:
                if msg.from_ in admin:
                    wait['message'] = msg.text.replace("Pesan set:","")
                    wN1.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
                    else:
                        wN1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
            elif "Coment Set:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Coment Set:","")
                    if c in [""," ","\n",None]:
                        wN1.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                    else:
                        wait["comment"] = c
                        wN1.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["#Comment on"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Aku berada di")
                        else:
                            wN1.sendText(msg.to,"To open")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Comment Actived")
                        else:
                            wN1.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Coment off"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Hal ini sudah off")
                        else:
                            wN1.sendText(msg.to,"It is already turned off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Off")
                        else:
                            wN1.sendText(msg.to,"To turn off")
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
            elif msg.text.lower() == 'jam on':
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        wN1.sendText(msg.to,"Jam already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = wN1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        wN1.updateProfile(profile)
                        wN1.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if msg.from_ in admin:
                    if wait["clock"] == False:
                        wN1.sendText(msg.to,"Jam already off")
                    else:
                        wait["clock"] = False
                        wN1.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                if msg.from_ in admin:
                    n = msg.text.replace("Jam say:","")
                    if len(n.decode("utf-8")) > 30:
                        wN1.sendText(msg.to,"terlalu lama")
                    else:
                        wait["cName"] = n
                        wN1.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
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
           
#==============================================================================#
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    wN3.sendText(msg.to,"Kirim Contact")
            elif msg.text in ["Jepit"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    wN1.sendText(msg.to,"Kirim Contact")
                    
            elif msg.text in ["Undang"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    wN2.sendText(msg.to,"Kirim Contact")
            
            elif msg.text in ["Steal contact"]:
                if msg.from_ in admin:
                    wait['contact'] = True
                    wN4.sendText(msg.to,"Send Contact")
#==============================================================================#
            elif "#bubar99" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        if msg.toType == 2:
                            print "ok"
                            _name = msg.text.replace("#bubar99","")
                            gs = wN1.getGroup(msg.to)
                            gs = wN2.getGroup(msg.to)
                            gs = wN3.getGroup(msg.to)
                            gs = wN4.getGroup(msg.to)
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
                                    try:
                                        klist=[wN1,wN2,wN3,wN4]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        wN1.sendText(msg.to,"Group Bersih")
                                        wN2.sendText(msg.to,"Group Bersih")
            elif ".bubar99" in msg.text:
                if msg.from_ in owner:
                    wN1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                    wN2.sendText(msg.to,"Assalamu'alaikum")
                    wN3.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                    wN4.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace(".bubar99","")
                        gs = wN1.getGroup(msg.to)
                        gs = wN2.getGroup(msg.to)
                        gs = wN3.getGroup(msg.to)
                        gs = wN4.getGroup(msg.to)
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
                                    klist=[wN1,wN2,wN3,wN4]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    wN1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                    wN2.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                    wN3.sendText(msg.to,"Nah salamnya jawab sendiri jadinya wkwkwk..!!")
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
            
            elif ("#Cium " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wN1.kickoutFromGroup(msg.to,[target])
                           wN1.inviteIntoGroup(msg.to,[target])
                           wN1.cancelGroupInvitation(msg.to,[target])
                       except:
                           wN1.sendText(msg.to,"Error")
            

            
            elif "Kick: " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick: ","")
                    wN1.kickoutFromGroup(msg.to,[midd])
            
            elif 'invite ' in msg.text.lower():
                if msg.from_ in admin:
                    key = msg.text[-33:]
                    wN1.findAndAddContactsByMid(key)
                    wN1.inviteIntoGroup(msg.to, [key])
                    contact = wN1.getContact(key)
            
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
            
            elif msg.text in ["Url","Gurl"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        g = wN1.getGroup(msg.to)
                        if g.preventJoinByTicket == True:
                            g.preventJoinByTicket = False
                            wN1.updateGroup(g)
                        gurl = wN1.reissueGroupTicket(msg.to)
                        wN1.sendText(msg.to,"line://ti/g/" + gurl)
                    
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
                    wN1.sendText(msg.to,"Gcreator Grup")
            
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
    
#==============================================================================#
            elif msg.text in ["#Glist"]:
                if msg.from_ in admin:
                    gid = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (wN1.getGroup(i).name +" ? ["+str(len(wN1.getGroup(i).members))+"]")
                    wN1.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'gcancel':
                if msg.from_ in admin:
                    gid = wN1.getGroupIdsInvited()
                    for i in gid:
                        wN1.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Aku menolak semua undangan")
                    else:
                        wN1.sendText(msg.to,"He declined all invitations")
                         
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
                    G = wN1.getGroup(msg.to)
                    ginfo = wN1.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    wN1.updateGroup(G)
                    wN5.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
                    print "Semua Sudah Lengkap"
                        
            elif "2bye" in msg.text:#keluar semua bots
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = wN1.getGroup(msg.to)
                        ginfo = wN2.getGroup(msg.to)
                        ginfo = wN3.getGroup(msg.to)
                        ginfo = wN4.getGroup(msg.to)
                        ginfo = wN5.getGroup(msg.to)
                        try:
                            wN1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN2.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN5.leaveGroup(msg.to)
                            wN1.leaveGroup(msg.to)
                        except:
                            pass
            elif ".bye" in msg.text:#keluar bot kecuali bot induk
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = wN1.getGroup(msg.to)
                        ginfo = wN2.getGroup(msg.to)
                        ginfo = wN3.getGroup(msg.to)
                        ginfo = wN4.getGroup(msg.to)
                        ginfo = wN5.getGroup(msg.to)
                        try:
                            wN2.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN3.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN4.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN5.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN2.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN5.leaveGroup(msg.to)
                            #wN1.leaveGroup(msg.to)
                        except:
                            pass
#==============================================================================#
            elif "Gbroadcast: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Gbroadcast: ","")
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        wN1.sendText(i, bc)
                    
            elif "Cbroadcast: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Cbroadcast: ","")
                    gid = wN1.getAllContactIds()
                    for i in gid:
                        wN1.sendText(i, bc)
#==============================================================================#
            elif msg.text.lower() == 'mymid':
                wN1.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                if msg.from_ in admin:
                    tl_text = msg.text.replace("Timeline: ","")
                    wN1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+wN1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
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
            elif msg.text in ["Myname"]:
                    h = wN1.getContact(mid)
                    wN1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybot"]:
                    h = wN1.getContact(mid)
                    h = wN2.getContact(mid2)
                    h = wN3.getContact(mid3)
                    h = wN4.getContact(mid4)
                    h = wN5.getContact(mid5)
                    wN1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN2.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN3.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN4.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN5.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            
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
#==============================================================================#
            elif "Absen" in msg.text:
                if msg.from_ in admin:
                    wN1.sendText(msg.to,"👉★★★√")
                    wN2.sendText(msg.to,"👉★★★★√")
                    wN3.sendText(msg.to,"👉★★★★★√")
                    wN4.sendText(msg.to,"👉★★★★★★√")
                    wN5.sendText(msg.to,"👉★★★★★★★√")
                    wN1.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
            
            elif "Bcast " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Bcast ","")
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        wN1.sendText(i,"●▬▬▬▬ஜ۩[BROADCAST]۩ஜ▬▬▬▬●\n\n"+bc+"\n\n#BROADCAST!!")          
#==============================================================================#
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
                    
            elif "Turn off" in msg.text:
                if msg.from_ in owner:
                    try:
                        import sys
                        sys.exit()
                    except:
                        pass
                
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot has been active "+waktu(eltime)
                    wN1.sendText(msg.to,van)

            elif msg.text in ["Bot pualang"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
                if msg.from_ in owner:
                    gid = wN1.getGroupIdsJoined()
                    gid = wN2.getGroupIdsJoined()
                    gid = wN3.getGroupIdsJoined()
                    gid = wN4.getGroupIdsJoined()
                    gid = wN5.getGroupIdsJoined()
                    for i in gid:
                        wN1.leaveGroup(i)
                        wN2.leaveGroup(i)
                        wN3.leaveGroup(i)
                        wN4.leaveGroup(i)
                        wN5.leaveGroup(i)
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        wN1.sendText(msg.to,"He declined all invitations")
#================================ CBW SCRIPT STARTED ==============================================#
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN1.sendMessage(msg)

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
                
            elif msg.text in ["#Gruplist"]:
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
                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                wN1.sendText(msg.to,van)
                
            elif msg.text in ["Restart"]:
                if msg.from_ in owner:
                    wN1.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"    
#=================================CBW SCRIPT FINISHED =============================================#
            
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
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    wN1.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban:on"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    wN1.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    wN1.sendText(msg.to,"Send Contact")
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
#==============================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        wN1.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        wN1.sendText(msg.to,"decided not to comment")
#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif ("#Nk " in msg.text):
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
                           
            elif msg.text in ["Cab glist"]: #Melihat List Group
                if msg.from_ in owner:
                    gids = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = wN1.getGroup(i).name
                      h += "[•]%s Member\n" % (wN1.getGroup(i).name   +"👉"+str(len(wN1.getGroup(i).members)))
                      wN1.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["Cab glist2"]: 
                if msg.from_ in owner:
                    gid = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                      h += "[%s]:%s\n" % (wN1.getGroup(i).name,i)
                      wN1.sendText(msg.to,h)

            elif "Cab asupka " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("Cab asupka ","")
                    if gid == "":
                        wN1.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            wN1.findAndAddContactsByMid(msg.from_)
                            wN1.inviteIntoGroup(gid,[msg.from_])
                            wN1.sendText(msg.to,"succes di invite boss, silahkan masuk...!!")
                        except:
                            wN1.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif "Cab bye" in msg.text:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = wN1.getGroup(msg.to)
                        try:
                            wN1.leaveGroup(msg.to)
                        except:
                            pass
            elif "recover" in msg.text:
                if msg.from_ in owner:
                    thisgroup = wN1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    wN1.createGroup("recover", mi_d)
                    wN1.sendText(msg.to,"Success recover")
          
            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    wN1.removeAllMessages(op.param2)
                    wN1.removeAllMessages(op.param2)
                    wN1.sendText(msg.to,"Removed all chat Finish")
            elif msg.text in ["Cab","cab"]:
                if msg.from_ in owner:
                    wN1.sendText(msg.to,"Cab masih aktif Say...!!!")
#===============================================
        if op.type == 17:
            if op.param2 not in Bots:
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
            if op.param2 not in Bots:
                if op.param2 in Bots or admin:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    wN1.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if wait["inviteprotect"] == True:
                wait ["blacklist"][op.param2] = True 
                if op.param2 in Bots or admin:
                    pass
                if op.param2 not in admin: #
                    wN1.cancelGroupInvitation(op.param1,[op.param3])
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    if wait["inviteprotect"] == True:
                        wait ["blacklist"][op.param2] = True
                        if op.param2 in Bots or admin:
                            pass
                        if op.param2 not in admin: #
                            wN1.cancelGroupInvitation(op.param1,[op.param3])
                            if wait["cancelprotect"] == True:
                                wait ["blacklist"][op.param2] = True
                                wN1.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 13: 
            print op.param3 
            if op.param3 in mid: 
                if op.param2 in owner: 
                    try: 
                        wN1.acceptGroupInvitation(op.param1) 
                        X = wN1.getGroup(op.param1) 
                        X.preventJoinByTicket = False 
                        wN1.updateGroup(X) 
                        Ti = wN1.reissueGroupTicket(op.param1) 
                        wN2.acceptGroupInvitationByTicket(op.param1,Ti) 
                        wN3.acceptGroupInvitationByTicket(op.param1,Ti) 
                        wN4.acceptGroupInvitationByTicket(op.param1,Ti) 
                        wN5.acceptGroupInvitationByTicket(op.param1,Ti) 
                        G = wN1.getGroup(op.param1) 
                        G.preventJoinByTicket = True 
                        wN1.updateGroup(G) 
                    except: 
                        X = wN1.getGroup(op.param1) 
                        X.preventJoinByTicket = True 
                        wN1.updateGroup(X) 
                        Ti = wN1.reissueGroupTicket(op.param1) 
                        wN2.acceptGroupInvitation(op.param1,Ti) 
                        wN3.acceptGroupInvitation(op.param1,Ti) 
                        wN4.acceptGroupInvitation(op.param1,Ti) 
                        wN5.acceptGroupInvitation(op.param1,Ti) 
                        G = wN1.getGroup(op.param1) 
                        G.preventJoinByTicket = True 
                        wN1.updateGroup(G)                           
       
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots or admin:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = wN1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN1.updateGroup(G)
                    wN1.kickoutFromGroup(op.param1,[op.param2])
 #       if op.type == 5:
 #           if wait['autoAdd'] == True:
 #               if (wait['message'] in [""," ","\n",None]):
 #                   pass
 #               else:
 #                   wN1.sendText(op.param1,str(wait['message']))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = wN1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN1.kickoutFromGroup(op.param1,[op.param3])
                    wN1.updateGroup(G)
        
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
