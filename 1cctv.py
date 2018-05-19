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
from googletrans import Translator

wN = CBW.LINE()
#wN.login(qr=True)
wN.login(token='')#cctv 
wN.loginResult()

wN1 = wN2 = wN3 = wN4 = wN5 = wN

print "╔═════════════════════════╗\n║╔═══════════════════════╗║\n║╠❂➣CBW BERHASIL LOGIN ║║\n║╚═══════════════════════╝║\n╚═════════════════════════╝"
reload(sys)
sys.setdefaultencoding('utf-8')


helpMessage ="""
╔═════════════
║╔════════════
║║✰  ✰ 
║╚════════════
║╔════════════
║║Owner : CBW
║╚════════════
║╔════════════
║╠❂➣Cctv
║╠❂➣Toong
║╠❂➣cctv on/off
║╠❂➣Check
║╠❂➣Sider
║╠❂➣Intip
║╠❂➣Setview
║╠❂➣Viewseen
║╠❂➣Intip on/off
║╚════════════
╚═════════════
"""
key1Message ="""
╔═════════════
║╔════════════
║║✰  ✰ 
║╚════════════
║╔════════════
║║Owner : CBW
║╚════════════
║╔════════════
║╠❂➣qr on/oғғ
║╠❂➣gυeѕт on/oғғ
║╠❂➣мeмвer on/oғғ
║╠❂➣groυp on/oғғ
║╠❂➣ĸιcĸ on/oғғ
║╠❂➣cancel on/oғғ
║╚════════════
╚═════════════
"""

KAC=[wN,wN1,wN2,wN3,wN4,wN5]
AST=[wN1,wN2,wN3,wN4,wN5]
mid1 = wN.getProfile().mid
Amid = wN1.getProfile().mid
Bmid = wN2.getProfile().mid
Cmid = wN3.getProfile().mid
Dmid = wN4.getProfile().mid
Emid = wN5.getProfile().mid

Bots=[mid1,Amid,Bmid,Cmid,Dmid,Emid]
induk=[mid1]
asist=[Amid,Bmid,Cmid,Dmid,Emid]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1","ud55745480bb2c5665e6a21df2a68155e","u6908b4803bf3e267cf659ddda91d5fa4","u60335d94c7a3ca3a3c3685f515724145","uc92d7e39d7259174dba7d8028c7ef4b2","uc1ba312554b4ee025039f54ff44c7c7f","uc70b2f7f85d13c96e0f28ded3b3b13d6","u9d4b18194ce5b48d86fa27e5fac1d606","ud3065a5bd9cf0d6961d9c046a124761c",mid1,Amid]#wN/CBW/6botProtect/media/agatha/hajir
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
wait = {
    "contact":False,
    "autoJoin":True,
    "autoCancel":{"on":False,"members":1},
    "leaveRoom":False,
    "timeline":False,
    "autoAdd":False,
    "detectMention":True,
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "QrProtect":False,
    "MProtection":False,
    "Protectguest":False,
    "Protectcancel":False,
    "autoKick":False,
    "auto":False,
    "tag":False,
    "tag2":False,
    "likeOn":False,
    "winvite":False,
    'invite':{},
    "Wc":False,
    "Wc2":False,
    "Lv":False,
    "Sider":{},
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "protectionOn":False,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }


setTime = {}
setTime = wait2['setTime']

contact = wN.getProfile()
mybackup = wN.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = wN.getProfile()
backup = wN.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = wN.getProfile()
profile = wN.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")

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


def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)


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
      M_id = self.Talk.client.sendMessage(0,M).id
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
            Name = wN.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in cctv['point']:
            Name = wN.getContact(op.param2).displayName
            if Name in cctv['sidermem'][op.param1]:
                pass
            else:
                cctv['sidermem'][op.param1] += "\n• " + Name
                cctv['cyduk'][op.param1][op.param2] = "\n• " + Name
        else:
            pass
    except:
        pass

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    print nm
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
    print msg
    try:
         wN.sendMessage(msg)
    except Exception as error:
        print error

def removeAllMessages(self, lastMessageId):
     return self._wN.removeAllMessages(0, lastMessageId)

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
url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait['autoAdd'] == True:
                wN.findAndAddContactsByMid(op.param1)
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    wN.sendText(op.param1,str(wait['message']))

#==========================[CBW]===========================
        if op.type == 55:
            try:
                group_id = op.param1
                user_id=op.param2
                subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
            except Exception as e:
                print e
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+wN.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@"+wN.getProfile().displayName,"")
                    jawab = ("Kenapa Tag Si "+wN.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung ownernya biar anu hihi..!!\n[autoRespon]by=>SelfBot~CBW\n👉Cyber Army Bot👈","Nah ngetag lagi si "," mending ajak mojok aja ownernya dari pada ngetag mulu.. wkwk.")
                    jawaban = random.choice(jawab)
                    wN.sendText(msg.to,jawaban)
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = wN.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN.sendImageWithURL(msg.to,ret_)
                                  break  
        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+wN.getProfile().displayName in msg.text:
                if wait["tag2"] == True:
                    tanya = msg.text.replace("@"+wN.getProfile().displayName,"")
                    jawab = "Ada apa ngetag "+wN.getProfile().displayName+"Maaf"
                    jawaban = random.choice(jawab)
                    wN.sendText(msg.to,jawaban)
                    random.choice(AST).kickoutFromGroup(msg.to,[msg.from_])
                    random.choice(KAC).inviteIntoGroup(msg.to,admin)
#==========================[CBW]===========================
#        if op.type == 32:
#            if wait["Protectcancel"] == True:
#                if op.param2 in admin and Bots:
#                    pass
#                if op.param2 not in Bots:
#                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#==========================[CBW]===========================
#        if op.type == 13:
#           if wait["Protectguest"] == True:
#                if op.param2 in admin and Bots:
#                    pass
#                if op.param2 not in Bots:
#                    random.choice(AST).cancelGroupInvitation(op.param1,[op.param3])
#                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#==========================[CBW]===========================
#        if op.type == 19:
#            if wait["MProtection"] == True:
#                if op.param2 in admin and Bots:
#                    pass
#                if op.param2 not in Bots:
#                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
#==========================[CBW]===========================
#        if op.type == 11:
#            if wait["QrProtect"] == True:
#                if op.param2 in admin and Bots:
#                    pass
#                if op.param2 not in Bots:
#                    G = random.choice(AST).getGroup(op.param1)
#                    G.preventJoinByTicket = True
#                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#                    random.choice(AST).kickoutFromGroup(op.param1,[op.param3])
#                    random.choice(AST).updateGroup(G)
#==========================[CBW]===========================
        if op.type == 17:
            if wait["Wc"] == True:
                if op.param2 in Bots:
                    return
                ginfo = wN.getGroup(op.param1)
                gm = Message()
                gm.to = op.param1
                gm.text = ("╔═════════════" + "\n║" + wN.getContact(op.param2).displayName + "\n╠═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╠═════════════\n║No Baper,No nakal,No Ngeyel ya..!! \n╚═════════════")
                wN.sendMessage(gm)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc2"] == True:
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
                wN.sendText(op.param1, "╔═════════════" + "\n║" + wN.getContact(op.param2).displayName  +  "\n╠═════════════\n║Nah Baper Dia :v \n╠═════════════\n║Belum di Anu Kayanya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#==========================[CBW]===========================
#        if op.type == 11:
#            if op.param3 == '1':
#                if op.param1 in wait['pname']:
#                    try:
#                        G = wN.getGroup(op.param1)
#                    except:
#                        try:
#                            G = wN1.getGroup(op.param1)
#                        except:
#                            try:
#                                G = wN2.getGroup(op.param1)
#                            except:
#                                try:
#                                    G = wN3.getGroup(op.param1)
#                                except:
#                                    try:
#                                        G = wN4.getGroup(op.param1)
#                                    except:
#                                        try:
#                                            G = wN5.getGroup(op.param1)
#                                        except:
#                                            pass
#                    G.name = wait['pro_name'][op.param1]
#                    try:
#                        wN.updateGroup(G)
#                    except:
#                        try:
#                            wN1.updateGroup(G)
#                        except:
#                            try:
#                                wN2.updateGroup(G)
#                            except:
#                                try:
#                                    wN3.updateGroup(G)
#                                except:
#                                    try:
#                                        wN4.updateGroup(G)
#                                    except:
#                                        try:
#                                            wN5.updateGroup(G)
#                                        except:
#                                            pass
#                    if op.param2 in Bots:
#                        pass
#                    else:
#                        try:
#                            wN1.kickoutFromGroup(op.param1,[op.param2])
#                        except:
#                            try:
#                                wN2.kickoutFromGroup(op.param1,[op.param2])
#                            except:
#                                try:
#                                    wN3.kickoutFromGroup(op.param1,[op.param2])
#                                except:
#                                    try:
#                                        wN4.kickoutFromGroup(op.param1,[op.param2])
#                                    except:
#                                        try:
#                                            wN5.kickoutFromGroup(op.param1,[op.param2])
#                                        except:
#                                            pass
#                                        wN.sendText(op.param1,"please do not change group name-_-")
#==========================[CBW]===========================
        if op.type == 13:
            print op.param3
            if op.param3 in mid1:
                if op.param2 in owner or Bots or admin:
                    wN.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in owner or Bots:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in owner or Bots:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in owner or Bots:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in owner or Bots:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in owner or Bots:
                    wN5.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in mid1:
                if op.param2 in Amid:
                    wN.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Bmid:
                    wN.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Cmid:
                    wN.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Dmid:
                    wN.acceptGroupInvitation(op.param1)
            if op.param3 in mid1:
                if op.param2 in Emid:
                    wN.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Amid:
                if op.param2 in mid1:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Cmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Dmid:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Emid:
                    wN1.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Bmid:
                if op.param2 in mid1:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Amid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Dmid:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Emid:
                    wN2.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Cmid:
                if op.param2 in mid1:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Amid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Emid:
                    wN3.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Dmid:
                if op.param2 in mid1:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Amid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Bmid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Emid:
                    wN4.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
            if op.param3 in Emid:
                if op.param2 in mid1:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Amid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Bmid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Cmid:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    wN5.acceptGroupInvitation(op.param1)
#==========================[CBW]===========================
        if op.type == 13:
            if mid1 in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots or admin or owner:
                        wN.acceptGroupInvitation(op.param1)
                    else:
                        wN.rejectGroupInvitation(op.param1)
                    
  #          if Amid in op.param3:
  #              if wait["autoJoin"] == True:
  #                  if op.param2 in Bots or admin:
  #                      wN1.acceptGroupInvitation(op.param1)
  #                  else:
  #                      wN1.acceptGroupInvitation(op.param1)
  #                      wN1.kickoutFromGroup(op.param1,[op.param2])
  #                      wN1.leaveGroup(op.param1)
  #                  
  #          if Bmid in op.param3:
  #              if wait["autoJoin"] == True:
  #                  if op.param2 in Bots or admin:
  #                      wN2.acceptGroupInvitation(op.param1)
  #                  else:
  #                      wN2.acceptGroupInvitation(op.param1)
  #                      wN2.kickoutFromGroup(op.param1,[op.param2])
  #                      wN2.leaveGroup(op.param1)
  #                  
  #          if Cmid in op.param3:
  #              if wait["autoJoin"] == True:
  #                  if op.param2 in Bots or admin:
  #                      wN3.acceptGroupInvitation(op.param1)
  #                  else:
  #                      wN3.acceptGroupInvitation(op.param1)
  #                      wN3.kickoutFromGroup(op.param1,[op.param2])
  #                      wN3.leaveGroup(op.param1)
  #                  
  #          if Dmid in op.param3:
  #              if wait["autoJoin"] == True:
  #                  if op.param2 in Bots or admin:
  #                      wN4.acceptGroupInvitation(op.param1)
  #                  else:
  #                      wN4.acceptGroupInvitation(op.param1)
  #                      wN4.kickoutFromGroup(op.param1,[op.param2])
  #                      wN4.leaveGroup(op.param1)
  #                  
  #          if Emid in op.param3:
  #              if wait["autoJoin"] == True:
  #                  if op.param2 in Bots or admin:
  #                      wN5.acceptGroupInvitation(op.param1)
  #                  else:
  #                      wN5.acceptGroupInvitation(op.param1)
  #                      wN5.kickoutFromGroup(op.param1,[op.param2])
  #                      wN5.leaveGroup(op.param1)
#==========================[CBW]===========================
        if op.type == 19:
            if op.param3 in admin:
                if op.param2 not in admin:
                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(AST).inviteIntoGroup(op.param1,admin)
                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
                    
            if op.param3 in admin:
                if op.param2 in admin:
                    random.choice(AST).inviteIntoGroup(op.param1,admin)
                    random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
                    
#            if op.param3 in induk:
#                if op.param2 not in Bots:
#                    midd = (mid1)
#                    random.choice(AST).findAndAddContactsByMid(midd)
#                    random.choice(AST).inviteIntoGroup(op.param1,[midd])
#                    wN.acceptGroupInvitation(op.param1)
#                    random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#==========================[CBW]===========================
#        if op.type == 19:
#            if wait["autoKick"] == True:
#                if op.param2 in admin or Bots:
#                    pass
#                else:
#                    try:
#                        wN1.kickoutFromGroup(op.param1,[op.param2])
#                        wN1.inviteIntoGroup(op.param1,[op.param3])
#                    except:
#                        try:
#                            random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#                            random.choice(AST).inviteIntoGroup(op.param1,[op.param3])
#                        except:
#                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
#                if op.param2 in wait["blacklist"]:
#                    pass
#                else:
#                    if op.param2 in admin or Bots:
#                        pass
#                    else:
#                        wait["blacklist"][op.param2] = True
#                if op.param2 in wait["blacklist"]:
#                    pass
#                else:
#                    if op.param2 in admin or Bots:
#                        pass
#                    else:
#                        wait["blacklist"][op.param2] = True
#==========================[CBW]===========================
#                if mid1 in op.param3:
#                    if op.param2 in Bots or admin:
#                        pass
#                    else:
#                        try:
#                            wN1.kickoutFromGroup(op.param1,[op.param2])
#                            wN2.kickoutFromGroup(op.param1,[op.param2])
#                        except:
#                            try:
#                                random.choice(AST).kickoutFromGroup(op.param1,[op.param2])
#                            except:
#                                print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
#                            if op.param2 in wait["blacklist"]:
#                                pass
#                            else:
#                                if op.param2 in Bots:
#                                    pass
#                                else:
#                                    wait["blacklist"][op.param2] = True
#                                    G = wN1.getGroup(op.param1)
#                                    G.preventJoinByTicket = False
#                                    wN1.updateGroup(G)
#                                    Ti = wN1.reissueGroupTicket(op.param1)
#                                    wN.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    wN1.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    wN2.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    wN3.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    wN4.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    wN5.acceptGroupInvitationByTicket(op.param1,Ti)
#                                    X = wN.getGroup(op.param1)
#                                    X.preventJoinByTicket = True
#                                    wN.updateGroup(X)
#                                    if op.param2 in wait["blacklist"]:
#                                        pass
#                                    else:
#                                        if op.param2 in Bots:
#                                            pass
#                                        else:
#                                            wait["blacklist"][op.param2] = True
#

#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message
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
#==========================[CBW]===========================
        if op.type == 26:
            if wait["leaveRoom"] == True:
                wN.leaveRoom(op.param1)
                wN1.leaveRoom(op.param1)
                wN2.leaveRoom(op.param1)
                wN3.leaveRoom(op.param1)
                wN4.leaveRoom(op.param1)
                wN5.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                wN.leaveRoom(op.param1)
                wN1.leaveRoom(op.param1)
                wN2.leaveRoom(op.param1)
                wN3.leaveRoom(op.param1)
                wN4.leaveRoom(op.param1)
                wN5.leaveRoom(op.param1)
#==========================[CBW]===========================
        if op.type == 26:
            msg = op.message
#==========================[CBW]===========================
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    wN.leaveRoom(msg.to)
                    wN1.leaveRoom(msg.to)
                    wN2.leaveRoom(msg.to)
                    wN3.leaveRoom(msg.to)
                    wN4.leaveRoom(msg.to)
                    wN5.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                random.choice(KAC).like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
 #               if wait["wblack"] == True:
 #                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
 #                       random.choice(KAC).sendText(msg.to,"already")
 #                       wait["wblack"] = False
 #                   else:
 #                       wait["commentBlack"][msg.contentMetadata["mid"]] = True
 #                       wait["wblack"] = False
 #                       random.choice(KAC).sendText(msg.to,"decided not to comment")
 #               elif wait["dblack"] == True:
 #                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
 #                       del wait["commentBlack"][msg.contentMetadata["mid"]]
 #                       wN.sendText(msg.to,"deleted")
 #                       wN2.sendText(msg.to,"deleted")
 #                       wN3.sendText(msg.to,"deleted")
 #                       wN4.sendText(msg.to,"deleted")
 #                       wait["dblack"] = False
 #                   else:
 #                       wait["dblack"] = False
 #                       wN.sendText(msg.to,"It is not in the black list")
 #                       wN2.sendText(msg.to,"It is not in the black list")
 #                       wN3.sendText(msg.to,"It is not in the black list")
 #                       wN4.sendText(msg.to,"It is not in the black list")
 #               elif wait["wblacklist"] == True:
 #                   if msg.contentMetadata["mid"] in wait["blacklist"]:
 #                       wN.sendText(msg.to,"already")
 #                       wN2.sendText(msg.to,"already")
 #                       wN3.sendText(msg.to,"already")
 #                       wN4.sendText(msg.to,"already")
 #                       wait["wblacklist"] = False
 #                   else:
 #                       wait["blacklist"][msg.contentMetadata["mid"]] = True
 #                       wait["wblacklist"] = False
 #                       wN.sendText(msg.to,"aded")
 #                       wN2.sendText(msg.to,"aded")
 #                       wN3.sendText(msg.to,"aded")
 #                       wN4.sendText(msg.to,"aded")
 #               elif wait["dblacklist"] == True:
 #                   if msg.contentMetadata["mid"] in wait["blacklist"]:
 #                       del wait["blacklist"][msg.contentMetadata["mid"]]
 #                       wN.sendText(msg.to,"deleted")
 #                       wN2.sendText(msg.to,"deleted")
 #                       wN3.sendText(msg.to,"deleted")
 #                       wN4.sendText(msg.to,"deleted")
 #                       wait["dblacklist"] = False
 #                   else:
 #                       wait["dblacklist"] = False
 #                       wN.sendText(msg.to,"It is not in the black list")
 #                       wN2.sendText(msg.to,"It is not in the black list")
 #                       wN3.sendText(msg.to,"It is not in the black list")
 #                       wN4.sendText(msg.to,"It is not in the black list")
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
                if wait["#timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�10��9�0�16�0�69�0�3�0�4\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)
#==========================[CBW]===========================
            elif msg.text is None:
                return
            elif msg.text in ["help","Help"]:
                if msg.from_ in admin:
					if wait["lang"] == "JP":
						wN.sendText(msg.to,helpMessage)
						random.choice(AST).sendImageWithURL(msg.to, url123)
						random.choice(AST).sendText(msg.to,"↥↥↥↥↥↪ Owner Bots ↩↥↥↥↥↥")
					else:
						random.choice(AST).sendText(msg.to,helpMessage)
#==========================[CBW]===========================
            elif msg.text in ["Key1","key1"]:
                if msg.from_ in admin:
					if wait["lang"] == "JP":
						wN.sendText(msg.to,key1Message)
					else:
						random.choice(AST).sendText(msg.to,key1Message)
#==========================[CBW]===========================
            elif ("#Gn " in msg.text):
                if msg.from_ in admin:
					if msg.toType == 2:
						X = wN.getGroup(msg.to)
						X.name = msg.text.replace("#Gn ","")
						wN.updateGroup(X)
					else:
						wN.sendText(msg.to,"It can't be used besides the group.")
#==========================[CBW]===========================
            elif "#Kick " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("#Kick ","")
					wN.kickoutFromGroup(msg.to,[midd])
#==========================[CBW]===========================
            elif "#Invite " in msg.text:
                if msg.from_ in admin:
					midd = msg.text.replace("#Invite ","")
					wN.findAndAddContactsByMid(midd)
					wN.inviteIntoGroup(msg.to,[midd])
#==========================[CBW]===========================
            elif msg.text in ["Me","me"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg.from_}
                    wN.sendMessage(msg)
           
#==========================[CBW]===========================
            elif msg.text in ["#cancel","#Cancel"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						G = wN.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							wN.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								wN.sendText(msg.to,"No one is inviting")
							else:
								wN.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Can not be used outside the group")
						else:
							wN.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["wN cancel","wN cancel"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						G = wN1.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							wN1.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								wN1.sendText(msg.to,"No one is inviting")
							else:
								wN1.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							wN1.sendText(msg.to,"Can not be used outside the group")
						else:
							wN1.sendText(msg.to,"Not for use less than group")
#==========================[CBW]===========================
            elif msg.text in ["Ourl","Link on","ourl","link on"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						X = wN.getGroup(msg.to)
						X.preventJoinByTicket = False
						wN.updateGroup(X)
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Done")
						else:
							wN.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Can not be used outside the group")
						else:
							wN.sendText(msg.to,"Not for use less than group")
           
#==========================[CBW]===========================
            elif msg.text in ["Curl","Link off","curl","link off"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						X = wN.getGroup(msg.to)
						X.preventJoinByTicket = True
						wN.updateGroup(X)
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Done")
						else:
							wN.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Can not be used outside the group")
						else:
							wN.sendText(msg.to,"Not for use less than group")
            
#==========================[CBW]===========================
            elif msg.text == "#Ginfo":
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = wN.getGroup(msg.to)
                        try:
                            gCreator = ginfo.creator.displayName
                        except:
                            gCreator = "Error"
                        if wait["lang"] == "JP":
                            if ginfo.invitee is None:
                                sinvitee = "0"
                            else:
                                sinvitee = str(len(ginfo.invitee))
                            if ginfo.preventJoinByTicket == True:
                                u = "close"
                            else:
                                u = "open"
                            wN.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                        else:
                            wN.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                    else:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Can not be used outside the group")
                        else:
                            wN.sendText(msg.to,"Not for use less than group")
                        

            elif "Mid" == msg.text:
                if msg.from_ in admin:
					wN.sendText(msg.to,mid1)
#==========================[CBW]===========================
            elif msg.text in ["Undang","undang"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    wN.sendText(msg.to,"send contact")
            elif msg.text in ["Jepit","jepit"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    wN1.sendText(msg.to,"send contact")
            elif msg.text in ["Tarik","tarik"]:
                if msg.from_ in admin:
                    wait['invite'] = True
                    wN2.sendText(msg.to,"send contact")
#==========================[CBW]===========================
            elif "Rename " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Rename ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN.getProfile()
                        profile.displayName = string
                        wN.updateProfile(profile)
                        wN.sendText(msg.to,"Changed " + string + "")

#==========================[CBW]===========================
            elif "Bio " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Bio ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN.getProfile()
                        profile.statusMessage = string
                        wN.updateProfile(profile)
                        wN.sendText(msg.to,"Changed " + string)
#==========================[CBW]===========================
            elif msg.text in ["#Guest on","#guest on"]:
                if msg.from_ in admin:
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger On")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger On")
                        else:
                            wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Guest off","guest off"]:
                if msg.from_ in admin:
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger Off")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger Off")
                        else:
                            wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Kontak on","kontak on"]:
                if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already on")
						else:
							wN.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already on")
						else:
							wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Kontak off","kontak off"]:
                if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already off")
						else:
							wN.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already off")
						else:
							wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Join on","join on"]:
                if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already on")
						else:
							wN.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already on")
						else:
							wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Join off","join off"]:
                if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already off")
						else:
							wN.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already off")
						else:
							wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Gcancel "]:
                if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel ","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								wN.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								wN.sendText(msg.to,"Done")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								wN.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								wN.sendText(msg.to,strnum + "Done")
					except:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Value is wrong")
						else:
							wN.sendText(msg.to,"Bizarre ratings")
#==========================[CBW]===========================
            elif msg.text in ["Leave on","leave on"]:
                if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already on")
						else:
							wN.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"done")
						else:
							wN.sendText(msg.to,"Already on")
#==========================[CBW]===========================
            elif msg.text in ["Leave off","leave off"]:
                if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already off")
						else:
							wN.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"done")
						else:
							wN.sendText(msg.to,"already off")
#==========================[CBW]===========================
            elif msg.text in ["#Share on","#share on"]:
                if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already on")
						else:
							wN.sendText(msg.to,"done")
					else:
						wait["#timeline"] = True
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"done")
						else:
							wN.sendText(msg.to,"Already on")
#==========================[CBW]===========================
            elif msg.text in ["#Share off","share off"]:
                if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"already off")
						else:
							wN.sendText(msg.to,"done")
					else:
						wait["#timeline"] = False
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"done")
						else:
							wN.sendText(msg.to,"Already off")
#==========================[CBW]===========================
            elif msg.text in ["Status","status"]:
                if msg.from_ in admin:
					md = ""
					if wait["contact"] == True: md+="🌂  CONTACT : [✅]\n"
					else: md+="🌂  CONTACT : [❌]\n"
					if wait["autoJoin"] == True: md+="🌂  AUTOJOIN : [✅]\n"
					else: md +="🌂  AUTOJOIN : [❌]\n"
					if wait["autoCancel"]["on"] == True:md+="🌂  GROUP CANCEL :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+="🌂  GROUP CANCEL : [❌]\n"
					if wait["leaveRoom"] == True: md+="🌂  AUTOLEAVE : [✅]\n"
					else: md+="🌂  AUTOLEAVE : [❌]\n"
					if wait["timeline"] == True: md+="🌂  SHARE : [✅]\n"
					else:md+="🌂  SHARE : [❌]\n"
					if wait["autoAdd"] == True: md+="🌂  AUTOADD : [✅]\n"
					else:md+="🌂  AUTOADD : [❌]\n"
					if wait["commentOn"] == True: md+="🌂  COMMENT : [✅]\n"
					else:md+="🌂  COMMENT : [❌]\n"
					if wait["QrProtect"] == True: md+="🌂  PROTECT QR : [✅]\n"
					else:md+="🌂  PROTECT QR : [❌]\n"
					if wait["MProtection"] == True:md+="🌂  PROTECT MEMBER : [✅]\n"
					else:md+="🌂  PROTECT MEMBER : [❌]\n"
					if wait["Protectguest"] == True:md+="🌂  PROTECT GUEST : [✅]\n"
					else:md+="🌂  PROTECT GUEST : [❌]\n"
					if wait["Protectcancel"] == True:md+="🌂  PROTECT CANCEL : [✅]\n"
					else:md+="🌂  PROTECT CANCEL : [❌]\n"
					if wait["autoKick"] == True:md+="🌂  PROTECT KICK : [✅]\n"
					else:md+="🌂  PROTECT KICK : [❌]\n"
					if wait["Wc"] == True: md+="🌂  SAMBUTAN : [✅]\n"
					else:md+="🌂  SAMBUTAN : [❌]\n"
					if wait["Wc2"] == True: md+="🌂  SAMBUTPOTO : [✅]\n"
					else:md+="🌂  SAMBUTPOTO : [❌]\n"
					if wait["Lv"] == True: md+="🌂  PERGI : [✅]\n"
					else:md+="🌂  PERGI : [❌]\n"
					if wait["tag"] == True: md+="🌂  TAG 1 : [✅]\n"
					else:md+="🌂  TAG 1 : [❌]\n"
					if wait["tag2"] == True: md+="🌂  TAG 2 KICK : [✅]\n"
					else:md+="🌂  TAG 2 KICK : [❌]\n"
					wN1.sendText(msg.to,md)

#==========================[CBW]===========================
            elif msg.text in ["Tolak","tolak"]:
                if msg.from_ in admin:
					gid = wN.getGroupIdsInvited()
					gid = wN1.getGroupIdsInvited()
					gid = wN2.getGroupIdsInvited()
					gid = wN3.getGroupIdsInvited()
					gid = wN4.getGroupIdsInvited()
					gid = wN5.getGroupIdsInvited()
					for i in gid:
						wN.rejectGroupInvitation(i)
						wN1.rejectGroupInvitation(i)
						wN2.rejectGroupInvitation(i)
						wN3.rejectGroupInvitation(i)
						wN4.rejectGroupInvitation(i)
						wN5.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						wN.sendText(msg.to,"All invitations have been refused")
					else:
						wN.sendText(msg.to,"All invitations have been refused")
#==========================[CBW]===========================
  #          elif msg.text in ["Add on","add on"]:
 #               if msg.from_ in admin:
#					if wait["autoAdd"] == True:
#						if wait["lang"] == "JP":
#							wN.sendText(msg.to,"Add already on")
#						else:
#							wN.sendText(msg.to,"Add done")
#					else:
#						wait["autoAdd"] = True
#						if wait["lang"] == "JP":
#							wN.sendText(msg.to,"Add done")
#						else:
#							wN.sendText(msg.to,"Add Already on")
#==========================[CBW]===========================
            elif msg.text in ["Add off","add off"]:
                if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Add already off")
						else:
							wN.sendText(msg.to,"Add done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Add done")
						else:
							wN.sendText(msg.to,"Add Already off")
#==========================[CBW]===========================
            elif "#Message change " in msg.text:
                if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change ","")
					wN.sendText(msg.to,"message changed")
					
            elif "#Message add " in msg.text:
                if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add ","")
					if wait["lang"] == "JP":
						wN.sendText(msg.to,"message changed")
					else:
						wN.sendText(msg.to,"done")
#==========================[CBW]===========================
#            elif msg.text in ["Pesan","pesan"]:
#                if msg.from_ in admin:
#					if wait["lang"] == "JP":
#						wN.sendText(msg.to,"message change to\n\n" + wait["message"])
#					else:
#						wN.sendText(msg.to,"The automatic appending information is set as follows\n\n" + wait["message"])
#==========================[CBW]===========================
 #           elif "Comment " in msg.text:
 #               if msg.from_ in admin:
#					c = msg.text.replace("Comment ","")
#					if c in [""," ","\n",None]:
#						wN.sendText(msg.to,"message changed")
#					else:
#						wait["comment"] = c
#						wN.sendText(msg.to,"changed\n\n" + c)
#==========================[CBW]===========================
 #           elif "Add comment " in msg.text:
 #               if msg.from_ in admin:
#					c = msg.text.replace("Add comment ","")
#					if c in [""," ","\n",None]:
#						wN.sendText(msg.to,"String that can not be changed")
#					else:
#						wait["comment"] = c
#						wN.sendText(msg.to,"changed\n\n" + c)
#
#==========================[CBW]===========================
            elif msg.text in ["#Gurl"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						x = wN.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							wN.updateGroup(x)
						gurl = wN.reissueGroupTicket(msg.to)
						wN.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							wN.sendText(msg.to,"Can't be used outside the group")
						else:
							wN.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["wN1 gurl"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						x = wN1.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							wN1.updateGroup(x)
						gurl = wN1.reissueGroupTicket(msg.to)
						wN1.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							wN1.sendText(msg.to,"Can't be used outside the group")
						else:
							wN1.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["wN2 gurl"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						x = wN2.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							wN2.updateGroup(x)
						gurl = wN2.reissueGroupTicket(msg.to)
						wN2.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							wN2.sendText(msg.to,"Can't be used outside the group")
						else:
							wN2.sendText(msg.to,"Not for use less than group")
							
            elif msg.text in ["wN3 gurl"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						x = wN3.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							wN3.updateGroup(x)
						gurl = wN3.reissueGroupTicket(msg.to)
						wN3.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							wN3.sendText(msg.to,"Can't be used outside the group")
						else:
							wN3.sendText(msg.to,"Not for use less than group")

#==========================[CBW]===========================
            elif msg.text in ["Cctv","cctv"]:
                if msg.from_ in admin:
                    wN.sendText(msg.to, "Check sider"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    
            elif msg.text in ["Toong","toong"]:
                if msg.from_ in admin:
                        if msg.to in wait2['readPoint']:
                            if wait2['ROM'][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2['ROM'][msg.to].items():
                                    print rom
                                    chiya += rom[1] + "\n"
                            wN.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal \n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        else:
                            wN.sendText(msg.to, "An already read point has not been set.\n¡¸Cctv¡¹you can send  read point will be created ")

#==========================[CBW]===========================
            elif msg.text.lower() == 'cctv on':
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
                            with open('intip.json', 'w') as fp:
                             json.dump(wait2, fp, sort_keys=True, indent=4)
                             wN.sendText(msg.to,"Cctv sudah menyala silahkan masukan command [Check]")
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
                        with open('intip.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         wN.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                         print wait2

            elif msg.text.lower() == 'cctv off':
                if msg.from_ in admin:
                    if msg.to not in wait2['readPoint']:
                        wN.sendText(msg.to,"Set Reading point tidak di temukan")
                        wN.sendText(msg.to,"Silahkan masukan Command [Cctv on] untuk set point")
                    else:
                        try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                        except:
                              pass
                        wN.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                    
            elif msg.text.lower() == 'check':
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             wN.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
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
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          wN.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        wN.sendText(msg.to, "cctv has not been set.")
#==========================[CBW]===========================
            elif msg.text == "SIDER":
                if msg.from_ in admin:
                    wN.sendText(msg.to, "Lurking Is Starting!! "+ datetime.today().strftime('%H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text in ["Intip","intip","lihat"]:
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
                            wN.sendText(msg.to, "╔═════════════\n║Sider :\n╠═════════════\n║%s\n╠═════════════\n║Reader :\n╠═════════════\n║%s\n╠═════════════\n║In the last seen point:\n║[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
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
                            print "lukers"
                            wN.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                        else:
                            wN.sendText(msg.to, "Ketik => [Cctv] untuk cek sider ketik => [Intip]")
#==========================[CBW]===========================

            elif msg.text in ["#bye","#Bye"]:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = wN.getGroup(msg.to)
                        ginfo = wN1.getGroup(msg.to)
                        ginfo = wN2.getGroup(msg.to)
                        ginfo = wN3.getGroup(msg.to)
                        ginfo = wN4.getGroup(msg.to)
                        ginfo = wN5.getGroup(msg.to)
                        try:
                            wN.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN5.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN2.leaveGroup(msg.to)
                            wN1.leaveGroup(msg.to)
                        except:
                            pass
                        
            elif msg.text in ["#x","#X"]:
                if msg.from_ in owner:
                    if msg.toType == 2:
                        ginfo = wN.getGroup(msg.to)
                        ginfo = wN1.getGroup(msg.to)
                        ginfo = wN2.getGroup(msg.to)
                        ginfo = wN3.getGroup(msg.to)
                        ginfo = wN4.getGroup(msg.to)
                        ginfo = wN5.getGroup(msg.to)
                        try:
                            wN2.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN5.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN2.leaveGroup(msg.to)
                            #wN.leaveGroup(msg.to)
                        except:
                            pass
#==========================[CBW]===========================
            elif msg.text in ["Glist","glist"]:
                if msg.from_ in owner:
                    gid = wN.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "☄ %s  \n" % (wN.getGroup(i).name + " 👥 ▄ [ " + str(len (wN.getGroup(i).members))+" ]")
                    wN.sendText(msg.to, "     ☄ [ ♡List Grup♄ ] ☜\n"+ h +"Total Group ▄" +"[ "+str(len(gid))+" ]")

#==========================[CBW]===========================
            elif msg.text in ["Salam1"]:
                wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif msg.text in ["###Salam3"]:
                if msg.from_ in owner:
                    wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                    wN.sendText(msg.to,"Assalamu'alaikum")
                    wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                    wN.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("###Salam3","")
                        gs = wN.getGroup(msg.to)
                        gs = wN1.getGroup(msg.to)
                        gs = wN2.getGroup(msg.to)
                        gs = wN3.getGroup(msg.to)
                        gs = wN4.getGroup(msg.to)
                        gs = wN5.getGroup(msg.to)
                        wN.sendText(msg.to,"maaf kalo gak sopan")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            wN.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                if target not in Bots:
                                    try:
                                        klist=[wN1,wN2,wN3,wN4,wN5]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        wN.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                        wN.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                        wN.sendText(msg.to,"Nah salamnya jawab sendiri dah")
#==========================[CBW]===========================
            elif "#Kiss " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Kiss ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = wN.getGroup(msg.to)
                    ginfo = wN.getGroup(msg.to)
                    midd2 = (Bmid)
                    gs.findAndAddContactsByMid(midd2)
                    wN.inviteIntoGroup(gs)
                    midd2 = wN.inviteIntoGroup(msg.to,[midd2])
                    wN2.acceptGroupInvitation(msg.to)
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
                                wN2.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                wN2.leaveGroup(msg.to)
                                gs = wN.getGroup(msg.to)

#==========================[CBW]===========================

            elif "#Cium " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                       try:
                          wN1.kickoutFromGroup(msg.to,[target])
                       except:
                          pass
                  
#            elif "zzz " in msg.text:
#                if msg.from_ in admin:
#                    key = eval(msg.contentMetadata["MENTION"])
#                    key["MENTIONEES"][0]["M"]
#                    targets = []
#                    for x in key["MENTIONEES"]:
#                        targets.append(x["M"])
#                    for target in targets:
#                       try:
#                          wN.kickoutFromGroup(msg.to,[target])
#                       except:
#                          pass
#==========================[CBW]===========================
            elif msg.text.lower() == '###':
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN2.sendMessage(msg)
                    wN2.sendMessage(msg)
                    
            elif msg.text.lower() == '####':
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN.sendMessage(msg)
                    wN.sendMessage(msg)
                    wN.sendMessage(msg)
#==========================[CBW]===========================
            elif msg.text in ["#Mode on","#mode on"]:
                if msg.from_ in admin:
                    if wait["QrProtect"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Protect QR On")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Protect QR On")
                        else:
                            wN.sendText(msg.to,"done")
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection On")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection On")
                        else:
                            wN.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        wN.sendText(msg.to,"TURN ON")
                    else:
                        wN.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = wN.getGroup(msg.to).name
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                    if wait["autoKick"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Kick on")
                    else:
                        wait["autoKick"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Already on")
                        else:
                            wN.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Tag On")
                        else:
                            wN.sendText(msg.to,"already on")
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            wN.sendText(msg.to,"Yang ngeTag Kick on")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Yang ngeTag Kick on")
                        else:
                            wN.sendText(msg.to,"Yang ngeTag Kick on")
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger On")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger On")
                        else:
                            wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Mode off","mode off"]:
                if msg.from_ in admin:
                    if wait["QrProtect"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Protect QR Off")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["QrProtect"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Protect QR Off")
                        else:
                            wN.sendText(msg.to,"done")
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection Off")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection Off")
                        else:
                            wN.sendText(msg.to,"done")
                    if msg.to in wait['pname']:
                        wN.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        wN.sendText(msg.to,"ALREADY OFF")
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Protect already oғғ")
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Nayapa yg gabung already oғғ")
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Nayapa yg left already oғғ")
                    if wait["autoKick"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Kick oғғ")
                    else:
                        wait["autoKick"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Kick already oғғ")
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Already Tag off")
                        else:
                            wN.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Tag Off")
                        else:
                            wN.sendText(msg.to,"Already Tag off")
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            wN.sendText(msg.to,"Yang ngeTag Kick off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Yang ngeTag Kick off")
                        else:
                            wN.sendText(msg.to,"Yang ngeTag Kick off")
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger Off")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Guest Stranger Off")
                        else:
                            wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Sider on","sider on"]:
                if msg.from_ in admin:
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                    wait["Sider"] == True
                    wN.sendText(msg.to,"Cek yang ngintip on..!!!")
                
            elif msg.text in ["Sider off","sider off"]:
                if msg.from_ in admin:
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        wait["Sider"] = False
                        wN.sendText(msg.to,"Cek yang ngintip off")
                    else:
                        wN.sendText(msg.to,"Belum Di Set kak")
                        
#==========================[CBW]===========================
 #           elif msg.text in ["Qr on","qr on"]:
 #               if msg.from_ in admin:
 #                   if wait["QrProtect"] == True:
 #                       if wait["lang"] == "JP":
 #                           wN.sendText(msg.to,"Protect QR On")
 #                       else:
 #                           wN.sendText(msg.to,"done")
 #                   else:
 #                       wait["QrProtect"] = True
 #                       if wait["lang"] == "JP":
 #                           wN.sendText(msg.to,"Protect QR On")
 #                       else:
 #                           wN.sendText(msg.to,"done")
 #           elif msg.text in ["Qr off","qr off"]:
 #               if msg.from_ in admin:
 #                   if wait["QrProtect"] == False:
 #                       if wait["lang"] == "JP":
 #                           wN.sendText(msg.to,"Protect QR Off")
 #                       else:
 #                           wN.sendText(msg.to,"done")
 #                   else:
 #                       wait["QrProtect"] = False
 #                       if wait["lang"] == "JP":
#                            wN.sendText(msg.to,"Protect QR Off")
#                        else:
#                            wN.sendText(msg.to,"done")
#==========================[CBW]===========================
            elif msg.text in ["Member on","member on"]:
                if msg.from_ in admin:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection On")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection On")
                        else:
                            wN.sendText(msg.to,"done")
            elif msg.text in ["Member off","member off"]:
                if msg.from_ in admin:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection Off")
                        else:
                            wN.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Member Protection Off")
                        else:
                            wN.sendText(msg.to,"done")
            elif msg.text in ["Respoto on","respoto on"]:
                if msg.from_ in admin:
                    wait["detectMention"] = True
                    wN.sendText(msg.to,"Auto respon tag Pict On")
                
            elif msg.text in ["Respoto off","respoto off"]:
                if msg.from_ in admin:
                    wait["detectMention"] = False
                    wN.sendText(msg.to,"Auto respon tag Pict Off")
#==========================[CBW]===========================
            elif msg.text in ["Creator","creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
					wN.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u9cc2323f5b84f9df880c33aa9f9e3ae1"}
					wN.sendMessage(msg)
#					url = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")#
#					wN.sendImageWithURL(msg.to, url)
#					wN.sendText(msg.to,"MyCreator\nyang bikin Bot ini...!!!")
#==========================[CBW]===========================
            elif msg.text in ["Invite creator"]:
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
 #           elif msg.text in ["Gcreator kick"]:
 #               if msg.from_ in admin:
 #                   ginfo = wN1.getGroup(msg.to)
 #                   gCreator = ginfo.creator.mid
#                    try:
#                        wN1.findAndAddContactsByMid(gCreator)
#                        wN1.kickoutFromGroup(msg.to,[gCreator])
#                        print "success inv gCreator"
#                    except:
#                        pass
#==========================[CBW]===========================
#            elif "Gbc " in msg.text:
#                if msg.from_ in owner:
#                    bctxt = msg.text.replace("Gbc ", "")
#                    n = wN.getGroupIdsJoined()
#                    for manusia in n:
#                        wN.sendText(manusia, (bctxt) + "\
            elif "Pm cast " in msg.text:
                if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = wN.getAllContactIds()
					for manusia in t:
						wN.sendText(manusia,(bctxt))
            elif "Fbc " in msg.text:
                if msg.from_ in owner:
                    bctxt = msg.text.replace("Fbc ", "")
                    t = wN.getAllContactIds()
                    for manusia in t:
                        wN.sendText(manusia, (bctxt))

#==========================[CBW]===========================

            elif msg.text in ["Group on","grup on","Grup on"]:
                if msg.from_ in admin:
                    if msg.to in wait['pname']:
                        wN.sendText(msg.to,"TURN ON")
                    else:
                        wN.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = wN.getGroup(msg.to).name
                        
            elif msg.text in ["Group off","Grup off","grup off"]:
                if msg.from_ in admin:
                    if msg.to in wait['pname']:
                        wN.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        wN.sendText(msg.to,"ALREADY OFF")
#==========================[CBW]===========================
            elif msg.text in ["Turn off","turn off"]:
                if msg.from_ in owner:
                    try:
                        import sys
                        sys.exit()
                        wN.sendText(msg.to, "Bot is Turn Off")
                    except:
                        pass
#==========================[CBW]===========================
            elif msg.text in ["Cancel on","cancel on"]:
                if msg.from_ in admin:
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"proтecт cancel on")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                            
            elif msg.text in ["Cancel off","cancel off"]:
                if msg.from_ in admin:
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"proтecт cancel oғғ")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
            elif msg.text in ["Sambut on","sambut on"]:
                if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                            
            elif msg.text in ["Sambut off","sambut off"]:
                if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
            elif msg.text in ["Sambutpoto on","sambutpoto on"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc2"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                            
            elif msg.text in ["Sambutpoto off","sambutpoto off"]:
                if msg.from_ in admin:
                    if wait["Wc2"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc2"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
            elif msg.text in ["Pergi on","pergi on"]:
                if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already on")
                            
            elif msg.text in ["Pergi off","pergi off"]:
                if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
#            elif msg.text in ["Kick on","kick on"]:
#                if msg.from_ in admin:
#                    if wait["autoKick"] == True:
#                        if wait["lang"] == "JP":
#                            wN.sendText(msg.to,"Kick on")
#                    else:
#                        wait["autoKick"] = True
#                        if wait["lang"] == "JP":
#                            wN.sendText(msg.to,"already on")
#                            
#            elif msg.text in ["Kick off","kick off"]:
#                if msg.from_ in admin:
#                    if wait["autoKick"] == False:
#                        if wait["lang"] == "JP":
#                            wN.sendText(msg.to,"Kick oғғ")
#                    else:
#                        wait["autoKick"] = False
#                        if wait["lang"] == "JP":
#                            wN.sendText(msg.to,"already oғғ")
#==========================[CBW]===========================
            elif "getGroup" in msg.text:
                if msg.from_ in owner:
                    group = wN.getGroup(msg.to)
                    path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                    wN.sendImageWithURL(msg.to, path)
#==========================[CBW]===========================
            elif "#Keluar" in msg.text.split():
                if msg.from_ in owner:
                    ng = msg.text.split().replace("#Keluar","")
                    gid = wN1.getGroupIdsJoined()
                    gid = wN2.getGroupIdsJoined()
                    gid = wN3.getGroupIdsJoined()
                    gid = wN4.getGroupIdsJoined()
                    gid = wN5.getGroupIdsJoined()
                    for i in gid:
                            h = wN1.getGroup(i).name
                            h = wN2.getGroup(i).name
                            h = wN3.getGroup(i).name
                            h = wN4.getGroup(i).name
                            h = wN5.getGroup(i).name
                    if h == ng:
                        wN1.sendText(i,"Bot di paksa keluar oleh owner..!,, MKSH :D..!!!")
                        wN5.leaveGroup(i)
                        wN4.leaveGroup(i)
                        wN3.leaveGroup(i)
                        wN2.leaveGroup(i)
                        wN1.leaveGroup(i)
                        wN.sendText(msg.to,"Success left ["+ h +"] group")
                else:
                    wN.sendText(msg.to,"Khusus Creator/owner")
#==========================[CBW]===========================
            elif msg.text in ["LG"]:
                if msg.from_ in owner:
                    gids = wN.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                        #####gn = wN.getGroup(i).name
                        h += "[•]%s Member\n" % (wN.getGroup(i).name   +"👉"+str(len(wN.getGroup(i).members)))
                        wN.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))

            elif msg.text in ["LG2"]:
                if msg.from_ in owner:
                    gid = wN.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (wN.getGroup(i).name,i)
                        wN.sendText(msg.to,h)
#==========================[CBW]===========================
#            elif "Asupka: " in msg.text:
#                if msg.from_ in owner:
#                    gid = msg.text.replace("Asupka: ","")
#                    if gid == "":
#                        wN1.sendText(msg.to,"Invalid group id")
#                    else:
#                        try:
#                            wN1.findAndAddContactsByMid(msg.from_)
#                            wN2.findAndAddContactsByMid(msg.from_)
#                            wN3.findAndAddContactsByMid(msg.from_)
#                            wN4.findAndAddContactsByMid(msg.from_)
#                            wN5.findAndAddContactsByMid(msg.from_)
#                            wN1.inviteIntoGroup(gid,[msg.from_])
#                            wN2.inviteIntoGroup(gid,[msg.from_])
#                            wN3.inviteIntoGroup(gid,[msg.from_])
#                            wN4.inviteIntoGroup(gid,[msg.from_])
#                            wN5.inviteIntoGroup(gid,[msg.from_])
#                        except:
#                            wN1.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#==========================[CBW]===========================
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot sudah berjalan selama "+waktu(eltime)
                    wN.sendText(msg.to,van)
#==========================[CBW]===========================
            elif msg.text in ["restart","Restart"]:
                if msg.from_ in admin:
                    wN.sendText(msg.to, "Bot Cctv has been restarted")
                    restart_program()
                    print "@Restart"
#==========================[CBW]===========================
            elif msg.text in ["Gcreator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = wN.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    wN.sendText(msg.to, "Group Creator : " + gCreator1)
                    wN.sendMessage(msg)
#==========================[CBW]===========================
            elif msg.text in ["Tag on","tag on"]:
                if msg.from_ in admin:
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Already on")
                        else:
                            wN.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Tag On")
                        else:
                            wN.sendText(msg.to,"already on")
                        
            elif msg.text in ["Tag off","tag off"]:
                if msg.from_ in admin:
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Already off")
                        else:
                            wN.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Tag Off")
                        else:
                            wN.sendText(msg.to,"Already off")
#==========================[CBW]===========================
            elif msg.text in ["Tag2 on","tag2 off"]:
                if msg.from_ in admin:
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Already on")
                        else:
                            wN.sendText(msg.to,"Tag On")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Tag On")
                        else:
                            wN.sendText(msg.to,"already on")
                            
            elif msg.text in ["Tag2 off","tag2 off"]:
                if msg.from_ in admin:
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Already off")
                        else:
                            wN.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Tag Off")
                        else:
                            wN.sendText(msg.to,"Already off")
#==========================[CBW]===========================
            elif msg.text in ["Auto on","auto on"]:
                if msg.from_ in admin:
                    if wait["auto"] == True:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Bot join on")
                        else:
                            wN.sendText(msg.to,"Bot join On")
                    else:
                        wait["auto"] = True
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Bot join On")
                        else:
                            wN.sendText(msg.to,"Bot join On")
                            
            elif msg.text in ["Auto off","auto off"]:
                if msg.from_ in admin:
                    if wait["auto"] == False:
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Bot join off")
                        else:
                            wN.sendText(msg.to,"Bot join off")
                    else:
                        wait["auto"] = False
                        if wait["lang"] == "JP":
                            wN.sendText(msg.to,"Bot join off")
                        else:
                            wN.sendText(msg.to,"Bot join off")
#==========================[CBW]===========================
            elif "admin @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = wN.getGroup(msg.to)
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
                        wN.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                wN.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    wN.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                    wN.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")
#==========================[CBW]===========================
            elif "Hapus admin @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Hapus admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = wN.getGroup(msg.to)
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
                        wN.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                wN.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    wN.sendText(msg.to,"Command DiTolak")
                    wN.sendText(msg.to,"Admin Tidak Bisa Menggunakan")
#==========================[CBW]===========================
            elif msg.text in ["Adminlist","admlist"]:
                if msg.from_ in admin:
                    if admin == []:
                        wN.sendText(msg.to,"The adminlist is empty")
                    else:
                        wN.sendText(msg.to,"Sabar Dikit Boss CBW.....")
                        mc = ""
                        for mi_d in admin:
                            mc += "☄ " +wN.getContact(mi_d).displayName + "\n"
                        wN.sendText(msg.to,mc)
                        print "[Command]Stafflist executed"

#==========================[CBW]===========================
            elif msg.text in ["Time"]:
                if msg.from_ in admin:
                    timeNow = datetime.now()
                    timeHours = datetime.strftime(timeNow,"(%H:%M)")
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    inihari = datetime.today()
                    hr = inihari.strftime('%A')
                    bln = inihari.strftime('%B')
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                    wN.sendText(msg.to, rst)
                    #client.sendText(msg.to, rst)


#==========================[CBW]===========================
#            elif msg.text in ["Kibar","kibar"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
#                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
#                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
#                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
#                    wN.sendImageWithURL(msg.to, url)
#                    wN.sendImageWithURL(msg.to, url1)
#                    wN.sendImageWithURL(msg.to, url6)
#                    wN.sendImageWithURL(msg.to, url7)
#==========================[CBW]===========================
            elif msg.text in ["setview","Setview"]:
                if msg.from_ in admin:
                    subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                    wN.sendText(msg.to, "Checkpoint checked!")
                    print "@setview"

            elif msg.text in ["viewseen","Viewseen"]:
                if msg.from_ in admin:
                    lurkGroup = ""
                    dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                    with open('dataSeen/'+msg.to+'.txt','r') as rr:
                        contactArr = rr.readlines()
                        for v in xrange(len(contactArr) -1,0,-1):
                            num = re.sub(r'\n', "", contactArr[v])
                            contacts.append(num)
                            pass
                        contacts = list(set(contacts))
                        for z in range(len(contacts)):
                            arg = contacts[z].split('|')
                            userList.append(arg[0])
                            timelist.append(arg[1])
                        uL = list(set(userList))
                        for ll in range(len(uL)):
                            try:
                                getIndexUser = userList.index(uL[ll])
                                timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                                recheckData.append(userList[getIndexUser])
                            except IndexError:
                                cName.append('nones')
                                pass
                        contactId = wN.getContacts(recheckData)
                        for v in range(len(recheckData)):
                            dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                            pass
                        if len(dataResult) > 0:
                            tukang = "List Viewer\n*"
                            grp = '\n* '.join(str(f) for f in dataResult)
                            total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                            wN.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        else:
                            wN.sendText(msg.to, "Belum ada viewers")
                        print "@viewseen"

#==========================[CBW]===========================
            elif msg.text in ["Respon","respon"]:
                if msg.from_ in admin:
					wN.sendText(msg.to,"Aktif Sayang...(^_^)")
            elif msg.text in ["Absen","absen"]:
                if msg.from_ in admin:
                    wN1.sendText(msg.to,"💡💡💡👉 Bot Hadir..!!!")
#==========================[CBW]===========================
            elif msg.text in ["#pulang","#Pulang"]:
                if msg.from_ in owner:
                    gid = wN1.getGroupIdsJoined()
                    gid = wN2.getGroupIdsJoined()
                    gid = wN3.getGroupIdsJoined()
                    gid = wN4.getGroupIdsJoined()
                    gid = wN5.getGroupIdsJoined()
                    for i in gid:
                        wN1.sendText(i,"Bye~Bye\n\nBots Dipaksa Keluar oleh Owner Bots...!!!")
                        wN.sendImageWithURL(i, url123)
                        wN1.leaveGroup(i)
                        wN2.leaveGroup(i)
                        wN3.leaveGroup(i)
                        wN4.leaveGroup(i)
                        wN5.leaveGroup(i)
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        wN1.sendText(msg.to,"He declined all invitations")
#==========================[CBW]===========================
            elif "Bcgrup: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Bcgrup: ","")
                    gid = wN.getGroupIdsJoined()
                    for i in gid:
                        wN.sendText(i,"╠═════[BROADCAST]═════╣\n\n"+bc+"\n\nMAAF BROADCAST!!\n\n=>>line://ti/p/~CBWsthea\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")
                        wN.sendText(msg.to, "Brodcastgrup sukses")
#==========================[CBW]===========================
            elif msg.text in ["Sp","sp"]:
                if msg.from_ in admin:
					start = time.time()
					wN1.sendText(msg.to, "Proses..🔥🔥🔥")
					elapsed_time = time.time() - start
					wN1.sendText(msg.to, "%s/Detik" % (elapsed_time))
					
            elif msg.text in ["Speed","speed"]:
                if msg.from_ in admin:
					start = time.time()
					wN.sendText(msg.to, "Proses..🔥🔥🔥")
					elapsed_time = time.time() - start
					wN.sendText(msg.to, "%s/Detik" % (elapsed_time))
#==========================[CBW]===========================
            elif msg.text in ["Batal","batal"]:
                if msg.from_ in admin:
					if msg.toType == 2:
						X = wN.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							wN.cancelGroupInvitation(msg.to, gInviMids)
#==========================[CBW]===========================
            elif "#cium " in msg.text:
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

            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    wN1.removeAllMessages(msg.to)
                    wN2.removeAllMessages(msg.to)
                    wN3.removeAllMessages(msg.to)
                    wN4.removeAllMessages(msg.to)
                    wN5.removeAllMessages(msg.to)
                    wN.sendText(msg.to,"Removed all chat Finish")
#==========================[CBW]===========================
            elif msg.text in ["#muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN1.sendMessage(msg)
                    
            elif msg.text in ["#Muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN.sendMessage(msg)
#==========================[CBW]===========================
            elif "spamtag @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Cctv spamtag @","")
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
                        
            elif "Spamtag @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
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
#==========================[CBW]===========================
            elif "Spamkontak @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Cctv spamkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            wN1.sendText(msg.to, "║╠❂➣ Spam sedang di Proses...!!!")
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
                            wN1.sendText(msg.to, "║╠❂➣ Done.. Selesai di Spam...!!!")
                            print " Spammed !"
                            
            elif "Spamkontak @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Spamkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            wN.sendText(msg.to, "║╠❂➣ Spam sedang di Proses...!!!")
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(g.mid,'spam')
                            wN.sendText(msg.to, "║╠❂➣ Done.. Selesai di Spam...!!!")
                            print " Spammed !"
#==========================[CBW]===========================

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
                            Np = wN.getContact(op.param2).pictureStatus
                            Np = wN.getContact(op.param2).pictureStatus
                            Np = wN.getContact(op.param2).pictureStatus
                            Np = wN.getContact(op.param2).pictureStatus
                            Np = wN.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        wN.sendText(op.param1, "Hallo.. " + "☞ " + nick[0] + " ☜" + "\nNah jangan ngintip mulu 😁. . .\nGabung Chat yux 😉")
                                        wN.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        wN.sendText(op.param1, "Hallo.. " + "☞ " + nick[1] + " ☜" + "\nJangan ngintip.. 😏. . .\nMasuk  ayox... 😆😂😛")
                                        wN.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    wN.sendText(op.param1, "hallo.. " + "☞ " + Name + " ☜" + "\nJangan ngintip aja\nMasuk gabung chat ya...😋 😝")
                                    wN.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
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

while True:
    try:
        Ops = wN.fetchOps(wN.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(wN.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            wN.Poll.rev = max(wN.Poll.rev, Op.revision)
            bot(Op)
