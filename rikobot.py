# -*- coding: utf-8 -*-

import CBW
from CBW.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

wN = CBW.LINE()
wN.login(token="Ep41bukEnqK4mo1APUR6.8v9J1XRqfIW/ErZtXU+kLG.ToDkrNPyjG7LdJoO5kmS1B1/YVsQAj+CU2arRo6WYao=")
wN.loginResult()

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ Login Success Boss\n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""╔═════════════════
╠❂͜͡➣ ❁Private Command❁ 
╠═════════════════
╠❂͜͡➣[Me]
╠❂͜͡➣[Myname: ]
╠❂͜͡➣[Mybio: ]
╠❂͜͡➣[Mybio]
╠❂͜͡➣[Mypict]
╠❂͜͡➣[Mycover]
╠❂͜͡➣[Mycopy @]
╠❂͜͡➣[Mybackup]
╠❂͜͡➣[Getgrup image]
╠❂͜͡➣[Speed Response]
╠❂͜͡➣[Getmid @]
╠❂͜͡➣[Getprofile @]
╠❂͜͡➣[Getcontact @]
╠❂͜͡➣[Getinfo @]
╠❂͜͡➣[Getname @]
╠❂͜͡➣[Getbio @]
╠❂͜͡➣[Getpict @]
╠❂͜͡➣[Getcover @]
╠❂͜͡➣[Mention]
╠❂͜͡➣[Lurk on/off]
╠❂͜͡➣[Lurkers]
╠❂͜͡➣[Mimic on/off]
╠❂͜͡➣[Micadd @]
╠❂͜͡➣[Micdel @]
╠═════════════════
╠❂͜͡➣ ❁Command Group❁ 
╠═════════════════
╠❂͜͡➣[Link on/off]
╠❂͜͡➣[Url/Gurl]
╠❂͜͡➣[Cancel]
╠❂͜͡➣[Gcreator]
╠❂͜͡➣[Kick @]
╠❂͜͡➣[Ulti @]
╠❂͜͡➣[Sentil @]
╠❂͜͡➣[Dj @]
╠❂͜͡➣[Cancel]
╠❂͜͡➣[Gname: ]
╠❂͜͡➣[Gbroadcast: ]
╠❂͜͡➣[Cbroadcast: ]
╠❂͜͡➣[Infogrup]
╠❂͜͡➣[Gruplist]
╠❂͜͡➣[Link bokep]
╠❂͜͡➣[Friendlist]
╠❂͜͡➣[Blocklist]
╠❂͜͡➣[Ban @]
╠❂͜͡➣[Unban @]
╠❂͜͡➣[wNearban]
╠❂͜͡➣[Banlist]
╠❂͜͡➣[Contactban]
╠❂͜͡➣[Midban]
╠❂͜͡➣[Midban]
╠❂͜͡➣[Nuke]
╠❂͜͡➣[Talkban]
╠❂͜͡➣[Takol]
╠❂͜͡➣[Takel]
╠❂͜͡➣[Talklist]
╠═════════════════
╠❂͜͡➣ wN_CBW
╚═════════════════"""

myhelp ="""╔═════════════════
╠❂͜͡➣ ❁My Setting❁ 
╠═════════════════
╠❂͜͡➣[Contact on/off]
╠❂͜͡➣[Autojoin on/off]
╠❂͜͡➣[Autoleave on/off]
╠❂͜͡➣[Autoadd on/off]
╠❂͜͡➣[Sleep on/off]
╠❂͜͡➣[Read on/off]
╠❂͜͡➣[Simi on/off]
╠❂͜͡➣[Sensi on/off]
╠❂͜͡➣[Autocrash on/off]
╠❂͜͡➣[Crashpc on/off]
╠❂͜͡➣[Crashtag on/off]
╠❂͜͡➣[Crashkick on/off]
╠❂͜͡➣[Pc on/off]
╠❂͜͡➣[Dm on/off]
╠❂͜͡➣[Pergi on/off]
╠❂͜͡➣[Welcome on/off]
╠═════════════════
╠❂͜͡➣ ❁My Protection❁ 
╠═════════════════
╠❂͜͡➣[Protect on/off]
╠❂͜͡➣[High on/off]
╠❂͜͡➣[Qr on/off]
╠❂͜͡➣[Invit on/off]
╠❂͜͡➣[Cancel on/off]
╠❂͜͡➣[Talkban on/off]
╠═════════════════
╠❂͜͡➣ ❁My Media❁ 
╠═════════════════
╠❂͜͡➣[Apakah]
╠❂͜͡➣[Checkdate]
╠❂͜͡➣[Cekig]
╠❂͜͡➣[Kapan]
╠❂͜͡➣[Lirik]
╠❂͜͡➣[Music]
╠❂͜͡➣[Profileig]
╠❂͜͡➣[Time]
╠❂͜͡➣[Runtime]
╠❂͜͡➣[tr-id]
╠❂͜͡➣[tr-en]
╠❂͜͡➣[tr-jp]
╠❂͜͡➣[tr-ko]
╠❂͜͡➣[say-id]
╠❂͜͡➣[say-en]
╠❂͜͡➣[say-jp]
╠❂͜͡➣[say-ko]
╠❂͜͡➣[Youtube]
╠═════════════════
╠❂͜͡➣ ❁
╠❂͜͡➣ OWNER
╚═════════════════"""

mulai = time.time()

mid = wN.getProfile().mid
Bots=[mid,"uf15f63d71ad0162c3e791cd3c6efca96"]
admin=["uf15f63d71ad0162c3e791cd3c6efca96","uebbf59db5b293de1c2c1e75daab296db"]
owner=["uf15f63d71ad0162c3e791cd3c6efca96","uebbf59db5b293de1c2c1e75daab296db"]

wait = {
    "likeOn":False,
    'Bot':False,
    "alwayRead":False,
    "tagVN":False,
    "detectMention":False,
    'detectMention3':False,
    'potoMention':False,
    "kickMention":False,
    "tagMention":False, 
    "blockMention":False,
    "steal":False,
    "talkban":{},
    'pap':{},
    'invite':{},
    'gift':{},
    'copy':{},    
    "spam":{},
    "Sider":{},
    "blacklist":{},
    "talkblacklist":{},
    "talkwblacklist":False,
    "talkdblacklist":False,
    'contact':False,
    'autoJoin':True,
    'sticker':False,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Cie Ngeadd",
    "lang":"JP",
    "comment":"",
    "AgResp":"「 - Riko Bots Was Here!! -」",
    "TagRespon":"\n\n\n\nMohon Maaf Riko Sedang Sibuk, Tolong Untuk Tidak Tag Riko Di Grup Untuk Sementara Waktu, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Riko Nanti, Terimakasih.",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "wNock":False,
    "cNames":"",
    "cNames":"",
    "respondpc":False,    
    "crashpc":False, 
    "crashTag":False, 
    "crashKick":False, 
    "autoCrash":False, 
    "Sambutan":False,
    "Lv":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect": False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
    "detectAll":False, 
    "me":"me",
    "userAgent": [
		"Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
		"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	],
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

res = {
    'num':{},
    'us':{},
    'au':{},
    }

dangerMessage = ["cleanse","group cleansed.","salam3",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke"]

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
    os.exewN(python, python, * sys.argv)
    
def sendMessageWithMention(self, to, text='', dataMid=[]):
        arr = []
        list_text=''
        if '[list]' in text.lower():
            i=0
            for l in dataMid:
                list_text+='\n@[list-'+str(i)+']'
                i=i+1
            text=text.replace('[list]', list_text)
        elif '[list-' in text.lower():
            text=text
        else:
            i=0
            for l in dataMid:
                list_text+=' @[list-'+str(i)+']'
                i=i+1
            text=text+list_text
        i=0
        for l in dataMid:
            mid=l
            name='@[list-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int( ln_text.index(name) )
                line_e=(int(line_s)+int( len(name) ))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
        return
        wN.sendMessage(to, text, contentMetadata)
    
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
        start_line = s.find('"wNass="rg_meta"')
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

def upload_tempimage(wNient):
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
    image = wNient.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._wNient.sendMessage(M).id
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
        r = self._wNient.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
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

def sendAudio(self, to_, path):
      M = Message(to=to_, text=None, contentType = 3)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self.Talk.wNient.sendMessage(0,M)
      M_id = M2.id
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
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
          raise Exception('Upload audio failure.')
      return True
    
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
         wN.sendMessage(msg)
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
       wN.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    years, month = divmod(month,12)
    return '%2d Month ♬\n%2d Days ♬\n%02d Hours ♬\n%02d Minutes ♬\n%02d Seconds ♬' % (month, days, hours, mins, secs)      

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        wN.sendText(op.param1, wN.getContact(op.param2).displayName + " Jangan kick sembarangan 😑")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

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
        if op.type == 13:
            if mid in op.param3:
                G = wN.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            wN.rejectGroupInvitation(op.param1)
                        else:
                            wN.acceptGroupInvitation(op.param1)
                            wN.sendText(op.param1,"Thnx For Invite Me Your Group 😊")
                    else:
                        wN.acceptGroupInvitation(op.param1)
                        wN.sendText(op.param1,"Thnx For Invite Me Your Group 😊")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        wN.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    wN.cancelGroupInvitation(op.param1, matched_list)        
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 5:
            if wait["autoAdd"] == True: 
                wN.findAndAddContactsByMid(op.param1)
                xname = wN.getContact(op.param1).displayName
                wN.sendText(op.param1, "Halo " + xname + " ,terimakasih telah menambahkan saya sebagai teman :3")
        if op.type == 22:
            if wait["leaveRoom"] == True:
                wN.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                wN.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message            
            if msg.text in ["Mayhem","mayhem","Nuke","nuke","Greet","greet","Ratakan","ratakan","Ready op","ready op","wNeanse","wNeanse","Kickall","kickall",".kickall"]:
              dia = ("Tercyduck Kamu Yah Mau Anu 😆","Mau Ngapain? ┌П┐(◣_◢)┌П┐ ")
              ket = random.choice(dia)
              wN.sendText(msg.to,ket)
              wN.kickoutFromGroup(msg.to,[msg.from_])
              wN.sendText(msg.to,"Mampus Lu Kekick 😎")                            
        if op.type == 26:
            msg = op.message            
            if msg.text in ["Crash","crash"]:
              dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash","Kamu asu ngecrash terus!")
              ket = random.choice(dia)
              wN.sendText(msg.to,ket)
              wN.kickoutFromGroup(msg.to,[msg.from_])
              wN.sendText(msg.to,"Mampus Lu Kekick 😎")                            
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
                                wN.sendText(msg.to, "[SimiSimi] " + data['result']['response'].encode('utf-8'))
                                
            if wait["respondpc"] == True:
                if msg.toType == 0:                	
                    wN.sendChatChecked(msg.from_,msg.id)
                    contact = wN.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Halo 「" + cName + "」\nMohon Maaf Riko Sedang Sibuk, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Riko Nanti, Terimakasih."]
                    agler = "" + random.choice(balas)                    
                    wN.sendText(msg.from_,agler) ## "Halo", displayName + "\n\nMohon Riko Sedang Sibuk, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Riko Nanti, Terimakasih.")                                        

            if wait["crashpc"] == True:
                if msg.toType == 0:
                    wN.sendChatChecked(msg.from_,msg.id)
                    wN.sendText(msg.from_,"「Dont Chat Me!! 」")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc4670540ac3b113403a9667df0b09df3',"}                	
                    wN.sendMessage(msg)  
                    
            if "@"+wN.getProfile().displayName in msg.text:
                 if wait["tagVN"] == True:
                  aud = ("LINE_A20171224_221320477.m4a")
                  wN.sendAudio(msg.to, aud)                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["tagMention"] == True:
                     contact = wN.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Halo 「" + cName + "」\nMohon Maaf Riko Sedang Sibuk, Tolong Untuk Tidak Tag Riko Di Grup Untuk Sementara Waktu, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Riko Nanti, Terimakasih."]
                     agler = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:                                            
                                  wN.sendText(msg.from_,agler)    
                                  msg.contentType = 7
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "2754644",
                                                       "STKPKGID": "1066653",
                                                       "STKVER": "1" }
                                  wN.sendMessage(msg)
                                  pass
                                  break    
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     names = re.findall(r'@(\w+)',msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                         if mention['M'] in admin:
                             xname = wN.getContact(msg.from_).displayName
                             xlen = str(len(xname)+1)
                             msg.to = msg.from_
                             msg.contentType = 0
                             balas = "@"+xname+ wait["TagRespon"]
                             tmbahan = balas
                             msg.text = tmbahan
                             msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                             wN.sendMessage(msg)
                             msg.contentType = 7
                             msg.text = None
                             msg.contentMetadata = {
                                                  "STKID": "2754644",
                                                  "STKPKGID": "1066653",
                                                  "STKVER": "1" }
                             wN.sendMessage(msg)
                             pass
                             break      
                             
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = wN.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["woy " + cName + ", Dasar Jones Ngetag Mulu!"]
                    balas1 = "Ini Foto Sii Jones Yang Suka Ngetag. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN.sendText(msg.to,ret_)
                                  wN.sendText(msg.to,balas1)
                                  wN.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "22987194",
                                                       "STKPKGID": "1711359",
                                                       "STKVER": "1" }
                                  wN.sendMessage(msg)                                
                                  break      
                    
#        if 'MENTION' in msg.contentMetadata.keys()!=None:
#              if wait["tagMention"] == True:
#                 names = re.findall(r'@(\w+)',msg.text)
#                 mention = ast.literal_eval(msg.contentMetadata['MENTION'])
#                 mentionees = mention['MENTIONEES']
#                 for mention in mentionees:
#                     if mention['M'] in admin:
#                         xname = wN.getContact(msg.from_).displayName
#                         xlen = str(len(xname)+1)
#                         msg.to = msg.from_
#                         msg.contentType = 0
#                         balas = "Halo「@"+xname+ "」\nMohon Maaf Riko Sedang Sibuk, Tolong Untuk Tidak Tag Riko Di Grup Untuk Sementara Waktu, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Riko Nanti, Terimakasih."
#                         tmbahan = balas
#                         msg.text = tmbahan
#                         msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
#                         wN.sendMessage(msg)
#                         pass
#                         break
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["crashTag"] == True:
                     contact = wN.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Bacot",cName + "┌П┐(◣_◢)┌П┐"]
                     ret_ = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN.sendText(msg.to,ret_)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "uc4670540ac3b113403a9667df0b09df3',"}                	
                                  wN.sendMessage(msg)                                       
                                  break                                              
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = wN.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["[Auto Respon] Dont Tag Me!! Im Busy ",cName + " Ngapain Ngetag?, ",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja ", cName + " Kenapa Tag saya? ","┌П┐(◣_◢)┌П┐ " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?",cName + " ┌П┐(◣_◢)┌П┐"]
                     ret_ = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN.sendText(msg.to,ret_)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "uc4670540ac3b113403a9667df0b09df3',"}                	
                                  wN.sendMessage(msg)                                                                                      
                                  wN.kickoutFromGroup(msg.to,[msg.from_])
                                  break
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
              if wait["blockMention"] == True:
                    contact = wN.getContact(msg.from_)
                    cName = contact.displayName
                    tname = wN.getGroup(msg.to)
                    tname.name = tname.name
                    balas = ["Dont tag me, im busy",cName + " ada apa ngetag?",cName + " PC AJA","tersummon-_-"]
                    ret_ = "" + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN.sendText(msg.to,ret_ +"\n[GNAME]" +str(tname.name))
                                  
        if op.type == 25:
            msg = op.message
            
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                wN.sendText(msg.to,"Bot Sudah On Kembali.")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
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
                                 wN.sendText(msg.to,"Telah Menginvite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      wN.sendText(msg.to,"Limit invite")
                                      wait['invite'] = False
                                      break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = wN.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                wN.findAndAddContactsByMid(target)
                                contact = wN.getContact(target)
                                cu = wN.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                wN.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                wN.sendText(msg.to,"Profile Picture " + contact.displayName)
                                wN.sendImageWithURL(msg.to,image)
                                wN.sendText(msg.to,"Cover " + contact.displayName)
                                wN.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                    
            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = wN.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                wN.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                wN.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break
                                     
            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = wN.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        wN.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                wN.wNoneContactProfile(target)
                                wN.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break
                                   
            if msg.contentType == 14:
                wN.sendText(msg.to,"Filenya auto download")
                               
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    wN.sendChatChecked(msg.from_,msg.id)
                else:
                    wN.sendChatChecked(msg.to,msg.id)
                    
            if wait["autoCrash"] == True:
                if msg.toType == 0:
                    wN.sendChatChecked(msg.from_,msg.id)      
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc4670540ac3b113403a9667df0b09df3',"}                	
                    wN.sendMessage(msg)                    
                   
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
#taruh di sebelum elif msg.text is None
            elif msg.contentType == 7: # <-- elif atau if tergantung posisinya di awal apa ditengah
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    wN.sendText(msg.to, filler)
                else:
                    pass
                    
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,helpmsg + datetime.today().strftime('%H:%M:%S'))
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    wN.sendMessage(msg)
                else:
                    wN.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'my help':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,myhelp + datetime.today().strftime('%H:%M:%S'))
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    wN.sendMessage(msg)
                else:
                    wN.sendText(msg.to,myhelp)            
#----------------ABOUT SECTION FINISH-----#
            elif msg.text in ["dich"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "817762",
                                     "STKPKGID": "1018582",
                                     "STKVER": "1" }
                wN.sendMessage(msg)
            elif "-_-" in msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "2754644",
                                     "STKPKGID": "1066653",
                                     "STKVER": "1" }
                wN.sendMessage(msg)
            elif msg.text in ["madtah","Mastah"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15878340",
                                     "STKPKGID": "1412505",
                                     "STKVER": "1" }
                wN.sendMessage(msg)
            elif msg.text in ["wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "17225910",
                                     "STKPKGID": "1456919",
                                     "STKVER": "1" }
                wN.sendMessage(msg)
            elif msg.text in ["kerad"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "26911496",
                                     "STKPKGID": "1869016",
                                     "STKVER": "1" }
                wN.sendMessage(msg)
            elif "kacang" in msg.text:
            	peanut = ("https://cdn.pixabay.com/photo/2010/12/13/09/51/peanut-1750_960_720.jpg")
                wN.sendImageWithURL(msg.to,peanut)
#==============================================================================#              
            elif "Tagmid: " in msg.text:
                    mid_ = msg.text.replace("Tagmid: ","")
		    for eue in mid_:
			    xname = wN.getContact(eue).displayName
			    xlen = str(len(xname)+1)
			    msg.contentType = 0
			    msg.text = "@"+xname+ ""
			    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid_)+'}]}','EMTVER':'4'}
			    wN.sendMessage(msg)
#==============================================================================#              
            elif msg.text in ["Speed","Sp","speed","sp"]:
                start = time.time()
                wN.sendText(msg.to, "「Benchmarking..」")
                elapsed_time = time.time() - start
                wN.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif msg.text in [".Sp",".sp",".Speed",".speed"]:
                wN.sendText(msg.to, "「Benchmarking..」")
                start = time.time()
                for i in range(3000):
                    1+1 
                elsp = time.time() - start
                wN.sendText(msg.to, "%s" % (elsp))   

            elif msg.text in ["Speed Setting"]:  	
                wN.sendText(msg.to, "「 Debug Speed 」\n☼Type: Speed Setting\n☼Testing....")
                wN.sendText(msg.to, "=====「Speed Setting」=====")
                start = time.time()
                start2 = time.time()
                start3 = time.time()
                start4 = time.time()             
                start5 = time.time()             
                start6 = time.time()             
                start7 = time.time()    
                start8 = time.time()             
                start9 = time.time()             
                start10 = time.time()                         
                for i in range(3000):
                    1+1
                elsp = time.time() - start          
                elsp2 = time.time() - start2
                elsp3 = time.time() - start3
                elsp4 = time.time() - start4
                elsp5 = time.time() - start5
                elsp6 = time.time() - start6
                elsp7 = time.time() - start7
                elsp8 = time.time() - start8
                elsp9 = time.time() - start9
                elsp10 = time.time() - start10    
                wN.sendText(msg.to, "「 Debug Speed」\nType: Contact\nTime taken: %s" % (elsp))   
                wN.sendText(msg.to, "「 Debug Speed」\nType: AutoJoin\nTime taken: %s" % (elsp2))   
                wN.sendText(msg.to, "「 Debug Speed」\nType: AutoCancel\nTime taken: %s" % (elsp3))   
                wN.sendText(msg.to, "「 Debug Speed」\nType: LeaveRoom\nTime taken: %s" % (elsp4))   
                wN.sendText(msg.to, "「 Debug Speed」\nType: Timeline\nTime taken: %s" % (elsp5))                
                wN.sendText(msg.to, "「 Debug Speed」\nType: AutoAdd\nTime taken: %s" % (elsp6))                
                wN.sendText(msg.to, "「 Debug Speed」\nType: Protect\nTime taken: %s" % (elsp7))    
                wN.sendText(msg.to, "「 Debug Speed」\nType: Linkprotect\nTime taken: %s" % (elsp8))        
                wN.sendText(msg.to, "「 Debug Speed」\nType: Inviteprotect\nTime taken: %s" % (elsp9))      
                wN.sendText(msg.to, "「 Debug Speed」\nType: Cancelprotect\nTime taken: %s" % (elsp10))     
                                                              

#==============================================================================#                                                                                  
            elif 'Xpertcrash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc1c72b2a69c6ab18a7b28aa77fee5822,'"}
                wN.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
                wN.sendMessage(msg)                                                   
            elif msg.text.lower() == '#####':
               if msg.from_ in admin and owner:           	
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc4670540ac3b113403a9667df0b09df3',"}
                wN.sendText(msg.to,"Sepi ea ┌П┐(◣_◢)┌П┐")
                wN.sendMessage(msg)
            elif msg.text in ["404"]:
              if msg.from_ in admin:
                wN.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
            elif msg.text.lower() == wait["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                wN.sendMessage(msg)
                profile = wN.getProfile()
                xname = profile.displayName
                xlen = str(len(xname)+1)
                msg.contentType = 0
                msg.text = "@"+xname+" \n\n\n\n[Auto Respond Tag]"
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                wN.sendMessage(msg)
                contact = wN.getContact(mid)
                wait2['setTime'][msg.to] = datetime.today().strftime('「Date」: %d-%m-%Y \n「Day」: %A \n「Time」: %H:%M:%S')
                eltime = time.time() - mulai
                van = "вoт нaѕ вeen acтιve\n "+ waktu(eltime)
                wN.sendText(msg.to,"Type: Kalender♪\n" + (wait2['setTime'][msg.to]) + "\n\n"+ van + "\n\nType: Name\n" + contact.displayName + "\n\nType: Mid\n" + contact.mid + "\n\nType: Bio\n" + contact.statusMessage)
                h = wN.getContact(mid)                
                wN.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)  
                h = wN.getContact(mid)
                cu = wN.channel.getCover(mid)          
                path = str(cu)
                wN.sendImageWithURL(msg.to, path)                              
            elif msg.text.lower() == "me key":
            	wN.sendText(msg.to,"Me Key Saat Ini Adalah : 「"+wait["me"]+"」")
            elif "Set me: " in msg.text:
                wait["me"] = msg.text.replace("Set me: ","")
                wN.sendText(msg.to,"Me Key Berhasil Diubah Menjadi : 「"+wait["me"]+"」")
            elif msg.text in ["Reset me key"]:
                wait["me"] = "me"
                wN.sendText(msg.to,"Me Key Berhasil Direset Menjadi : 「"+wait["me"]+"」")
                
            elif msg.text.lower() == "respon key":
            	wN.sendText(msg.to,"Respon Key Saat Ini Adalah : 「"+wait["AgResp"]+"」")
            elif "Set respon: " in msg.text:
                wait["AgResp"] = msg.text.replace("Set respon: ","")
                wN.sendText(msg.to,"Respon Key Berhasil Diubah Menjadi : 「"+wait["AgResp"]+"」")
            elif msg.text in ["Reset respon key"]:
                wait["AgResp"] = "AgResp"
                wN.sendText(msg.to,"Respon Key Berhasil Direset Menjadi : 「"+wait["AgResp"]+"」")
                
            elif msg.text.lower() == "respontag key":
            	wN.sendText(msg.to,"Respon Tag Key Saat Ini Adalah : 「"+wait["TagRespon"]+"」")
            elif "Set respontag: " in msg.text:
                wait["TagRespon"] = msg.text.replace("Set respontag: ","")
                wN.sendText(msg.to,"Respon Tag Key Berhasil Diubah Menjadi : 「"+wait["TagRespon"]+"」")
            elif msg.text in ["Reset respontag key"]:
                wait["TagRespon"] = "TagRespon"
                wN.sendText(msg.to,"Respon Tag Key Berhasil Direset Menjadi : 「"+wait["TagRespon"]+"」")
            elif "Add: " in msg.text:
                target = msg.text.replace("Add: ","")
                wN.findAndAddContactsByMid(target)
                wN.sendText(msg.to, "Sukses Add " +wN.getContact(target).displayName+ ". ")
                msg.contentType = 13
                msg.contentMetadata = {"mid": target}
                wN.sendMessage(msg)
                print "Add user"
            elif msg.text.lower() == 'Hai @':
                _name = msg.text.replace("Hai @","")
                _nametarget = _name.rstrip(' ')
                gs = wN.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "uc4670540ac3b113403a9667df0b09df3',"}
                            wN.sendMessage(g.mid,msg.to + str(msg))
                            wN.sendText(g.mid, "Hallo")
                            wN.sendText(g.mid, "Error ya 😅 ??")
                            print " Spammed crash Wkwkwk!"                            
#========================== B O T ``C O M M A N D =============================#
#==============================================================================#
            elif msg.text.lower() == 'contact on':
               if msg.from_ in admin and owner:           	
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"contact already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"contact already on")
            elif msg.text.lower() == 'contact off':
               if msg.from_ in admin and owner:           	
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ❎ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"contact already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ❎ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"contact already off")
            elif msg.text.lower() == 'high on':
               if msg.from_ in admin and owner:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection High Already ON")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection High Already ON")
            elif msg.text.lower() == 'protect on':
               if msg.from_ in admin and owner:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection already on")                                               
            elif msg.text.lower() == 'qr on':
               if msg.from_ in admin and owner:            	
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect qr ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect qr ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Qr already on")
            elif msg.text.lower() == 'invit on':
               if msg.from_ in admin and owner:            	
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Invite already on")
            elif msg.text.lower() == 'cancel on':
               if msg.from_ in admin and owner:            	
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Cancel Protection already on")
            elif msg.text.lower() == 'autojoin on':   
               if msg.from_ in owner:             
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Autojoin already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Autojoin already on")
            elif msg.text.lower() == 'autojoin off':
               if msg.from_ in owner:            	
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Autojoin already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Autojoin already off")
            elif msg.text.lower() == 'high off':
               if msg.from_ in admin and owner:            	
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection High Already OFF")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection High Already OFF")                        
            elif msg.text.lower() == 'protect off':
               if msg.from_ in admin and owner:            	
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection already off")
            elif msg.text.lower() == 'qr off':
               if msg.from_ in admin and owner:            	
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Qr already off")
            elif msg.text.lower() == 'invit off': 
               if msg.from_ in admin and owner:           	
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Protection Invite already off")
            elif msg.text.lower() == 'cancel off':
               if msg.from_ in admin and owner:            	
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Cancel Protection Invite already off")
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
                            wN.sendText(msg.to,strnum + "The team dewNined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Nilai tidak benar")
                    else:
                        wN.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'leave on':
               if msg.from_ in owner:           	
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'leave off':
               if msg.from_ in owner:           	
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'share on':
               if msg.from_ in admin and owner:           	
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
               if msg.from_ in admin and owner:           	
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Share already off")
 #==============================================================================#                                   
            elif msg.text.lower() == 'set':   
               if msg.from_ in admin and owner:
                md = ""
                if wait["autoJoin"] == True: md+="Auto join ☞ ✔\n"
                else: md +="Auto join ☞ ✖\n"  
                if wait["autoAdd"] == True: md+="Auto add ☞ ✔\n"
                else: md +="Auto add ☞ ✖\n"  
                if wait["autoCancel"]["on"] == True:md+="Auto cancel ☞" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "Group cancel ☞ ✖\n"
                if wait["leaveRoom"] == True: md+="Auto leave ☞ ✔\n"
                else: md+="Auto leave ☞ ✖\n"
                if wait["contact"] == True: md+="Contact ☞ ✔\n"
                else: md+="Contact ☞ ✖\n"
                if wait["timeline"] == True: md+="Share ☞ ✔\n"
                else:md+="Share ☞ ✖\n"
                if wait["alwayRead"] == True: md+="Auto read ☞ ✔\n"
                else: md +="Auto read ☞ ✖\n"
                if wait["crashpc"] == True: md+="Auto crash pc ☞ ✔\n"
                else: md +="Auto crash pc ☞ ✖\n"
                if wait["crashTag"] == True: md+="Tag crash ☞ ✔\n"
                else: md +="Tag crash ☞ ✖\n"
                if wait["crashKick"] == True: md+="Auto crash kick☞ ✔\n"
                else: md +="Auto crash kick ☞ ✖\n"
                if wait["autoCrash"] == True: md+="Auto crash ☞ ✔\n"
                else: md +="Auto crash ☞ ✖\n"
                if wait["respondpc"] == True: md+="Auto respond ☞ ✔\n"
                else: md +="Auto respond pc ☞ ✖\n"
                if wait["detectMention"] == True: md+="Respond tag ☞ ✔\n"
                else: md +="Respond tag ☞ ✖\n"
                if wait["kickMention"] == True: md+="Mention kick ☞ ✔\n"
                else: md +="Mention kick☞ ✖\n"
                if wait["TagMention"] == True: md+="Tag mention ☞ ✔\n"
                else: md +="Tag mention ☞ ✖\n"
                if wait["blockMention"] == True: md+="Block mention ☞ ✔\n"
                else: md +="Block mention ☞ ✖\n"
                if wait["protect"] == True: md+="Protect ☞ ✔\n"
                else:md+="Protect ☞ ✖\n"
                if wait["protect"] == True: md+="High ☞ ✔\n"
                else:md+="High ☞ ✖\n"
                if wait["linkprotect"] == True: md+="Link protect ☞ ✔\n"
                else:md+="Link protect ☞ ✖\n"
                if wait["inviteprotect"] == True: md+="Invitation protect ☞ ✔\n"
                else:md+="Invitation protect ☞ ✖\n"
                if wait["cancelprotect"] == True: md+="Cancel protect ☞ ✔\n"
                else:md+="Cancel protect ☞ ✖"
                wN.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                wN.sendMessage(msg)      
 #==============================================================================#              
            elif cms(msg.text,["bot creator","Bot Creator"]):
               if msg.from_ in admin and owner:           	
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uf15f63d71ad0162c3e791cd3c6efca96"}
                wN.sendMessage(msg)
#==============================================================================#         
            elif msg.text.lower() == 'add on':
               if msg.from_ in admin:           	
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'add off':
               if msg.from_ in admin:           	
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
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
#            elif msg.text.lower() == 'jam on':
#                if wait["clock"] == True:
#                    wN.sendText(msg.to,"Jam already on")
#                else:
#                    wait["clock"] = True
#                    now2 = datetime.now()
#                    nowT = datetime.strftime(now2,"?%H:%M?")
#                    profile = wN.getProfile()
#                    profile.displayName = wait["cName"] + nowT
#                    wN.updateProfile(profile)
#                    wN.sendText(msg.to,"Jam set on")
#            elif msg.text.lower() == 'jam off':
#                if wait["clock"] == False:
#                    wN.sendText(msg.to,"Jam already off")
#                else:
#                    wait["clock"] = False
#                    wN.sendText(msg.to,"Jam set off")
  #          elif "Jam say:" in msg.text:
  #              n = msg.text.replace("Jam say:","")
  #              if len(n.decode("utf-8")) > 30:
  #                  wN.sendText(msg.to,"terlalu lama")
  #              else:
  #                  wait["cName"] = n
  #                  wN.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
  #          elif msg.text.lower() == 'update':
  #              if wait["wNock"] == True:
  #                  now2 = datetime.now()
  #                  nowT = datetime.strftime(now2,"?%H:%M?")
  ##                  profile = wN.getProfile()
#                    profile.displayName = wait["cName"] + nowT
#                    wN.updateProfile(profile)
#                    wN.sendText(msg.to,"Diperbarui")
#                else:
#                    wN.sendText(msg.to,"Silahkan Aktifkan Jam")
#==============================================================================#
#==============================================================================#
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                wN.sendText(msg.to,"Send Contact 😎")
            
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                wN.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                wN.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                wN.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                wN.sendText(msg.to,"Bot Sudah Di Nonaktifkan.")   
                
#            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
#                print "[Command]Like executed"
#                wN.sendText(msg.to,"Like Status Owner")
#                try:
#                  likeme()
#                except:
#                  pass
#                
#            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
#                print "[Command]Like executed"
#                wN.sendText(msg.to,"Like Status Teman")
#                try:
#                  likefriend()
#                except:
#                  pass
#            
#            elif msg.text in ["Like:on","Like on"]:
#                if wait["likeOn"] == True:
#                    if wait["lang"] == "JP":
#                        wN.sendText(msg.to,"Done")
#                else:
#                    wait["likeOn"] = True
#                    if wait["lang"] == "JP":
#                        wN.sendText(msg.to,"Already")
#                        
#            elif msg.text in ["Like off","Like:off"]:
#                if wait["likeOn"] == False:
#                    if wait["lang"] == "JP":
#                        wN.sendText(msg.to,"Done")
#                else:
#                    wait["likeOn"] = False
#                    if wait["lang"] == "JP":
#                        wN.sendText(msg.to,"Already")
                        
            elif msg.text in ["Simisimi on","Simi on"]:
                settings["simiSimi"][msg.to] = True
                wN.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Simi off"]:
                settings["simiSimi"][msg.to] = False
                wN.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["Read on","R on"]:
                wait['alwayRead'] = True
                wN.sendText(msg.to,"「 Auto Read」\nType: All\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Read off","R off"]:
                wait['alwayRead'] = False
                wN.sendText(msg.to,"「 Auto Read」\nType: All\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Detect mention on","detect mention on","Dm on","dm on"]:
                wait['detectMention'] = True
                wN.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Detect mention off","detect mention off","Dm off","dm off"]:
                wait['detectMention'] = False
                wN.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Poto on","poto on"]:
                wait["detectMention3"] = True
                wN.sendText(msg.to,"「 Auto Respon Tag Foto」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Poto off","poto off"]:
                wait["detectMention3"] = True
                wN.sendText(msg.to,"「 Auto Respon Tag Foto」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["C on","Autocrash on"]:
                wait["autoCrash"] = True
                wN.sendText(msg.to,"「 Auto Crash」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["C off","Autocrash off"]:
                wait["autoCrash"] = False
                wN.sendText(msg.to,"「 Auto Crash」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Pc on","Responpc on"]:
                wait["respondpc"] = True
                wN.sendText(msg.to,"「 Auto Respon Pc」\nType: Respon Pc\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Pc off","Responpc off"]:
                wait["respondpc"] = False
                wN.sendText(msg.to,"「 Auto Respon Pc」\nType: Respon Pc\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Cpc on","Crashpc on"]: 
                wait["crashpc"] = True
                wN.sendText(msg.to,"「 Auto Respon Pc + Crash」\nType: Respon Pc + Crash\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Cpc off","Crashpc off"]:
                wait["crashpc"] = False
                wN.sendText(msg.to,"「 Auto Respon Pc + Crash」\nType: Respon Pc + Crash\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Ct on","Crashtag on"]:
                wait["crashTag"] = True
                wN.sendText(msg.to,"「 Mention Crash」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Ct off","Crashtag off"]:
                wait["crashTag"] = False
                wN.sendText(msg.to,"「 Mention Crash」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Ck on","Crashkick on"]:
                wait["crashKick"] = True
                wN.sendText(msg.to,"Kick Crash Set to ON")
                
            elif msg.text in ["Ck off","Crashkick off"]:
                wait["crashKick"] = False
                wN.sendText(msg.to,"Kick Crash Set to OFF")      
                
            elif msg.text in ["Tm on","Tagmention on"]:
                if wait["tagMention"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Tag Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Tag Mention Set to ON")
                else:
                    wait["TagMention"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Tag Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Tag Mention Already ON")
                        
            elif msg.text in ["Tm off","Tagmention off"]:
                if wait["TagMention"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Tag Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Tag Mention Set to OFF")
                else:
                    wait["TagMention"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 Tag Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wN.sendText(msg.to,"Tag Mention Already OFF")
            
            elif msg.text in ["Sensi on","S on","Kick mention on","Km on","Responkick on"]:
                wait["kickMention"] = True
                wN.sendText(msg.to,"「 Kick Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Sensi off","S off","Kick mention off","Km off","Responkick off"]:
                wait["kickMention"] = False
                wN.sendText(msg.to,"「 Kick Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Block mention on","Bm on","Block Mention on","bm on","block mention on"]:
            	wait["blockMention"] = True
                wN.sendText(msg.to,"「 Block Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Block mention off","Bm off","Block Mention off","bm off","block mention off"]:
            	wait["blockMention"] = False
                wN.sendText(msg.to,"「 Block Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text.lower() in ['sticker:on','detectsticker:on','sticker on']:
              if msg.from_ in admin:
                if wait['sticker'] == True:
                    wN.sendText(msg.to, "Sticker id detect already ON.")
                else:
                    wait['sticker']=True
                    wN.sendText(msg.to, "Sticker id detect turned ON.")
                    
            elif msg.text.lower() in ['sticker:off','detectsticker:off','sticker off']:
              if msg.from_ in admin:
                if wait['sticker'] == False:
                    wN.sendText(msg.to, "Sticker id detect already OFF.")
                else:
                    wait['sticker']=False
                    wN.sendText(msg.to, "Sticker id detect turned OFF.")
#==============================================================================#
            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Sudah Onヽ(´▽｀)")
            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"Sudah Off(p′︵‵。)")
                            
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
            elif msg.text in ["BUBAR","bubar","bubar tolol"]:
            	   cat = ["http://dl.profile.line-cdn.net/0m002af1d3725161d09deb2597257acb237065e3003073"]
                   meow = random.choice(cat)
                   wN.sendImageWithURL(msg.to,meow)                   
            elif ":v" in msg.text:
                url = ("https://i.imgur.com/WbYWq38.jpg")
                urllib.urlretrieve(url, "gambar.png")
                wN.sendImage(msg.to, "gambar.png")
            elif "hmm" in msg.text:
            	url = ("https://ih1.redbubble.net/image.414126097.7189/flat,800x800,070,f.u1.jpg")
                urllib.urlretrieve(url, "gambar.png")
                wN.sendImage(msg.to, "gambar.png")
            elif msg.text in ["hilih","halah"]:
            	url = ("https://s14.postimg.org/e89u8gpo1/1514433298070.jpg")
                say = ("Hilih kinthil")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasyl.mp3")
                urllib.urlretrieve(url, "hilihkinthil.png")
                wN.sendImage(msg.to, "hilihkinthil.png")
                wN.sendAudio(msg.to,"hasyl.mp3")
            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                iyo.sendGifWithURL(msg.to,gore)
            elif msg.text in ["brisik","Berisik","Brisik","berisik","berisik asw"]:
            	vn = ("LINE_A20171229_005634157.m4a")
                wN.sendAudio(vn)
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = wN.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = iyo.getGroup(i)
                            _list += gids.name
                            wN.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        wN.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        wN.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  
            elif "/gCall" in msg.text:
            	group = wN.getGroup(msg.to)
                wN.createGroupCall(msg.to)
#==============================================================================#
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = wN.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        wN.sendText(msg.to,"Check Your Gift 😆")
                        wN.sendMessage(msg,g)
#==============================================================================#
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
                                    
            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
            
            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
                                    
            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
            
            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
                                    
            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '145277'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
                                    
            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    wN.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    wN.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
            
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                wN.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                wN.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                wN.sendMessage(msg)
                
            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                wN.sendMessage(msg)
                
            elif msg.text in ["Gift4"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                wN.sendMessage(msg)
               
            elif msg.text in ["Spam gift"]:
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
#============================ooo==================================================#
            elif "Salam1" in msg.text:
                wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Assalamu'alaikum")
            elif "Salam2" in msg.text:
                wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
                if msg.from_ in admin:
    				if msg.toType == 2:
    					if msg.toType == 2:
    						print "ok"
    						_name = msg.text.replace("Salam3","")
    						gs = wN.getGroup(msg.to)
    						gs = wN.getGroup(msg.to)
    						gs = wN.getGroup(msg.to)
    						gs = wN.getGroup(msg.to)
    						wN.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
    						wN.sendText(msg.to,"maaf kalo gak sopan")
    						targets = []
    						for g in gs.members:
    							if _name in g.displayName:
    								targets.append(g.mid)
    						if targets == []:
    							wN.sendText(msg.to,"Not found.")
    						else:
    							for target in targets:
    								try:
    									klist=[wN]
    									kicker=random.choice(klist)
    									kicker.kickoutFromGroup(msg.to,[target])
    									print (msg.to,[g.mid])
    								except:
    									wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                        wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                        wN.sendText(msg.to,"Nah salamnya jawab sendiri jadinya")
#==============================================================================#
            elif "wNeanse" in msg.text:
                if msg.from_ in owner:    	
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = wN.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[wN]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                wN.sendMessage(msg.to,"Grup wNeanse")
#-----------------------------------------------------
                                
            elif "Ratakan" in msg.text:
                if msg.from_ in owner:            	
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = wN.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[wN]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                wN.sendMessage(msg.to,"Grup Dibersihkan")
#-----------------------------------------------------------
            
            elif "Kickall" in msg.text:
				OWN = "uc4670540ac3b113403a9667df0b09df3"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("Fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = wN.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"PEMBERSIHAN!!")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									wN.kickoutFromGroup(msg.to, [target])							   
							except:
									wN.kickoutFromGroup(msg.to, [target])							   
									pass
            elif "Mayhem" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = wN.getGroup(msg.to)
                    wN.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n' abort' to abort♪")
                    wN.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[wN]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   wN.sendText(msg.to,"Mayhem done")
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
                           wN.sendText(msg.to,"Success ea 😅")
            
            elif ("Ulti " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wN.kickoutFromGroup(msg.to,[target])
                       except:
                           wN.sendText(msg.to,"Success ea 😅")
            
            elif "#Kick " in msg.text:
                midd = msg.text.replace("#Kick ","")
                wN.kickoutFromGroup(msg.to,[midd])
            
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                wN.findAndAddContactsByMid(midd)
                wN.inviteIntoGroup(msg.to,[midd])
                    
            elif msg.text.lower() == 'cancel':
                if msg.from_ in owner:
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
            
            elif msg.text.lower() == 'ourl':
                if msg.from_ in owner:
                    group = wN.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    wN.updateGroup(group)
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 URL Group」\nType: Url\nStatus: Url open success")
                    else:
                        wN.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"It can not be used outside the group")
                    else:
                        wN.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'curl':
                if msg.from_ in owner:
                    group = wN.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    wN.updateGroup(group)
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"「 URL Group」\nType: Url\nStatus: Url wNose success")
                    else:
                        wN.sendText(msg.to,"URL wNose")
                else:
                    if wait["lang"] == "JP":
                        wN.sendText(msg.to,"It can not be used outside the group")
                    else:
                        wN.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","Gurl"]:
                if msg.from_ in owner:
                    g = wN.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        wN.updateGroup(g)
                    gurl = wN.reissueGroupTicket(msg.to)
                    wN.sendText(msg.to,"「 LINK Group」\nType: Link group\nStatus: line://ti/g/" + gurl)
                    
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		wN.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=wN.findGroupByTicket(ticket_id)
				wN.acceptGroupInvitationByTicket(group.mid,ticket_id)
				wN.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                    
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
                if msg.from_ in owner:
                    X = wN.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    wN.updateGroup(X)
            
            elif "Ginfo" in msg.text:
                    group = wN.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(wN.reissueGroupTicket(group.id)))
                    ret_ = "╔════════Grup Info═════════"
                    ret_ += "\n╠Nama Grup : {}".format(group.name)
                    ret_ += "\n╠ID Grup : {}".format(group.id)
                    ret_ += "\n╠Pembuat Grup : {}".format(gCreator)
                    ret_ += "\n╠Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠Grup QR : {}".format(gQr)
                    ret_ += "\n╠Grup URL : {}".format(gTicket)
                    ret_ += "\n╚════════Grup Info═════════"
                    wN.sendText(msg.to, str(ret_))
                    wN.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
            
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
#            elif msg.text in ["Quote","quote","quotes","Quotes"]:
#                quote = ['Barangsiapa yang suka meninggalkan barang di tempat umum maka ia akan kehilangan barangnya tersebut\n\nQuote By Riko.','Kunci KESUKSESAN itu cuma satu, yakni lu harus BERHASIL.\n\nQuote By Riko.','Buang mantan di TPA']
#                psn = random.choice(quote)
#                wN.sendText(msg.to,psn)
#==============================================================================#
#==============================================================================#
#            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
#                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
#                 psn = random.choice(quote)
#                 wN.sendText(msg.to,psn)
#==============================================================================#
            elif msg.text == "Link bokep":
                    wN.sendText(msg.to,"nekopoi.host")
                    wN.sendText(msg.to,"sexvideobokep.com")
                    wN.sendText(msg.to,"memek.com")
                    wN.sendText(msg.to,"pornktube.com")
                    wN.sendText(msg.to,"faketaxi.com")
                    wN.sendText(msg.to,"videojorok.com")
                    wN.sendText(msg.to,"watchmygf.mobi")
                    wN.sendText(msg.to,"xnxx.com")
                    wN.sendText(msg.to,"pornhd.com")
                    wN.sendText(msg.to,"xvideos.com")
                    wN.sendText(msg.to,"vidz7.com")
                    wN.sendText(msg.to,"m.xhamster.com")
                    wN.sendText(msg.to,"xxmovies.pro")
                    wN.sendText(msg.to,"youporn.com")
                    wN.sendText(msg.to,"pornhub.com")
                    wN.sendText(msg.to,"anyporn.com")
                    wN.sendText(msg.to,"hdsexdino.com")
                    wN.sendText(msg.to,"rubyourdick.com")
                    wN.sendText(msg.to,"anybunny.mobi")
                    wN.sendText(msg.to,"wNiphunter.com")
                    wN.sendText(msg.to,"sexloving.net")
                    wN.sendText(msg.to,"free.goshow.tv")
                    wN.sendText(msg.to,"eporner.com")
                    wN.sendText(msg.to,"Pornhd.josex.net")
                    wN.sendText(msg.to,"m.hqporner.com")
                    wN.sendText(msg.to,"m.spankbang.com")
                    wN.sendText(msg.to,"m.4tube.com")
                    wN.sendText(msg.to,"brazzers.com")
#==============================================================================#
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
                msgs="═══════List Friend═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Friend═══════\n\nTotal Friend : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = wN.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═══════List Member═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Member═══════\n\nTotal Members : %i" % len(group)
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
                msgs="═══════List FriendMid═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═══════List FriendMid═══════\n\nTotal Friend : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = wN.getBlockedContactIds()
                kontak = wN.getContacts(blockedlist)
                num=1
                msgs="═══════List Blocked═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Blocked═══════\n\nTotal Blocked : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:  
                gruplist = wN.getGroupIdsJoined()
                kontak = wN.getGroups(gruplist)
                num=1
                msgs="═══════List Grup═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═══════List Grup═══════\n\nTotal Grup : %i" % len(kontak)
                wN.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = wN.getGroupIdsJoined()
                kontak = wN.getGroups(gruplist)
                num=1
                msgs="═══════List GrupMid═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═══════List GrupMid═══════\n\nTotal Grup : %i" % len(kontak)
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
                
            elif msg.text in ["Glist"]:
                gid = wN.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (wN.getGroup(i).name +" ? ["+str(len(wN.getGroup(i).members))+"]")
                wN.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
                
            elif msg.text in ["Tag me"]:
                            profile = wN.getProfile()
                            xname = profile.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" \n\n\nAuto Respond Tag"
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                            wN.sendMessage(msg)
            
            elif msg.text.lower() == 'cancel':
                gid = wN.getGroupIdsInvited()
                for i in gid:
                    wN.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    wN.sendText(msg.to,"He dewNined all invitations")
                    
            elif "@bye" in msg.text:
                if msg.from_ in owner or admin or staff:
                    ginfo = wN.getGroup(msg.to)
                    try:
                        wN.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------------------------------------                            
            elif "mention" == msg.text.lower():
                if msg.from_ in admin:
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
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    wN.sendMessage(cnt)
#-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Dor","Tag","Tagall"]:
                group = wN.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    wN.sendMessage(msg)
                except Exception as error:
                    print error              
#-------------------------------------------------------------    
            elif "lurk on" == msg.text.lower():
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
                         wN.sendText(msg.to,"Lurking already on")
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

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    wN.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wN.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             wN.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = wN.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
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
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
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
                        
            elif "slurker on" == msg.text.lower():
               if msg.from_ in staff:            	
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
                         wN.sendText(msg.to,"Lurking already on")
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

                    
            elif "slurker off" == msg.text.lower():
               if msg.from_ in staff:            	
                if msg.to not in wait2['readPoint']:
                    wN.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wN.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "slurkers" == msg.text.lower():
                 if msg.from_ in staff:           	
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             wN.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = wN.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
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
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
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
                        
            elif "Sider on" == msg.text.lower():
               if msg.toType == 2:         	
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
                         wN.sendText(msg.to,"Lurking already on")
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

                    
            elif "Sider off" == msg.text.lower():
               if msg.toType == 2:   	
                if msg.to not in wait2['readPoint']:
                    wN.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wN.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "Siders" == msg.text.lower():
                if msg.toType == 2:	
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             wN.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = wN.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
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
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
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
                        
            elif "Cek sider on" in msg.text:
	      if msg.from_ in Creator:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                wN.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Cek sider off" in msg.text:
	      if msg.from_ in Creator:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    wN.sendText(msg.to, "Cek Sider Off")
                else:
                    wN.sendText(msg.to, "Heh Belom Di Set")
                        
            elif "Gbc " in msg.text:  	
                bc = msg.text.replace("Gbc ","")
                gid = wN.getGroupIdsJoined()
                for i in gid:
                    wN.sendText(i, bc)
                    
            elif "Cbc " in msg.text: 	
                bc = msg.text.replace("Cbc ","")
                gid = wN.getAllContactIds()
                for i in gid:
                    wN.sendText(i, bc)
            
            elif "Spam change: " in msg.text:            	
                wait["spam"] = msg.text.replace("Spam change: ","")
                wN.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    wN.sendText(msg.to,"spam changed")
                else:
                    wN.sendText(msg.to,"Done")
    
 #           elif "Spam: " in msg.text:
 #               strnum = msg.text.replace("Spam: ","")
 #               num = int(strnum)
 #               for var in range(0,num):
 #                   wN.sendText(msg.to, wait["spam"])
                    
            elif "Tag:10 @" in msg.text:
                _name = msg.text.replace("Tag:10 @","")
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
                    else:
                    	pass
                        
            elif "Tag:15 @" in msg.text:
                _name = msg.text.replace("Tag:15 @","")
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
                    else:
                    	pass
            
            elif "Tag @" in msg.text:
                _name = msg.text.replace("Tag @","")
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
                        
            
            elif "Tag:100 @" in msg.text:
                _name = msg.text.replace("Tag:100 @","")
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
                    
            elif msg.text in ["MiwNist"]:
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
            elif "Tagvn " in msg.text:
                cmd = msg.text.replace("Tagvn ","")
                if cmd == "on":
                    if wait["tagVN"] == False:
                        wait["tagVN"] = True
                        wN.sendText(msg.to,"「Tag VN on」")
                    else:
                        wN.sendText(msg.to,"「Turned on」")
                elif cmd == "off":
                    if wait["tagVN"] == True:
                        wait["tagVN"] = False
                        wN.sendText(msg.to,"「Tag VN off」")
                    else:
                        wN.sendText(msg.to,"「Turned off」")
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
#==============================================================================#
            elif "Foto" in msg.text:
                linkfoto = msg.text.replace("Foto ","")
                wN.sendImageWithURL(msg.to, linkfoto)
                
            elif "Video" in msg.text:
                 linkvid = msg.text.replace("Video ","")
                 wN.sendVideoWithURL(msg.to, linkvid)
#==============================================================================#
            elif msg.text.lower() == 'mymid':
                wN.sendText(msg.to,mid)
#            elif "Timeline: " in msg.text:
#                tl_text = msg.text.replace("Timeline: ","")
#                wN.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+wN.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = wN.getProfile()
                    profile.displayName = string
                    wN.updateProfile(profile)
                    wN.sendText(msg.to,"The name " + string + " I did NI change ◑")          
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = wN.getProfile()
                    profile.statusMessage = string
                    wN.updateProfile(profile)
                    wN.sendText(msg.to,"Update Bio👉" + string + "👈")
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
                               wN.wNoneContactProfile(target)
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
                
            elif msg.text in ["Result"]:
                    mE = wN.getProfile()
                    gT = wN.getGroupIdsJoined()
                    fT = wN.getAllContactIds()
                    wN.sendText(msg.to,"「"+mE.displayName+"」 \n\nGroup total : " + str(len(gT))+ "\nFriend total: " +str(len(fT)))       
                
            elif "playstore " in msg.text.lower():
                if msg.from_ in admin:
                    tob = msg.text.lower().replace("playstore ","")
                    wN.sendText(msg.to,"Sedang Mencari boss...")
                    wN.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    wN.sendText(msg.to,"Ketemu boss ^")

            elif "facebook " in msg.text.lower():
                if msg.from_ in admin:
                    tob = msg.text.lower().replace("facebook ","")
                    wN.sendText(msg.to,"「 Searching 」\n" "Type: Facebook Search\nStatus: Processing...")
                    wN.sendText(msg.to,"Title: " + a + "\nhttps://m.facebook.com/search/top/?q="+replace+"&ref=content_filter&tsid=0.7682944806717842&source=typeahead")
                    wN.sendText(msg.to,"「 Searching 」\n" "Type: Search Info\nStatus: Success")

            elif "github " in msg.text.lower():
                if msg.from_ in admin:
                    tob = msg.text.lower().replace("github ","")
                    wN.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                    wN.sendText(msg.to,"Title: " + a + "\nhttps://github.com/search?utf8=✓&q="+b)
                    wN.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Success")
                    
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Tr-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Tr-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                wN.sendText(msg.to, A)
            elif "Tr-ko" in msg.text:
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
                cari_hasil = 'wNass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO ENGLISH----\n" + "" + result + "\n------SUKSES-----")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'wNass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN.sendText(msg.to,"----FROM EN----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'wNass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'wNass="t0">'
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
                cari_hasil = 'wNass="t0">'
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
                cari_hasil = 'wNass="t0">'
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
                cari_hasil = 'wNass="t0">'
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
                cari_hasil = 'wNass="t0">'
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
                cari_hasil = 'wNass="t0">'
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
                cari_hasil = 'wNass="t0">'
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
                cari_hasil = 'wNass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                wN.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = wN.getGroup(msg.to)
                wN.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                wN.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                wN.sendAudio(msg.to,'tts.mp3')
            
            elif "Gblk" in msg.text:
                x = ("goblok lo asu")
                lang = 'id'
                tts = gTTS(text=x, lang=lang)
                tts.save("x.mp3")
                wN.sendAudio(msg.to,"x.mp3")
                
            elif "Kerad" in msg.text:
                kerad = ("kerad juga kamu ea","kerad sangad kamu bangsad","alamak, kerad juga kamu ea")
                asu = random.choice(kerad)
                lang = 'id'
                tts = gTTS(text=asu, lang=lang)
                tts.save("krd.mp3")
                wN.sendAudio(msg.to,"krd.mp3")
            
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
            
            elif "Myspeed" in msg.text:
                start = time.time()               
                elsp = time.time() - start
                agler = ("「 Debug Speed」\nType: speed\nTime taken: %ssecond" % (elsp))
                jawab = ("「 Debug Speed」\nType: speed\nTime taken: 0.1 second","「 Debug Speed」\nType: speed\nTime taken: 0 second")
                jawaban = random.choice(agler + jawab) 
                wN.sendText(msg.to,jawaban)            
            
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'wNass': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        wN.sendVideoWithURL(msg.to, ght)
                    except:
                        wN.sendText(msg.to, "Could not find it")
            
            elif "Youtubesearch " in msg.text:
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
                        
            elif "lirik" in msg.text.lower():
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(wait["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[3]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                wN.sendText(msg.to, str(ret_))
                        except:
                            wN.sendText(to, "Lirik tidak ditemukan")
                        
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
                              pesan="Over Text Limit! Please wNick link\n"
                              pesan+=wikipedia.page(wiki).url
                              wN.sendText(msg.to, pesan)
                          except Exception as e:
                              wN.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
					songname = msg.text.replace("Music ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						wN.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						wN.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						wN.sendAudioWithURL(msg.to,abc)
						wN.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
            
            elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						wN.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						wN.sendAudioWithURL(msg.to,abc)
						wN.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						wN.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
            
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
                    
            elif msg.text.lower().startswith("imagetext "):
                sep = msg.text.split(" ")
                textnya = msg.text.replace(sep[0] + " ","")
                urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                wN.sendImageWithURL(msg.to, urlnya)
                    
            elif 'video ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('video ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'wNass': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        wN.sendVideoWithURL(msg.to, ght)
                    except:
                        wN.sendText(msg.to, "Could not find it")
                        
            elif "Cekig " in msg.text:
                    try:
                        instagram = msg.text.replace("Cekig ","")
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
                        wN.sendText(msg.to, str(text))
                        wN.sendImageWithURL(msg.to, profileIG)
                    except Exception as e:
                        wN.sendText(msg.to, str(e))
            
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
                        
            elif "idline: " in msg.text:
                msgg = msg.text.replace('idline: ','')
                conn = wN.findContactsByUserid(msgg)
                if False:
                 	wN.sendText(msg.to,"Gaada ID kayak gitu goblok!")
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    wN.sendText(msg.to,"[ Nama Profil ]\n"+conn.displayName+"\n\n[ Status Profil ]\n"+conn.statusMessage+"\n\n[ Mid Profil ]\n"+conn.mid+"\n\n[ URL Foto Profil ]\nhttp://dl.profile.line-cdn.net/"+conn.pictureStatus+"\n\nKepoin lebih lanjut?\nKlik line://ti/p/~"+msgg)
                    wN.sendMessage(msg)

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                wN.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text.lower() == 'time':
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
                    if bln == str(k): bulan = blan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                wN.sendText(msg.to, rst)
                
            elif "Location " in msg.text.lower():
                            pisah = msg.text.split("n ")
                            location = msg.text.replace(pisah[0]+"n ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = requests.get("http://api.corrykalam.net/apiloc.php?"+ urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "╔══『 Detail location 』"
                                    ret_ += "\n╠ ⌬「 Lokasi」: " + data[0]
                                    ret_ += "\n╠ ⌬.「 Google maps 」: " + link
                                    ret_ += "\n╚══『 Detail location 』"
                                else:
                                    ret_ = "[ Details Location ] Error : Location not found"
                                wN.sendText(msg.to, str(ret_))
                                
            elif "Sholat " in msg.text.lower():
                            pisah = msg.text.split("e ")
                            location = msg.text.replace(pisah[0]+"e ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                r = requests.get("http://api.corrykalam.net/apisholat.php?" + urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[1] != "╠ ⌬「 Subuh」: " and data[2] != "╠ ⌬「 Dzuhur」: " and data[3] != "╠ ⌬「 Ashar」: " and data[4] != "╠ ⌬「 Maghrib」: " and data[5] != "╠ ⌬「 Isya」: ":
                                    ret_ = "╔══『 Jadwal Sholat 』"
                                    ret_ += "\n╠ ⌬「 Lokasi 」: " + data[0]
                                    ret_ += "\n" + data[1]
                                    ret_ += "\n" + data[2]
                                    ret_ += "\n" + data[3]
                                    ret_ += "\n" + data[4]
                                    ret_ += "\n" + data[5]
                                    ret_ +=  "\n╚══『 Jadwal Sholat 』"
                                else:
                                    ret_ = "[ Prayer Schedule ] Error : Location not found" 
                                wN.sendText(msg.to, str(ret_))
                
            elif msg.text.lower().startswith("cuaca "):
                location = msg.text.lower().replace("cuaca ","")
                with requests.session() as web:
                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                    r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib2.quote(location)))
                    data = r.text
                    data = json.loads(data)
                    if "result" not in data:
                        ret_ = "╔══『 Status Cuaca 』"
                        ret_ += "\n╠ ⌬.「 Lokasi 」 : " + data[0].replace("Temperatur di kota ","")
                        ret_ += "\n╠ ⌬.「 Suhu 」 : " + data[1].replace("Suhu : ","")
                        ret_ += "\n╠ ⌬.「 Kelembaban 」: " + data[2].replace("Kelembaban : ","")
                        ret_ += "\n╠ ⌬.「 Tekanan Udara 」 : " + data[3].replace("Tekanan udara : ","")
                        ret_ += "\n╠ ⌬.「 Kecepatan Angin」 : " + data[4].replace("Kecepatan angin : ","")
                        ret_ += "\n╚══『 Status Cuaca 』"
                    else:
                        ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                    wN.sendText(msg.to, str(ret_))
                
            elif "google:" in msg.text:
                    a = msg.text.replace("google:","")
                    b = urllib.quote(a)
                    wN.sendText(msg.to, "https://www.google.co.jp/search?q=" + b)                
#==============================================================================#
 #           elif msg.text.lower() == 'ifconfig':
 #                   botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
 #                   wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
 #           elif msg.text.lower() == 'system':
 #                   botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
 #                   wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
 #           elif msg.text.lower() == 'kernel':
 #                   botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
 #                   wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
 #           elif msg.text.lower() == 'cpu':
 #                   botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
 #                   wN.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#==============================================================================#                             
            elif "Restart" in msg.text:
            	if msg.from_ in admin:
                    print "[Command]Restart"
                    try:
                        wN.sendText(msg.to,"Restarting...")
                        wN.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        wN.sendText(msg.to,"Please waiting...")
                        restart_program()
                        pass                   
                
            elif msg.text.lower() == 'runtime':
                wN.sendText(msg.to,"「Please wait..」\nType  :Loading...\nStatus : Loading...")
                eltime = time.time() - mulai
                van = "「 Runtime」\nType: Runtime\nStatus: вoт нaѕ вeen acтιve\n "+waktu(eltime)
                wN.sendText(msg.to,van)     

            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass               
#==============================================================================#
#==============================================================================#           
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Ban repeat " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      wN.sendText(msg.to,"Succes Banned ")
                   except:
                      pass        
#==============================================================================#           
            elif "Ban @" in msg.text:
               if msg.from_ in owner or admin or staff:
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
               if msg.from_ in owner or admin or staff:            	
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
                       nk1 = nk0.Istrip()
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
                                    
            elif msg.text in ["clear"]:
                wait["blacklist"] = {}
                wN.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                wN.sendText(msg.to,"Send contact")
                ki.sendText(msg.to,"Send contact")
                ag.sendText(msg.to,"Send contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                wN.sendText(msg.to,"Send contact")
                ki.sendText(msg.to,"Send contact")
                ag.sendText(msg.to,"Send contact")
            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    wN.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    wN.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="════════List Blacklist════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, wN.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n════════List Blacklist════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
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
                    cocoa = "════════List Blacklist════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n════════List Blacklist════════\n\nTotal Blacklist : %i" % len(matched_list)
                    wN.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
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
#----------------------------------------------
            elif msg.text.lower() in dangerMessage:
                try:
                    if msg.toType == 2:
                        wN.kickoutFromGroup(msg.to,[msg.from_])
                        wN.sendText(msg.from_,"Hati Hati Kalo Ngomong (｀・ω・´)")
                except:
                    pass
#========================================
            elif msg.text in ["creator"]:   
               if msg.toType == 2:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                wN.sendMessage(msg)
                jawab = ("Bot Creator by wN","My Creator is Handsome","My Creator is Cool")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                wN.sendAudio(msg.to,'tts.mp3')     
#-----------------------[Admin add section]------------------------
  #          elif "Admin add @" in msg.text:
  #            if msg.from_ in owner:
  #              print "[Command]Staff add executing"
  #              _name = msg.text.replace("Admin add @","")
  #              _nametarget = _name.rstrip('  ')
  #              gs = wN.getGroup(msg.to)
  #              gs = ki.getGroup(msg.to)
  #              gs = ag.getGroup(msg.to)
  #              targets = []
  #              for g in gs.members:
  #                  if _nametarget == g.displayName:
  #                      targets.append(g.mid)
  #              if targets == []:
  #                 random.choice(KAC).sendText(msg.to,"Contact not found")
  #              else:
  #                 for target in targets:
  #                      try:
  #                          admin.append(target)
  #                          wN.sendText(msg.to,"Succes Add To Adminlist")
  #                          ki.sendText(msg.to,"Succes Add To Adminlist")
  #                          ag.sendText(msg.to,"Succes Add To Adminlist")
  #                      except:
  #                          pass
  #              print "[Command]Staff add executed"
  #            else:
  #              wN.sendText(msg.to,"Command denied.")
  #              wN.sendText(msg.to,"Owner permission required.")
                
 #           elif "Admin remove @" in msg.text:
 #             if msg.from_ in owner:
 #               print "[Command]Staff remove executing"
 #               _name = msg.text.replace("Admin remove @","")
 #               _nametarget = _name.rstrip('  ')
 #               gs = wN.getGroup(msg.to)
 #               gs = ki.getGroup(msg.to)
 #               gs = ag.getGroup(msg.to)
 #               targets = []
 #               for g in gs.members:
 #                   if _nametarget == g.displayName:
 #                       targets.append(g.mid)
 #               if targets == []:
 #                  random.choice(KAC).sendText(msg.to,"Contact not found")
 #               else:
 #                  for target in targets:
 #                       try:
 #                           admin.remove(target)
 #                           wN.sendText(msg.to,"Succes Remove Admin From Adminlist")
 #                           ki.sendText(msg.to,"Succes Remove Admin From Adminlist")
 #                           ag.sendText(msg.to,"Succes Remove Admin From Adminlist")
 #                       except:
 #                           pass
 #               print "[Command]Staff remove executed"
 #             else:
 #               wN.sendText(msg.to,"Command denied.")
 #               wN.sendText(msg.to,"Owner permission required.")
                
 #           elif msg.text in ["Adminlist","adminlist"]:
 #             if admin == []:
 #                 wN.sendText(msg.to,"The adminlist is empty")
 #             else:
 #                 wN.sendText(msg.to,"Tunggu...")
 #                 mc = "||Admin ❁R̯̙̱͇̗̼̉̎͊̇̎̕͟͟͡I̛̮̝̖̾͌͂̄̈́̍̅̅̄͜͜K̨͎̺͚̘̻̬̱̲̉͒̅̽̾͝Ǫ̷̛͉̙͖͈̯̙͓͍̋͑̐̕͘͢͝͞ S̶̙̯̺̤̠̦̻̃̆͆̽͒̏͌̅͛͢E̡̨̡͕͇̲̼̐̾̆̓̐̄̒̽͝L̮͖͍̭̗̅̑́͆͒̔̈͢͠͞F̵̣̱̪͓̙̀̀̐̅̌̂͘̚͟͜͝͞B̴̛̝̳̱̬̙̓̅̈́̿̿̚͢O̠̺̙͇̫̹̘͕̅̑̇̏̚͞͠Ṫ̵͉͚̱͖̰̉̏̊̉̓̆̇͟͜͠ ❁||\n=====================\n"
 #                 for mi_d in admin:
 #                     mc += "❂͜͡➣" +wN.getContact(mi_d).displayName + "\n"
 #                 wN.sendText(msg.to,mc)
 #                 print "[Command]Stafflist executed"
#==============================================================================#
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = wN.getGroup(msg.to)
                       ginfo = wN.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       wN.updateGroup(gs)
                       invsend = 0
                       Ticket = wN.reissueGroupTicket(msg.to)
                       ag.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
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
                                    ag.sendText(msg.to,"Kamu Tercyduk")
                                    ag.sendText(msg.to,"┌П┐(◣_◢)┌П┐")
                                    ag.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ag.sendText(msg.to,"Tugas Selesai Boss")
                                    ag.sendText(msg.to,"See You ~~")
                                    ag.leaveGroup(msg.to)
                                    gs = wN.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    wN.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    wN.updateGroup(gs)
#-----------------------------------------------------------   
            elif "Dj" in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                                    try:
                                        wN.kickoutFromGroup(msg.to,[target])
                                    except:
                                        wN.sendText(msg.to, "ѕυcceѕѕ")
#-----------------------------------------------------------   
            elif ("Sentil " in msg.text):
                if msg.from_ in owner or admin or staff:            	
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wN.kickoutFromGroup(msg.to,[target])
                       except:
                           wN.sendText(msg.to,"Error")    
#-----------------------[Bot speed test Section]------------------------
            elif msg.text in ["Speed Response"]:
                if msg.from_ in owner or staff:

                    wN.sendText(msg.to, "=====「Speed Response」=====")
                    
                    wN.sendText(msg.to, "「Response Protect」")
                    start = time.time()
                    for i in range(3000):
                        1+1
                    elsp = time.time() - start
                    wN.sendText(msg.to,"「%sseconds」" % (elsp))     
                    print "[Command]Speed Response Protect"                    
 
                    wN.sendText(msg.to, "「Response Invite」")                    
                    start2 = time.time()
                    for i in range(3000):
                        1+1
                    elsp2 = time.time() - start2
                    wN.sendText(msg.to,"「%sseconds」" % (elsp2))     
                    print "[Command]Speed Response Invite"                  
                    
                    wN.sendText(msg.to, "「Response Cancel」")                    
                    start3 = time.time()
                    for i in range(3000):
                        1+1
                    elsp3 = time.time() - start3
                    wN.sendText(msg.to,"「%sseconds」" % (elsp3))       
                    print "[Command]Speed Response Cancel"                
                    
                    wN.sendText(msg.to, "「Response Kick」")                    
                    start4 = time.time()
                    for i in range(3000):
                        1+1
                    elsp4 = time.time() - start4
                    wN.sendText(msg.to,"「%sseconds」" % (elsp4))       
                    print "[Command]Speed Response Kick"        
                    
                    wN.sendText(msg.to, "「Response Qr」")                    
                    start5 = time.time()
                    for i in range(3000):
                        1+1
                    elsp5 = time.time() - start5
                    wN.sendText(msg.to,"「%sseconds」" % (elsp5))    
                    print "[Command]Speed Response Qr"       

                    wN.sendText(msg.to, "=====「Response Done! 」=====")
                    print "[Command]Speed all executed"
                else:
                    wN.sendText(msg.to,"Command Speed Done!")                   
     #-------------------------------------------------
            elif "youtube:" in msg.text.lower():
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           wN.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           wN.sendText(msg.to, isi[0])
                           #wN.sendVideoWithURL(msg.to, song[4])
                   except Exception as e:
                       wN.sendText(msg.to, str(e))  
#----------------------NUKE----------------------------------
            elif "###333" in msg.text:
                if msg.from_ in admin:
                    print "Nuke ok"
                    _name = msg.text.replace("###333","")
                    gs = wN.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ag.getGroup(msg.to)                    
                    start = time.time()
                    ki.sendText(msg.to, "Nuke Speed")
                    elapsed_time = time.time() - start
                    ag.sendText(msg.to, "%sseconds" % (elapsed_time))
                    wN.sendText(msg.to, "Nuke Start")
                    ki.sendText(msg.to, "Nuke Proses")
                    ag.sendText(msg.to,"􀜁􀇔􏿿 See You Bitch!")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        wN.sendText(msg.to,"Not found.")
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[wN,ki,ag]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Nuke Finish")
                                ag.sendText(msg,to,"Nuke Succes")                       
#==============================================#

            elif 'talkban ' in msg.text.lower():
                spl = msg.text.lower().replace('talkban ','')
                if spl == 'on':
                    if wait['talkban'] == True:
                        msgs="Talkban already Not For chat"
                    else:
                        msgs="Talkban set to Not For chat"
                        wait['talkban']=True
                    wN.sendText(msg.to, msgs)
                elif spl == 'off':
                    if wait['talkban'] == False:
                        msgs="Talkban already Allow For chat"
                    else:
                        msgs="Talkban set to Allow For chat"
                        wait['talkban']=False
                    wN.sendText(msg.to, msgs)
#-----------------------------------------------
            elif "Takol" in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wait["talkblacklist"][target] = True
                           group = wN.getContact(target)
                           wN.sendText(msg.to,group.displayName + " Succes Add to Talkban")
                       except:
                           wN.sendText(msg.to,"Error")
#---------------------------------------------------
            elif "Takel" in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           del wait["talkblacklist"][target]
                           group = wN.getContact(target)
                           wN.sendText(msg.to,group.displayName + " Delete From Talkban")
                       except:
                           wN.sendText(msg.to,group.displayName + " Not In Talkban")
#-----------------------------------------------
            elif msg.text in ["Talklist"]:
                displayfreand = wN.getContacts(wait["talkblacklist"])
                wN.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Talkban List」"
                for ids in displayfreand:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「Total %i Talkban List」 " % len(wait["talkblacklist"])
                wN.sendText(msg.to, msgs)
#-------------------------------------------------
            if wait["talkban"] == True:
             if msg.from_ in wait["talkblacklist"]:
                try:
                    wN.sendText(msg.to,wN.getContact(msg.from_).displayName + " Ngomong kk")
                    wN.kickoutFromGroup(msg.to,[msg.from_])
                except:
                    try:
                        wN.sendText(msg.to,wN.getContact(msg.from_) .displayName + " ")
                        wN.kickoutFromGroup(msg.to,[msg.from_])
                        wN.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        wN.sendText(msg.to,wN.getContact(msg.from_).displayName + " ")
                        wN.kickoutFromGroup(msg.to,[msg.from_])
                        wN.kickoutFromGroup(msg.to,[msg.from_])     
#-----------------------------------------------
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

        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = wN.getGroup(op.param1)
            contact = wN.getContact(op.param2)
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            wN.sendMessage(c)
            wN.sendText(op.param1,"╔═════════════" + "\n║" + wN.getContact(op.param2).displayName + "\n╠═════════════\n║Selamat Datang kak,,Jgn lupa Jalan2 ke NOTE ya 😊 \n╚═════════════")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "17225910",
                                    "STKPKGID": "1456919",
                                    "STKVER": "1" }                
            wN.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                wN.sendText(op.param1, "╔═════════════" + "\n║" + wN.getContact(op.param2).displayName + "\n╠═════════════\n║Selamat Jalan Kakak Terima Kasih Kunjunganya 😊 \n╚═════════════")
                wN.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+wN.getContact(op.param2).pictureStatus)
                d = Message(to=op.param1, from_=None, text=None, contentType=7)
                d.contentMetadata={
                                        "STKID": "12842269",
                                        "STKPKGID": "1318245",
                                        "STKVER": "1" }                
                wN.sendMessage(d)             
                print "MEMBER HAS LEFT THE GROUP"
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
#        if op.type == 5:
#            if wait["autoAdd"] == True:
#                if (wait["message"] in [""," ","\n",None]):
#                    pass
#                else:
#                    wN.sendText(op.param1,str(wait["message"]))
                    
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = wN.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    wN.kickoutFromGroup(op.param1,[op.param3])
                    wN.updateGroup(G)
#---------------------------------------------------------------
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

#def autolike():
#    count = 1
#    while True:
#        try:
#           for posts in wN.activity(1)["result"]["posts"]:
#             if posts["postInfo"]["liked"] is False:
#                if wait["likeOn"] == True:
#                   wN.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
#                   print "Like"
#                   if wait["commentOn"] == True:
#                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
#                         pass
#                      else:
#                          wN.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#        except:
#            count += 1
#            if(count == 50):
#                sys.exit(0)
#            else:
#                pass
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

#def likefriend():
#    for zx in range(0,20):
#      hasil = wN.activity(limit=20)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          wN.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          print "Like"
#        except:
#          pass
#      else:
#          print "Already Liked"
#time.sleep(0.60)

#def likeme():
#    for zx in range(0,20):
#        hasil = wN.activity(limit=20)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
#                try:
#                    wN.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#                    print "Like"
#                except:
#                    pass
#            else:
#                print "Status Sudah di Like"
#---------------------------------------------------------------
while True:
    try:
        Ops = wN.fetchOps(wN.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(wN.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            wN.Poll.rev = max(wN.Poll.rev, Op.revision)
            bot(Op)
