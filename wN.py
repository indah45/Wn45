# -*- coding: utf-8 -*-

import CBW
from CBW.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
#from googletrans import Translator
#JANGAN LUPA =>  sudo pip install bs4 => sudo pip install BeautifulSoup => sudo pip install urllib

wN = CBW.LINE()
#wN.login(qr=True)
#wN.login(token='EqNFdhPzRcPiYgmxmXHb.WWh6JWLI9sSFlypCjrwjYW.Wq0Fsp34M2ma6GgcJnjMI77sqCtxQGcZyWAhFJgJCCA=')#r
wN.login(token='Erbc5lTfAtbljygqxTLb.WWh6JWLI9sSFlypCjrwjYW.FGOBptJIHpL3bIjWthUQeZXu2eyPygS+wIPnnA21fRU=')#r
wN.loginResult()

print "╔════════════════════════════════════════════════════\n╠❂➣[KBERHASIL LOGIN]\n╚════════════════════════════════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

keymsg ="""
╔═════════════
║ 🐉 💚💚#NS3OC💚💚 🐉
╠═════════════
║╔════════════
║╠🐉➣google (text)
║╠🐉➣Playstore (text)
║╠🐉➣instagram (username)
║╠🐉➣wikipedia (text)
║╠🐉➣idline (text)
║╠🐉➣time
║╠🐉➣image (text)
║╠🐉➣runtime
║╠🐉➣Restart
║╠🐉➣lirik (text)
║╠🐉➣nah (mention)
║╠🐉➣cctv on/off (Lurk)
║╠🐉➣toong (Lurker)
║╠🐉➣protect on/off
║╠🐉➣qr on/off
║╠🐉➣invite on/off
║╠🐉➣Cancel on/off
║╠🐉➣Simisimi:on/off
║╠🐉➣Read on/off
║╠🐉➣Getinfo @
║╠🐉➣Getcontact @
║╠🐉➣Cium @
║╠🐉➣speed
║╠🐉➣Friendlist
║╠🐉➣id@eny
║╠🐉➣en@id
║╠🐉➣id@jp
║╠🐉➣keybot
║╚════════════
╚═════════════"""

helpmsg ="""
╔═════════════
║  🐉💚💚#NS3OC💚💚🐉
╠═════════════
║╔════════════
║╠🐉➣keypro
║╠🐉➣keyself
║╠🐉➣keygrup
║╠🐉➣keyset
║╠🐉➣keybot
║╠🐉➣mode on/off
║╚════════════
╚═════════════"""

helppro ="""
╔═════════════
║ 🐉 💚💚#NS3OC💚💚 🐉
╠═════════════
║╔════════════
║╠🐉➣mode on/off
║╠🐉➣protect on/off
║╠🐉➣qr on/off
║╠🐉➣invite on/off
║╠🐉➣cancel on/off
║╚════════════
╚═════════════"""

helpself ="""
╔═════════════
║ 🐉 💚💚#NS3OC💚💚 🐉
╠═════════════
║╔════════════
║╠🐉➣Me
║╠🐉➣Myname:
║╠🐉➣Mybio:
║╠🐉➣Mypict
║╠🐉➣Mycover
║╠🐉➣My copy @
║╠🐉➣My backup
║╠🐉➣Getgroup image
║╠🐉➣Getmid @
║╠🐉➣Getprofile @
║╠🐉➣Getinfo @
║╠🐉➣Getname @
║╠🐉➣Getbio @
║╠🐉➣Getpict @
║╠🐉➣Getcover @
║╠🐉➣sayang (Mention)
║╠🐉➣cctv on/off (Lurking)
║╠🐉➣intip/toong (Lurkers)
║╠🐉➣Micadd @
║╠🐉➣Micdel @
║╠🐉➣Mimic on/off
║╠🐉➣Miclist
║╚════════════
╚═════════════"""

helpset ="""
╔═════════════
║ 🐉 💚💚#NS3OC💚💚 🐉
║╔════════════
║╠🐉➣contact on/off
║╠🐉➣autojoin on/off
║╠🐉➣auto leave on/off
║╠🐉➣autoadd on/off
║╠🐉➣like frien\d
║╠🐉➣link on
║╠🐉➣respon on/off
║╠🐉➣read on/off
║╠🐉➣simisimi on/off
║╠🐉➣Sambut on/off
║╠🐉➣Pergi on/off
║╠🐉➣Respontag on/off
║╠🐉➣Kicktag on/off
║╚════════════
╚═════════════"""

helpgrup ="""
╔═════════════
║ 🐉 💚💚#NS3OC💚💚 🐉
╠═════════════
║╔════════════
║╠🐉➣Link on
║╠🐉➣Url
║╠🐉➣Cancel
║╠🐉➣Gcreator
║╠🐉➣Kick @
║╠🐉➣Cium @
║╠🐉➣Gname:
║╠🐉➣Gbroadcast:
║╠🐉➣Cbroadcast:
║╠🐉➣Infogrup
║╠🐉➣Gruplist
║╠🐉➣Friendlist
║╠🐉➣Blacklist
║╠🐉➣Ban @
║╠🐉➣Unban @
║╠🐉➣Clearban
║╠🐉➣Banlist
║╠🐉➣Contact ban
║╠🐉➣Midban
║╚════════════
║╔════════════
║╠🐉➣Id@en
║╠🐉➣En@id
║╠🐉➣Id@jp
║╠🐉➣Jp@id
║╠🐉➣Id@th
║╠🐉➣Th@id
║╠🐉➣Id@ar
║╠🐉➣Ar@id
║╠🐉➣Id@ko
║╠🐉➣Ko@id
║╠🐉➣Say-id
║╠🐉➣Say-en
║╠🐉➣Say-jp
║╚════════════
╚═════════════"""

KAC=[wN]
mid = wN.getProfile().mid

Bots=[mid]
admin=["uc301fa8f0962f52b1f2d83dc251589cb",mid]

wait = {
    "likeOn":False,
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    "steal":True,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':False,
   # 'autoAdd':False,
    #'message':"",
    "lang":"JP",
    "comment":"",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "Wc":False,
    "Lv":False,
    'MENTION':True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Sider":{},
    }

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
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
    
res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = wN.getProfile()
backup = wN.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage                        
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
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
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def yt(query): 
    with requests.session() as s: 
        isi = [] 
        if query == "": 
           query = "S1B tanysyz" 
        s.headers['user-agent'] = 'Mozilla/5.0' 
        url = 'http://www.youtube.com/results' 
        params = {'search_query': query} 
        r = s.get(url, params=params) 
        soup = BeautifulSoup(r.content, 'html5lib') 
        for a in soup.select('.yt-lockup-title > a[title]'): 
           if '&list=' not in a['href']: 
               if 'watch?v' in a['href']: 
                   b = a['href'].replace('watch?v=', '') 
                   isi += ['youtu.be' + b] 
        return isi

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
      bb += "► @c \n"
      #bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       wN.sendMessage(msg)
    except Exception as error:
       print error
       
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
         cl.sendMessage(msg)
    except Exception as error:
        print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                wN.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    wN.sendText(op.param1,str(wait["message"]))
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        wN.sendText(msg.to,text)
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in admin:
		    wN.acceptGroupInvitation(op.param1)
 #        if op.type == 13:
 #            if mid in op.param3:
 #              if wait["autoJoin"] == True:
 #                if op.param2 in Bots or admin:
#                   wN.acceptGroupInvitation(op.param1)
 #                else:
 #                  wN.rejectGroupInvitation(op.param1)
 #              else:
 #                print "autoJoin is Off"
        if op.type == 19:
            if op.param3 in admin:
                wN.kickoutFromGroup(op.param1,[op.param2])
                wN.inviteIntoGroup(op.param1,admin)
                wN.inviteIntoGroup(op.param1,[op.param3])
            else:
                pass
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                wN.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                wN.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            wN.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = wN.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            wN.updateGroup(G)
                        except:
                            wN.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    wN.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                wN.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        wN.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                wN.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = wN.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Don't Tag Me! iam Bussy!, ",cName + "Ada perlu apa beb 😴, ?",cName + " Beb pc aja klo urgent! sedang sibuk 😪,", "kenapa Beb 😇, ", cName + " kangen ya beb 😴?","kangen bilang gak usah tag tag Beb😲, " + cName, "kenapa beb,ni masih nikung 😇, " + cName, "apasi beb?ni lagi kojom 😋, " + cName + "?", "pulang gih beb😂,lukan jones😂, " + cName + "?","aya naon Beb 😲, ?" + cName + "😴😴 masi tidur Beb -_-"]
                     ret_ = "." + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN.sendText(msg.to,ret_)
                                  msg.contentType = 7 
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "13915097",
                                                       "STKPKGID": "7464",
                                                       "STKVER": "1" }
                                  wN.sendMessage(msg)
                                  break            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = wN.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["lagi kojom beb jangan tag dulu!! ",cName + " Ngapain Ngetag beb?,kangen ya 😲 ",cName + " Nggak Usah Tag-Tag! 😲 Kalo kangen Langsung Pc beb,kkkk", "-_-, ","maaf beb lagi off, ", cName + " jones Tag saya? 😲, ","masih nikung nih beb 😲, " + cName, "Jangan pangil terus beb nanti anu,kkk 😲, " + cName, "Kamu siapa beb tag mulu 😲, " + cName + "?", "Ada Perlu apa beb, " + cName + "?","Tag doang, telp dunk beb., "]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN.sendText(msg.to,ret_)
                                  wN.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = wN.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             wN.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 wN.findAndAddContactsByMid(target)
                                 wN.inviteIntoGroup(msg.to,[target])
                                 wN.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      wN.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            
            #if msg.contentType == 13:
            #    if wait["steal"] == True:
            #        _name = msg.contentMetadata["displayName"]
            #        copy = msg.contentMetadata["mid"]
            #        groups = wN.getGroup(msg.to)
            #        pending = groups.invitee
            #        targets = []
            #        for s in groups.members:
            #            if _name in s.displayName:
            #                print "[Target] Stealed"
            #                break                             
            #            else:
            #                targets.append(copy)
            #        if targets == []:
            #            pass
            #        else:
            #            for target in targets:
            #                try:
            #                    wN.findAndAddContactsByMid(target)
            #                    contact = wN.getContact(target)
            #                    cu = wN.channel.getCover(target)
            #                    path = str(cu)
            #                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            #                    wN.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
            #                    wN.sendText(msg.to,"Profile Picture " + contact.displayName)
            #                    wN.sendImageWithURL(msg.to,image)
            #                    wN.sendText(msg.to,"Cover " + contact.displayName)
            #                    wN.sendImageWithURL(msg.to,path)
            #                    wait["steal"] = False
            #                    break
            #                except:
            #                        pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    wN.sendChatChecked(msg.from_,msg.id)
                else:
                    wN.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        wN.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        wN.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        wN.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        wN.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        wN.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        wN.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        wN.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        wN.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    wN.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = wN.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = wN.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        wN.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = wN.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = wN.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        wN.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    wN.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,helpmsg)
                else:
                    wN.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'keybot':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,keymsg)
                else:
                    wN.sendText(msg.to,keymsg)
            elif msg.text.lower() == 'keypro':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,helppro)
                else:
                    wN.sendText(msg.to,helppro)
            elif msg.text.lower() == 'keyself':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,helpself)
                else:
                    wN.sendText(msg.to,helpself)
            elif msg.text.lower() == 'keygrup':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,helpgrup)
                else:
                    wN.sendText(msg.to,helpgrup)
            elif msg.text.lower() == 'keyset':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,helpset)
                else:
                    wN.sendText(msg.to,helpset)
            elif msg.text.lower() == 'keytran':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,helptranslate)
                else:
                    wN.sendText(msg.to,helptranslate)
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                wN.sendText(msg.to, "❂➣Proses.....")
                elapsed_time = time.time() - start
                wN.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text.lower() == '/crash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                wN.sendMessage(msg)
                wN.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                wN.sendMessage(msg)
                
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    b = urllib.quote(a)
                    wN.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    wN.sendText(msg.to, "https://www.facebook.com" + b)
                    wN.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")    
#======================== FOR COMMAND MODE ON STARTING ==========================#
            elif msg.text.lower() == 'mode on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protecion Already On")
                    else:
                        wN.sendText(msg.to,"Protecion Already On")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protecion Already On")
                    else:
                        wN.sendText(msg.to,"Protecion Already On")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already On")
                    else:
                        wN.sendText(msg.to,"Protection Qr already On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already On")
                    else:
                        wN.sendText(msg.to,"Protection Qr already On")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Invite already On")
                    else:
                        wN.sendText(msg.to,"Protection Invite already On")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
#======================== FOR COMMAND MODE OFF STARTING ==========================#
            elif msg.text.lower() == 'mode off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection already Off")
                    else:
                        wN.sendText(msg.to,"Protection already Off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                    else:
                        wN.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already off")
                    else:
                        wN.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already Off")
                    else:
                        wN.sendText(msg.to,"Protection Qr already Off")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wN.sendText(msg.to,"Protection Invite already Off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wN.sendText(msg.to,"Protection Invite already Off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wN.sendText(msg.to,"Protection Cancel already Off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wN.sendText(msg.to,"Protection Cancel already Off")
#========================== FOR COMMAND BOT STARTING =============================#
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        wN.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        wN.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        wN.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        wN.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
            elif "Halo" in msg.text:                                                    
                try:
                    del cctv['point'][msg.to]                                              
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except: pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                wN.sendText(msg.to,"Sider apa kabar,,main yuk 😆😆")            
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    wN.sendText(msg.to, "Cek Sider Off")
                else:
                    wN.sendText(msg.to, "Hihi Belom Di Set")            
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protecion Already On")
                    else:
                        wN.sendText(msg.to,"Protecion Already On")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protecion Already On")
                    else:
                        wN.sendText(msg.to,"Protecion Already On")
            elif msg.text.lower() == 'qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already On")
                    else:
                        wN.sendText(msg.to,"Protection Qr already On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already On")
                    else:
                        wN.sendText(msg.to,"Protection Qr already On")
            elif msg.text.lower() == 'invite on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Invite already On")
                    else:
                        wN.sendText(msg.to,"Protection Invite already On")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
            elif msg.text.lower() == 'autojoin on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        wN.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
            elif msg.text.lower() == 'autojoin off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        wN.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        wN.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection already Off")
                    else:
                        wN.sendText(msg.to,"Protection already Off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                    else:
                        wN.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
            elif msg.text.lower() == 'qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already off")
                    else:
                        wN.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Qr already Off")
                    else:
                        wN.sendText(msg.to,"Protection Qr already Off")
            elif msg.text.lower() == 'invit off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wN.sendText(msg.to,"Protection Invite already Off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wN.sendText(msg.to,"Protection Invite already Off")
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wN.sendText(msg.to,"Protection Cancel already Off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wN.sendText(msg.to,"Protection Cancel already Off")
            elif "Grup cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Grup cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            wN.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            wN.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Nilai tidak benar")
                    else:
                        wN.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'autoleave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        wN.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        wN.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        wN.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        wN.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == '#share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Share set to on")
                    else:
                        wN.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Share set to on")
                    else:
                        wN.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Share set to off")
                    else:
                        wN.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Share set to off")
                    else:
                        wN.sendText(msg.to,"Share already off")
            elif msg.text.lower() == 'status':
                md = """╔═════════════\n"""
                if wait["contact"] == True: md+="╠❂➣Contact:on [✅]\n"
                else: md+="╠❂➣Contact:off [❌]\n"
                if wait["autoJoin"] == True: md+="╠❂➣Auto Join:on [✅]\n"
                else: md +="╠❂➣Auto Join:off [❌]\n"
                if wait["autoCancel"]["off"] == True:md+="╠❂➣Auto cancel:" + str(wait["autoCancel"]["members"]) + "[✅]\n"
                else: md+= "╠❂➣Group cancel:off [❌]\n"
                if wait["leaveRoom"] == True: md+="╠❂➣Auto leave:on [✅]\n"
                else: md+="╠❂➣Auto leave:off [❌]\n"
                if wait["timeline"] == True: md+="╠❂➣Share:on [✅]\n"
                else:md+="╠❂➣Share:off [❌]\n"
                if wait["autoAdd"] == True: md+="╠❂➣Auto add:on [✅]\n"
                else:md+="╠❂➣Auto add:off [❌]\n"
                if wait["protect"] == True: md+="╠❂➣Protect:on [✅]\n"
                else:md+="╠❂➣Protect:off [❌]\n"
                if wait["linkprotect"] == True: md+="╠❂➣Link Protect:on [✅]\n"
                else:md+="╠❂➣Link Protect:off [❌]\n"
                if wait["inviteprotect"] == True: md+="╠❂➣Invitation Protect:on [✅]\n"
                else:md+="╠❂➣Invitation Protect:off [❌]\n"
                if wait["cancelprotect"] == True: md+="╠❂➣Cancel Protect:on [✅]\n"
                else:md+="╠❂➣Cancel Protect:off [❌]\n╚═════════════"
                wN.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN.sendMessage(msg)
             #   wN.sendText(msg.to,'❂➣ Creator yang manis kalem  􀜁􀄯􏿿')
 #           elif msg.text.lower() == 'autoadd on':
 #               if wait["autoAdd"] == False:
  #                  if wait["lang"] == "JP":
 #                       wN.sendText(msg.to,"Auto add set to on")
 #                   else:
  #                      wN.sendText(msg.to,"Auto add already on")
 #               else:
 #                   wait["autoAdd"] = True
 #                   if wait["lang"] == "JP":
 #                       wN.sendText(msg.to,"Auto add set to on")
 #                   else:
  #                      wN.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'autoadd off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Auto add set to off")
                    else:
                        wN.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Auto add set to off")
                    else:
                        wN.sendText(msg.to,"Auto add already off")
            elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                wN.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    wN.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    wN.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    wN.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Aku berada di")
                    else:
                        wN.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Comment Actived")
                    else:
                        wN.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Hal ini sudah off")
                    else:
                        wN.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Off")
                    else:
                        wN.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                wN.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                wN.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                wN.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    wN.sendText(msg.to,"Nothing in the blacklist")
                else:
                    wN.sendText(msg.to,"The following is a blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +wN.getContact(mi_d).displayName + "\n"
                    wN.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    wN.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = wN.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    wN.updateProfile(profile)
                    wN.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    wN.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    wN.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    wN.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    wN.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = wN.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    wN.updateProfile(profile)
                    wN.sendText(msg.to,"Diperbarui")
                else:
                    wN.sendText(msg.to,"Silahkan Aktifkan Jam")
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    wN.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif msg.text in ["Sepi","Panggil"]: 
              if msg.from_ in admin: 
                group = wN.getGroup(msg.to) 
                nama = [contact.mid for contact in group.members] 
                cb = "" 
                cb2 = "" 
                strt = int(0) 
                akh = int(0) 
                for md in nama: 
                    akh = akh + int(5) 
                    cb +="""{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},""" 
                    strt = strt + int(6) 
                    akh = akh + 1 
                    cb2 += "@nrik\n" 
                cb = (cb[:int(len(cb)-1)]) 
                msg.contentType = 0 
                msg.text = cb2 
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'} 
                try: 
                    wN.sendMessage(msg) 
                except Exception as error: 
                    print error   

#========================== FOR COMMAND BOT FINISHED =============================#
            elif "Spam change:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace("Spam change:","")
                wN.sendText(msg.to,"spam changed")

            elif "Spam add:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace("Spam add:","")
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,"spam changed")
                else:
                    wN.sendText(msg.to,"Done")

#==============================================
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = wN.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam") 
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam") 
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam") 
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam") 
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam") 
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(g.mid,"Spam")
                       wN.sendText(msg.to, "Done")
                       print " Spammed !"

#==============================================================================#
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                wN.sendText(msg.to,"Send Contact")
            
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                wN.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                wN.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["#Like:friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                wN.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Done")
                else:
                    wait["#likeOn"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Done")
                else:
                    wait["#likeOn"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Already")
                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wN.sendText(msg.to,"Simi mode On")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wN.sendText(msg.to,"Simi mode Off")
                
            elif msg.text in ["Autoread on","Read:on"]:
                wait['alwayRead'] = True
                wN.sendText(msg.to,"Auto read On")
                
            elif msg.text in ["Autoread off","Read:off"]:
                wait['alwayRead'] = False
                wN.sendText(msg.to,"Auto read Off")
                
            elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                wN.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                wN.sendText(msg.to,"Auto respon tag Off")
            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                wN.sendText(msg.to,"Auto Kick tag ON")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                wN.sendText(msg.to,"Auto Kick tag OFF")
            elif "Time" in msg.text:
              if msg.toType == 2:
                  wN.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif msg.text in ["Sambut on","sambut on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"noтιғ yg joιn on")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"already on")
            elif msg.text in ["Sambut off","sambut off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"noтιғ yg joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif msg.text in ["Pergi on","pergi on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"noтιғ yg leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","pergi off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"noтιғ yg leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif ".bubar99" in msg.text:
				if msg.toType == 2:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace(".bubar99","")
						gs = wN.getGroup(msg.to)
						gs = wN.getGroup(msg.to)
						gs = wN.getGroup(msg.to)
						wN.sendText(msg.to,"Just some casual cleansing ô")
						wN.sendText(msg.to,"Group cleansed.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							wN.sendText(msg.to,"Not found.")
							wN.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[wN,wN,wN]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									wN.sendText(msg.to,"Group cleanse")
									wN.sendText(msg.to,"Group cleanse")
            elif msg.text in ["Salam1"]:
                wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "###Salam3" in msg.text:
              if msg.from_ in owner:
                wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Assalamu'alaikum")
                wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam3","")
                    gs = wN.getGroup(msg.to)
                    wN.sendText(msg.to,"maaf kalo gak sopan")
                    wN.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    wN.sendText(msg.to,"hehehhehe")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin:
                            try:
                                klist=[wN]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                wN.sendText(msg.to,"Nah salamnya jawab sendiri dah")
            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wN.kickoutFromGroup(msg.to,[target])
                       except:
                           wN.sendText(msg.to,"Error")
            
            elif ("Nk " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wN.kickoutFromGroup(msg.to,[target])
                           wN.inviteIntoGroup(msg.to,[target])
                           wN.cancelGroupInvitation(msg.to,[target])
                       except:
                           wN.sendText(msg.to,"Error")
            
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                wN.kickoutFromGroup(msg.to,[midd])
            
            elif 'invite ' in msg.text.lower():
                    key = msg.text[-33:]
                    wN.findAndAddContactsByMid(key)
                    wN.inviteIntoGroup(msg.to, [key])
                    contact = wN.getContact(key)
            
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = wN.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        wN.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Tidak ada undangan")
                        else:
                            wN.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Tidak ada undangan")
                    else:
                        wN.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'link on':
                if msg.toType == 2:
                    group = wN.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    wN.updateGroup(group)
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"URL open")
                    else:
                        wN.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"It can not be used outside the group")
                    else:
                        wN.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'link off':
                if msg.toType == 2:
                    group = wN.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    wN.updateGroup(group)
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"URL close")
                    else:
                        wN.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"It can not be used outside the group")
                    else:
                        wN.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","Gurl"]:
                if msg.toType == 2:
                    g = wN.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        wN.updateGroup(g)
                    gurl = wN.reissueGroupTicket(msg.to)
                    wN.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif "Gcreator" == msg.text:
                try:
                    group = wN.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    wN.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    wN.sendMessage(M)
                    wN.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'invite:gcreator':
                if msg.toType == 2:
                       ginfo = wN.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           wN.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           wN.inviteIntoGroup(msg.to,[gcmid])
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    X = wN.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    wN.updateGroup(X)
            
            elif msg.text.lower() == 'infogrup':        
                    group = wN.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    wN.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                gid = wN.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (wN.getGroup(i).name,i)
                wN.sendText(msg.to,h)
#==============================================================================#
            elif msg.text in ["Glist"]:
                gid = wN.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (wN.getGroup(i).name +" ? ["+str(len(wN.getGroup(i).members))+"]")
                wN.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'gcancel':
                gid = wN.getGroupIdsInvited()
                for i in gid:
                    wN.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    wN.sendText(msg.to,"He declined all invitations")
                         
#            elif "Auto add" in msg.text:
#                thisgroup = wN.getGroups([msg.to])
#                Mids = [contact.mid for contact in thisgroup[0].members]
#                mi_d = Mids[:33]
#                wN.findAndAddContactsByMids(mi_d)
#                wN.sendText(msg.to,"Success Add all")
                    
            elif "@bye" in msg.text:
                if msg.toType == 2:
                    ginfo = wN.getGroup(msg.to)
                    try:
                        wN.leaveGroup(msg.to)
                    except:
                        pass
#==============================================================================#
            elif "sayang" == msg.text.lower():
                 group = wN.getGroup(msg.to)
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
                 #cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 wN.sendText(msg.to,"Ciluk baa...😲😲")
                 wN.sendMessage(cnt)

            elif "cctv on" == msg.text.lower():
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
                         wN.sendText(msg.to,"Setpoint already on")
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
                     wN.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "cctv off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    wN.sendText(msg.to,"Setpoint already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wN.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif msg.text in ["Lihat","Cyduk"]:
                 if msg.toType == 2:
                    print "\nRead aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        wN.sendText(msg.to, "╔═════════════ \n╠❂➣Sider :\n╠═════════════                     %s\n╠\n╠═════════════\n╠❂➣Reader :\n╠═════════════ %s\n╠\n╠═════════════\n╠In the last seen point:\n╠[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
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
                        wN.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                    else:
                        wN.sendText(msg.to, "Ketik [Cctv on] dulu, baru ketik [Toong]")


                    
            elif "intip" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             wN.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = wN.getContacts(chiya)
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
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          wN.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
                    else:
                        wN.sendText(msg.to, "Lurking has not been set.")
                        
            elif msg.text in ["/sayang"]:
                if msg.from_ in admin:
                             group = wN.getGroup(msg.to)
                             nama = [contact.mid for contact in group.members]
                             nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                             if jml <= 100:
                                mention(msg.to, nama)
                             if jml > 100 and jml < 200:
                                for i in range (0, 99):
                                        nm1 += [nama[i]]
                                mention(msg.to, nm1)
                                for j in range (100, len(nama)-1):
                                        nm2 += [nama[j]]
                                mention(msg.to, nm2)
                             if jml > 200 and jml < 300:
                                for i in range (0, 99):
                                        nm1 += [nama[i]]
                                mention(msg.to, nm1)
                                for j in range (100, 199):
                                        nm2 += [nama[j]]
                                mention(msg.to, nm2)
                                for k in range (200, len(nama)-1):
                                        nm3 += [nama[k]]
                                mention(msg.to, nm3)
                             if jml > 300 and jml < 400:
                                for i in range (0, 99):
                                        nm1 += [nama[i]]
                                mention(msg.to, nm1)
                                for j in range (100, 199):
                                        nm2 += [nama[j]]
                                mention(msg.to, nm2)
                                for k in range (200, 299):
                                        nm3 += [nama[k]]
                                mention(msg.to, nm3)
                                for l in range (300, len(nama)-1):
                                    nm4 += [nama[l]]
                                mention(msg.to, nm4)
                             cnt = Message()
                             #cnt.text = "Hasil Tag : " +str(jml)
                             cnt.to = msg.to
                             wN.sendText(msg.to,"Ciluk baa...😲😲")
                             wN.sendMessage(cnt) 
  
            elif "Gbroadcast: " in msg.text:
                bc = msg.text.replace("Gbroadcast: ","")
                gid = wN.getGroupIdsJoined()
                for i in gid:
                    wN.sendText(i, bc)
                    
            elif "Cbroadcast: " in msg.text:
                bc = msg.text.replace("Cbroadcast: ","")
                gid = wN.getAllContactIds()
                for i in gid:
                    wN.sendText(i, bc)
            elif "megs " in msg.text: 
              if msg.from_ in owner: 
                gName = msg.text.replace("megs ","") 
                ap = wN.getGroups([msg.to]) 
                semua = [contact.mid for contact in ap[0].members]
                nya = ap[0].members 
                for a in nya: 
                    Mi_d = str(a.mid) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua)
            elif "#megs " in msg.text: 
              if msg.from_ in owner: 
                gName = msg.text.replace("#megs ","") 
                ap = wN.getGroups([msg.to]) 
                semua = findAndAddContactsByMid(Mi_d) 
                nya = ap[0].members 
                for a in nya: 
                    Mi_d = str(a.mid) 
                    klis=[wN] 
                    team=random.choice(klis) 
                    wN.findAndAddContactsByMid(Mi_d) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    wN.createGroup(gName, semua) 
                    team.findAndAddContactsByMid(Mi_d) 
                    team.createGroup(gName, semua) 
                    team.createGroup(gName, semua) 
                    team.createGroup(gName, semua) 
                    team.createGroup(gName, semua) 
                    team.createGroup(gName, semua) 
                    team.createGroup(gName, semua)   
                    
            elif "youtube " in msg.text.lower(): 
                if msg.from_ in admin: 
                   query = msg.text.split(" ") 
                   try: 
                       if len(query) == 3: 
                           isi = yt(query[2]) 
                           hasil = isi[int(query[1])-1] 
                           wN.sendText(msg.to, hasil) 
                       else: 
                           isi = yt(query[1]) 
                           wN.sendText(msg.to, isi[0]) 
                   except Exception as e: 
                       wN.sendText(msg.to, str(e))
   
            elif msg.text in ["Reject invite"]: 
                    gid = wN.getGroupIdsInvited() 
                    for i in gid: 
                        wN.rejectGroupInvitation(i) 
                    if wait["lang"] == "JP": 
                        wN.sendText(msg.to,"All invitations have been rejected") 
                    else:
                        wN.sendText(msg.to,"Done")        
            elif (msg.text == 'Tagall'): 
                  a = wN.getGroup(msg.to) 
                  b = [] 
                  for i in a.members: 
                      b.append('@'+i.displayName) 
                  c = '\n'.join(b) 
                  wN.sendText(msg.to,c) 
            #elif msg.text in ["Salam1"]: 
              #  ki.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ") 
             #   kk.sendText(msg.to,"Assalamu'alaikum") 
            #elif msg.text in ["Salam2"]: 
                #ki.sendText(msg.to,"وَعَلَيْكُمْ الَرَحمَُ اللهِوَبَرَكَاتُهُ" )
             #kk.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                wN.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,"spam changed")
                else:
                    wN.sendText(msg.to,"Done")
    
            
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = wN.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           wN.sendText(msg.to, teks)
                    else:
                       wN.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        wN.sendText(msg.to, tulisan)
                    else:
                        wN.sendText(msg.to, "Out Of Range!")
                        
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        wN.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        wN.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        wN.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        wN.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            wN.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+wN.getContact(mi_d).displayName + "\n"
                            wN.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                wN.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                wN.sendText(msg.to,"Mimic change to target")
                            else:
                                wN.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        wN.sendText(msg.to,"Reply Message on")
                    else:
                        wN.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        wN.sendText(msg.to,"Reply Message off")
                    else:
                        wN.sendText(msg.to,"Sudah off")
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                wN.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                wN.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                wN.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                wN.sendVideoWithURL(msg.to,wait["pap"])
            elif "TL:" in msg.text:
              if msg.toType == 2:
                tl_text = msg.text.replace("TL:","")
                wN.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+wN.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==============================================================================#
            elif msg.text.lower() == 'mymid':
                wN.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                wN.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+wN.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = wN.getProfile()
                    profile.displayName = string
                    wN.updateProfile(profile)
                    wN.sendText(msg.to,"Changed " + string + "")
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = wN.getProfile()
                    profile.statusMessage = string
                    wN.updateProfile(profile)
                    wN.sendText(msg.to,"Changed " + string)
            elif msg.text in ["Myname"]:
                    h = wN.getContact(mid)
                    wN.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = wN.getContact(mid)
                    wN.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = wN.getContact(mid)
                    wN.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = wN.getContact(mid)
                    wN.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = wN.getContact(mid)
                    wN.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = wN.getContact(mid)
                    cu = wN.channel.getCover(mid)          
                    path = str(cu)
                    wN.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = wN.getContact(mid)
                    cu = wN.channel.getCover(mid)          
                    path = str(cu)
                    wN.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = wN.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        wN.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = wN.getContact(key1)
                cu = wN.channel.getCover(key1)
                try:
                    wN.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    wN.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = wN.getContact(key1)
                cu = wN.channel.getCover(key1)
                try:
                    wN.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    wN.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = wN.getContact(key1)
                cu = wN.channel.getCover(key1)
                try:
                    wN.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    wN.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = wN.getContact(key1)
                cu = wN.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    wN.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    wN.sendText(msg.to,"Profile Picture " + contact.displayName)
                    wN.sendImageWithURL(msg.to,image)
                    wN.sendText(msg.to,"Cover " + contact.displayName)
                    wN.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = wN.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                wN.sendMessage(msg)
            elif "Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = wN.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    wN.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = wN.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            wN.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = wN.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    wN.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = wN.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            wN.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = wN.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    wN.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = wN.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            wN.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = wN.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    wN.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = wN.getContact(target)
                            cu = wN.channel.getCover(target)          
                            path = str(cu)
                            wN.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = wN.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    wN.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = wN.getContact(target)
                            cu = wN.channel.getCover(target)          
                            path = str(cu)
                            wN.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                group = wN.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                wN.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                group = wN.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                wN.sendText(msg.to,path)
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = wN.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       wN.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               wN.CloneContactProfile(target)
                               wN.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:
                try:
                    wN.updateDisplayPicture(backup.pictureStatus)
                    wN.updateProfile(backup)
                    wN.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    wN.sendText(msg.to, str(e))
#==============================================================================#
            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                wN.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
                    
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            
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
                wN.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
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
                wN.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
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
                wN.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
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
                wN.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
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
                wN.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
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
                wN.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
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
                wN.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
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
                wN.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
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
                wN.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
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
                wN.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
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
                wN.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = wN.getGroup(msg.to)
                wN.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
               # wN.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                wN.sendAudio(msg.to,'tts.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  wN.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  wN.sendAudio(msg.to,'tts.mp3')
            
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        wN.sendVideoWithURL(msg.to, ght)
                    except:
                        wN.sendText(msg.to, "Could not find it")
            
            elif "/Youtube " in msg.text:
                    query = msg.text.replace("Youtube ","")
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
                        wN.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
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
                        wN.sendText(msg.to, hasil)
                except Exception as wak:
                        wN.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      wN.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              wN.sendText(msg.to, pesan)
                          except Exception as e:
                              wN.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
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
                        wN.sendText(msg.to, hasil)
                        wN.sendText(msg.to, "Please Wait for audio...")
                        wN.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        wN.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    wN.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
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
                        wN.sendImageWithURL(msg.to, profileIG)
                        wN.sendText(msg.to, str(text))
                    except Exception as e:
                        wN.sendText(msg.to, str(e))

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                wN.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Time","Waktu"]:
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
                wN.sendText(msg.to, rst)
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif "Restart" in msg.text:
                    print "[Command]Restart"
                    try:
                        wN.sendText(msg.to,"Restarting...")
                        wN.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        wN.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
                
            elif msg.text.lower() == 'run time':
                eltime = time.time() - mulai
                van = "Bot has been active "+waktu(eltime)
                wN.sendText(msg.to,van)

        
#================================ CBW SCRIPT STARTED ==============================================#
            elif "google " in msg.text:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    wN.sendText(msg.to,"Sedang Mencari om...")
                    wN.sendText(msg.to, "https://www.google.com/" + b)
                    wN.sendText(msg.to,"Ketemu om ^")

            elif cms(msg.text,["/creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN.sendMessage(msg)

            elif "friendpp: " in msg.text:
              if msg.from_ in admin:
                suf = msg.text.replace('friendpp: ','')
                gid = wN.getAllContactIds()
                for i in gid:
                    h = wN.getContact(i).displayName
                    gna = wN.getContact(i)
                    if h == suf:
                        wN.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)

            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                wN.sendMessage(msg)
                contact = wN.getContact(saya)
                cu = wN.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    wN.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    wN.sendText(msg.to,"Profile Picture " + contact.displayName)
                    wN.sendImageWithURL(msg.to,image)
                    wN.sendText(msg.to,"Cover " + contact.displayName)
                    wN.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = wN.getGroupIdsJoined()
                for i in gid:
                    h = wN.getGroup(i).id
                    group = wN.getGroup(i)
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
                            wN.sendText(msg.to,md)
                            wN.sendMessage(msg)
                            wN.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist"]:    
                contactlist = wN.getAllContactIds()
                kontak = wN.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = wN.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                wN.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = wN.getAllContactIds()
                for i in gid:
                    h = wN.getContact(i).displayName
                    contact = wN.getContact(i)
                    cu = wN.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        wN.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        wN.sendText(msg.to,"Profile Picture " + contact.displayName)
                        wN.sendImageWithURL(msg.to,image)
                        wN.sendText(msg.to,"Cover " + contact.displayName)
                        wN.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = wN.getAllContactIds()
                for i in gid:
                    h = wN.getContact(i).displayName
                    gna = wN.getContact(i)
                    if h == saya:
                        wN.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = wN.getAllContactIds()
                kontak = wN.getContacts(gruplist)
                num=1
                msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = wN.getBlockedContactIds()
                kontak = wN.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:  
                gruplist = wN.getGroupIdsJoined()
                kontak = wN.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = wN.getGroupIdsJoined()
                kontak = wN.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = wN.getGroupIdsJoined()
                for i in gid:
                    h = wN.getGroup(i).name
                    gna = wN.getGroup(i)
                    if h == saya:
                        wN.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = wN.getGroup(msg.to)
                wN.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = wN.getGroup(msg.to)
                wN.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = wN.getGroupIdsJoined()
                for i in gid:
                    h = wN.getGroup(i).name
                    group = wN.getGroup(i)
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
                            wN.sendText(msg.to,md)
                            wN.sendMessage(msg)
                            wN.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"

            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = wN.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        wN.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "crashkontak @" in msg.text:
                _name = msg.text.replace("crashkontak @","")
                _nametarget = _name.rstrip(' ')
                gs = wN.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                            wN.sendMessage(g.mid,msg.to + str(msg))
                            wN.sendText(g.mid, "hai")
                            wN.sendText(g.mid, "salken")
                            wN.sendText(msg.to, "Done")
                            print " Spammed crash !"

            elif "playstore " in msg.text.lower():
                    tob = msg.text.lower().replace("playstore ","")
                    wN.sendText(msg.to,"Sedang Mencari boss...")
                    wN.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    wN.sendText(msg.to,"Ketemu boss ^")
                    
            elif 'wiki ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wiki ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    wN.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                            pesan+=wikipedia.page(wiki).url
                            wN.sendText(msg.to, pesan)
                        except Exception as e:
                            wN.sendText(msg.to, str(e))    
                            
            elif "say " in msg.text.lower():
                say = msg.text.lower().replace("say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                wN.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text in ["spam gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg) 
                wN.sendMessage(msg)
                wN.sendMessage(msg) 
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
               
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = wN.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       wN.findAndAddContactsByMid(gCreator)
                       wN.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in ["Gcreator:kick"]:
	           if msg.from_ in admin:
                    ginfo = wN.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       wN.findAndAddContactsByMid(gCreator)
                       wN.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
                   
            elif 'lirik ' in msg.text.lower():
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
                        wN.sendText(msg.to, hasil)
                except Exception as wak:
                        wN.sendText(msg.to, str(wak))       
                   
            elif "Getcover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getcover @","")
                _nametarget = _name.rstrip('  ')
                gs = wN.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = wN.getContact(target)
                            cu = wN.channel.getCover(target)
                            path = str(cu)
                            wN.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
                
            elif "idline: " in msg.text:
                msgg = msg.text.replace('idline: ','')
                conn = wN.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    wN.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    wN.sendMessage(msg)
                        
            elif "reinvite" in msg.text.split():
                if msg.toType == 2:
                    group = wN.getGroup(msg.to)
                    if group.invitee is not None:
                        try:
                            grCans = [contact.mid for contact in group.invitee]
                            wN.findAndAddContactByMid(msg.to, grCans)
                            wN.cancelGroupInvitation(msg.to, grCans)
                            wN.inviteIntoGroup(msg.to, grCans)
                        except Exception as error:
                            print error
                    else:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"No Invited")
                        else:
                            wN.sendText(msg.to,"Error")
                else:
                    pass
                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                wN.sendText(msg.to,van)
                
            elif msg.text in ["Restart"]:
                wN.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"
                
            elif msg.text in ["time"]:
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
                client.sendText(msg.to, rst)
                
            elif "image " in msg.text:
                search = msg.text.replace("image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    wN.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif 'instagram ' in msg.text.lower():
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
                    wN.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    wN.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	wN.sendText(msg.to, str(njer))    
                	
            elif msg.text in ["#Attack"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                wN.sendMessage(msg)
                
            elif msg.text.lower() == '###':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                wN.sendMessage(msg)    
#=================================CBW SCRIPT FINISHED =============================================#
            
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = wN.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                wN.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                wN.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = wN.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                wN.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                wN.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = wN.getGroup(msg.to)
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
                                    wN.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    wN.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = wN.getGroup(msg.to)
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
                                    wN.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    wN.sendText(msg.to,_name + " Not In Blacklist")
            elif msg.text in ["Clear"]:
                wait["blacklist"] = {}
                wN.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                wN.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                wN.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    wN.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    wN.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="*Blacklist*"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, wN.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    wN.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    wN.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    wN.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = wN.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        wN.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = wN.getGroup(msg.to)
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
                    wN.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.toType == 2:
                    group = wN.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        wN.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            wN.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass       
#==============================================#
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        wN.kickoutFromGroup(op.param1,[op.param2])
                        G = wN.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        wN.updateGroup(G)
                    except:
                        try:
                            wN.kickoutFromGroup(op.param1,[op.param2])
                            G = wN.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            wN.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    wN.kickoutFromGroup(op.param1,[op.param2])
                    wN.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    wN.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            wN.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    wN.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = wN.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN.updateGroup(G)
                    wN.kickoutFromGroup(op.param1,[op.param2])
 #       if op.type == 5:
 #           if wait["autoAdd"] == True:
  #              if (wait["message"] in [""," ","\n",None]):
 #                   pass
 #               else:
  #                  wN.sendText(op.param1,str(wait["message"]))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = wN.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN.kickoutFromGroup(op.param1,[op.param3])
                    wN.updateGroup(G)
        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = wN.getGroup(op.param1)
               wN.sendText(op.param1, "╔═════════════\n║HALO kak Selamat Datang Di  " + str(ginfo.name) + "jangan lupa cek NOTE ya kak semua info ada di note & Semangat Kak 😍😙==========🙋🐉")
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc"] == True:
               if op.param2 in Bots:
                   return
               G = wN.getGroup(op.param1)
               h = wN.getContact(op.param2)
               wN.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                wN.sendText(op.param1, "╔═════════════\n║Baper Tuh Orang :v \n║Semoga Bahagia ya,,GOODBYE 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
               if op.param2 in Bots:
                   return
               G = wN.getGroup(op.param1)
               h = wN.getContact(op.param2)
               wN.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
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
            
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = wN.getContact(op.param2).displayName
                            Name = wN.getContact(op.param2).displayName
                            Name = wN.getContact(op.param2).displayName
                            Name = wN.getContact(op.param2).displayName
                            Name = wN.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih kak 😁. . .\nSini gabung Chat Kek 😉")
                                    else:
                                        random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nihh Betah Banget ngintip Kak 😏. . .\nDasar jones 😆😂😛")
                                else:
                                    random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Ngintip Aja???😆😆\nCiyeee Sijones ,,,lagi intipin aku yaa 😋 😝kkkk.  ")
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass    
     
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

#def autolike():
#    count = 1
 #   while True:
  #      try:
 #          for posts in wN.activity(1)["result"]["posts"]:
 #            if posts["postInfo"]["liked"] is False:
 #               if wait["likeOn"] == True:
 #                  wN.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   print "Like"
 #                  if wait["commentOn"] == True:
#                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
 #                        pass
#                      else:
 #                         wN.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#        except:
#            count += 1
#            if(count == 50):
#                sys.exit(0)
#            else:
 #               pass
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

#def likefriend():
#    for zx in range(0,20):
#      hasil = wN.activity(limit=20)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
 #         wN.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          wN.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚🐉 tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt 🐉º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by CBW ⭐👈 »»» http://line.me/ti/p/~CBWsthea «««")
#          print "Like"
#        except:
#          pass
#      else:
 #         print "Already Liked Om"
#time.sleep(0.60)

#def likeme():
#    for zx in range(0,20):
#        hasil = wN.activity(limit=20)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
 #               try:
 #                   wN.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
 #                   wN.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚🐉 tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt 🐉º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by CBW ⭐👈 »»» http://line.me/ti/p/~CBWsthea «««")
 #                   print "Like"
 #               except:
 #                   pass
 #           else:
 #               print "Status Sudah di Like Om"


while True:
    try:
        Ops = wN.fetchOps(wN.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(wN.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            wN.Poll.rev = max(wN.Poll.rev, Op.revision)
            bot(Op)
