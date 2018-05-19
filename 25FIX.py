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

wN1 = CBW.LINE()
#wN1.login(qr=True)
wN1.login(token="Ep7wEn7bwlYOcQ4Tw3ib.tpBkkcnzdHTzh8qoh1/nsW.LNLJUL5BO1fP5J1tATqDVPV/DLW7Vzh7JerDeToQiD4=")#1
wN1.loginResult()

wN2 = CBW.LINE()
#wN2.login(qr=True)
wN2.login(token="EpodEadlAuXlJHT9eG9e.FHoeJRm44Jh+J9ym4CoR3G.6c8+gUpHreSd1OXQalUKspWoQhW1WRoSCVVbUrp2XKM=")#2
wN2.loginResult()

wN3 = CBW.LINE()
#wN3.login(qr=True)
wN3.login(token="EppUBQG8bA8fgKCIaZD8.BzD2C6X5O4D1tQw8zJzYwa.54YCnVsRqEncGb0ADWvWJKY2IVvB4mGl3ULcpuS84XI=")#3
wN3.loginResult()

wN4 = CBW.LINE()
#wN4.login(qr=True)
wN4.login(token="EpS5QcOnyaYp3ZqYZjdb.fDxTRFxYJIH0z/UUxuNGIW.54gFRc3ErViUm7Y91Akw3rrn9HRrEivCjBicc9DKD5U=")#4
wN4.loginResult()

wN5 = CBW.LINE()
#wN5.login(qr=True)
wN5.login(token="Ep9ilhAschXQI3Fx62pb.G1U1Z383iLTuKypXO8LEAW.aEbkmZPK/5fjM4ZlDdsXeCgbIytMsErU5Awt4G+2GnI=")#5
wN5.loginResult()

wN6 = CBW.LINE()
#wN6.login(qr=True)
wN6.login(token="EpX3jO18ifUahFJIoaB1.uazgSO9bWUxAzB5DsFngeq.KEZnq4tyeDRNSxJyUFkOAmXe7rE9WSKGJcGetb4HSJI=")#6
wN6.loginResult()

wN7 = CBW.LINE()
#wN7.login(qr=True)
wN7.login(token="Epr9XR3vQZSNfogHUFZ4.qShqrjgOA9e7LQrRkAjMja.jqMncQ47JnhSJ5+Pnir3KBl4UY4TfxiEeIgGmTq/C2s=")#7
wN7.loginResult()

wN8 = CBW.LINE()
#wN8.login(qr=True)
wN8.login(token="EpOYg88v3OVU8vl6W4wf.kuWQjPuunx29CPqQAL3PlW.YZDi/jb0Nn2xn//NwyMD9kVIOUAMWG3ma24WZYN0gHY=")#8
wN8.loginResult()

wN9 = CBW.LINE()
#wN9.login(qr=True)
wN9.login(token="Ep07zQEWTPjQOyKlxV97.6Y0z8Cdtymvu1mBZSliFvW.hdm7TnRBEHho0YuE++SifY78jWWS8BG7UeLfRG0CiLc=")#9
wN9.loginResult()

wN10 = CBW.LINE()
#wN10.login(qr=True)
wN10.login(token="EpGQW5Rqi62ArNDyqDf6.z65SpYjOhBrg/cPupDfXzG.sX/OHjbqT5PRgE0d0g6TuM5e9S7KqHJ1Ckyse+PhNwA=")#10
wN10.loginResult()

wN11 = CBW.LINE()
#wN11.login(qr=True)
wN11.login(token="Ep0AAwrkRJcgmDLyVD79.MuVPKSPTNJEmucSTO0EgMq.y/AY76kbpKgapbEM2If+yYh3SxBgMeuSDl6Nz9S7koc=")#11
wN11.loginResult()

wN12 = CBW.LINE()
#wN12.login(qr=True)
wN12.login(token="EpcTOVZHiUX1gTDSTYk0.rp3iy6AHhJAe6ULdRlS0Ga.Btx0aotiKeXVs6Kj+eXVOQCMNN20QY68egJiWMOVLm0=")#12
wN12.loginResult()

wN13 = CBW.LINE()
#wN13.login(qr=True)
wN13.login(token="EpSxQj58O78LTOEVDYS1.khW7clxXW6mpPpUIVAvOaq.N66BEQH4drJAzD/fX1bm4mGqgMX9ect9RPxyrJVbcfk=")#13
wN13.loginResult()

wN14 = CBW.LINE()
#wN14.login(qr=True)
wN14.login(token="Ep1oJF9PiITUgdZx7Y26.cFCuv1sJG0t3IQ+DSFO4XG.wwBSNStnbOgIXVct+cbLZvjQY4iKZf/2hW4EJliVX+4=")#14
wN14.loginResult()

wN15 = CBW.LINE()
#wN15.login(qr=True)
wN15.login(token="EpmpGTZ9iBsiCplV90xb.dGfnLg8q+kntKKhBdBzBwW.vBmz6Glxybki6q8AznOY64BWNwNh+BtchI0aaQIuqYU=")#15
wN15.loginResult()

wN16 = CBW.LINE()
#wN16.login(qr=True)
wN16.login(token="EpaLjYoOEs3EMgcuc5G8.1uAIjNn0Al6lg86ClXf9Ya.dQ++4ikf46ktcom51cZLZaZsED9kPbGxtmumBPgDU94=")#16
wN16.loginResult()

wN17 = CBW.LINE()
#wN17.login(qr=True)
wN17.login(token="EpY7brOnrDAKdDvuAU9f.IoDAMDiyLjtmaSKHNfAzxW.vV232eJ9fK5scQ68jnRpj2h/1yB+9NHBf22xmYUn+HA=")#17
wN17.loginResult()

wN18 = CBW.LINE()
#wN18.login(qr=True)
wN18.login(token="Ep8BkAsDKwp9EzxcbWgf.LxQf3n4J+lan9MzgEjTIpW.ic4kX8a5xkeYTR0wpRMXLYKBc9Ukb1OvEpUseUETxsg=")#18
wN18.loginResult()

wN19 = CBW.LINE()
#wN19.login(qr=True)
wN19.login(token="EpE5P9HJPWorNwu1I5Y1.hICAsHWiPbwKnTM3M9rcyq.mE/YBr/5Dee+xAo16F5LmitwcvgyciJRneclfSqQlNQ=")#19
wN19.loginResult()

wN20 = CBW.LINE()
#wN20.login(qr=True)
wN20.login(token="Ep6AwuXwxqH13NbMFP59.AlEHjWlxhgV58LvmsjqU2q.hbG19UPTzhFnxN76outDIySfYrWTGWBOgA8xfkSkwGM=")#20
wN20.loginResult()

wN21 = CBW.LINE()
#wN21.login(qr=True)
wN21.login(token="Epxfhuif8NZKTeE6FEid.FyVRtKEBLFEuaU36x7sO3q.zcaRmc4hwbfSWN2Mfjrrjii1tIt7Psr2n4C2vyVos9k=")#21
wN21.loginResult()

wN22 = CBW.LINE()
#wN22.login(qr=True)
wN22.login(token="Ep7VzXde1cojIWATuQda.00XSIVYDkUfkAzZrR4UzYG.p9pHDTGzraktsEQvyT9Z1BV8XpyOgkH2RI3Kc/JObN0=")#22
wN22.loginResult()

wN23 = CBW.LINE()
#wN23.login(qr=True)
wN23.login(token="EpOhV0ioHMDpdZ51XJ0e.MGPgtY0Gwcc0Q7kVqfPgtG.D5NnveMkZoLOFO258TxEfB5miUedrYJCkLiTldn2IOM=")#23
wN23.loginResult()

wN24 = CBW.LINE()
#wN24.login(qr=True)
wN24.login(token="EpinftLoJAoWdLrbdf87.L1mYXPq7tk5jIxn4GditXW.MHkouGpChvtzFxOJ3ysDr3pfTv5UOTpePhVKPffN+i8=")#24
wN24.loginResult()

wN25 = CBW.LINE()
#wN25.login(qr=True)
wN25.login(token="Epssh8LRCA13pJayrYD5.nldM1B6yM6kQXJdxg2Ikfq.WC4WnVSPFTYkEei2XhLghIf78b3jRzkZLb7aS87/23U=")#25
wN25.loginResult()


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
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
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
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
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
║╠❂➣CBW/. (manggil bot)
║╠❂➣Kabur all
║╠❂➣CBW bye
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
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
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
║tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt
╠═════════════
║   ☔ 🎃w🎃N🎃 ☔
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
║╠❂➣Bot kemari
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
║╠❂➣Kr
║╠❂➣Salam3
║╚════════════
╚═════════════"""

KAC=[wN1,wN1,wN2,wN3,wN4,wN5,wN6,wN7,wN8,wN9,wN10,wN11,wN12,wN13,wN14,wN15,wN16,wN17,wN18,wN19,wN20,wN21,wN22,wN23,wN24,wN25]
mid = wN1.getProfile().mid
mid2 = wN2.getProfile().mid
mid3 = wN3.getProfile().mid
mid4 = wN4.getProfile().mid
mid5 = wN5.getProfile().mid
mid6 = wN6.getProfile().mid
mid7 = wN7.getProfile().mid
mid8 = wN8.getProfile().mid
mid9 = wN9.getProfile().mid
mid10 = wN10.getProfile().mid
mid11 = wN10.getProfile().mid
mid12 = wN12.getProfile().mid
mid13 = wN13.getProfile().mid
mid14 = wN14.getProfile().mid
mid15 = wN15.getProfile().mid
mid16 = wN16.getProfile().mid
mid17 = wN17.getProfile().mid
mid18 = wN18.getProfile().mid
mid19 = wN19.getProfile().mid
mid20 = wN20.getProfile().mid
mid21 = wN21.getProfile().mid
mid22 = wN22.getProfile().mid
mid23 = wN23.getProfile().mid
mid24 = wN24.getProfile().mid
mid25 = wN25.getProfile().mid

Bots=[mid,mid2,mid3,mid4,mid5,mid6,mid7,mid8,mid9,mid10,mid11,mid12,mid13,mid14,mid15,mid16,mid17,mid18,mid19,mid20,mid21,mid22,mid23,mid24,mid25]
owner=["uc301fa8f0962f52b1f2d83dc251589cb","u986c71616f66e33497b7426fb613cf03"]
admin=['uc301fa8f0962f52b1f2d83dc251589cb','u986c71616f66e33497b7426fb613cf03','uaecc760911be47db56c5d0cc3ae14a27','ufdedeacc6a6e547f11f36078a15acc7d','ued6685c48b974db65601f3df45ea8c88','udb7654c85bf03026c67eb58484a01e19','u0018100c35195db59f8e3e54f1c8458d',mid,mid2,mid3,mid4,mid5,mid6,mid7,mid8,mid9,mid10,mid11,mid12,mid13,mid14,mid15,mid16,mid17,mid18,mid19,mid20,mid21,mid22,mid23,mid24,mid25]

wait = {
    'likeOn':False,
    'alwayRead':True,
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
    "cNames6":"↝↬₡αβ↫↜",
    "cNames7":"↝↬₡αβ↫↜",
    "cNames8":"↝↬₡αβ↫↜",
    "cNames9":"↝↬₡αβ↫↜",
    "cNames10":"↝↬₡αβ↫↜",
    "cNames11":"↝↬₡αβ↫↜",
    "cNames12":"↝↬₡αβ↫↜",
    "cNames13":"↝↬₡αβ↫↜",
    "cNames14":"↝↬₡αβ↫↜",
    "cNames15":"↝↬₡αβ↫↜",
    "cNames16":"↝↬₡αβ↫↜",
    "cNames17":"↝↬₡αβ↫↜",
    "cNames18":"↝↬₡αβ↫↜",
    "cNames19":"↝↬₡αβ↫↜",
    "cNames20":"↝↬₡αβ↫↜",
    "cNames21":"↝↬₡αβ↫↜",
    "cNames22":"↝↬₡αβ↫↜",
    "cNames23":"↝↬₡αβ↫↜",
    "cNames24":"↝↬₡αβ↫↜",
    "cNames25":"↝↬₡αβ↫↜",
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
contact = wN11.getProfile()
mybackup = wN11.getProfile()
contact = wN12.getProfile()
mybackup = wN12.getProfile()
contact = wN13.getProfile()
mybackup = wN13.getProfile()
contact = wN14.getProfile()
mybackup = wN14.getProfile()
contact = wN15.getProfile()
mybackup = wN15.getProfile()
contact = wN16.getProfile()
mybackup = wN16.getProfile()
contact = wN17.getProfile()
mybackup = wN17.getProfile()
contact = wN18.getProfile()
mybackup = wN18.getProfile()
contact = wN19.getProfile()
mybackup = wN19.getProfile()
contact = wN20.getProfile()
mybackup = wN20.getProfile()
contact = wN21.getProfile()
mybackup = wN21.getProfile()
contact = wN22.getProfile()
mybackup = wN22.getProfile()
contact = wN23.getProfile()
mybackup = wN23.getProfile()
contact = wN24.getProfile()
mybackup = wN24.getProfile()
contact = wN25.getProfile()
mybackup = wN25.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


mulai = time.time()

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

#def autolike():
#			for zx in range(0,100):
#				hasil = wN1.activity(limit=100)
#				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#					try:
#						wN1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#						wN1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By TobyBots!!\nID LINE : line://ti/p/~tobyg74\nIG : instagram.com/tobygaming74")
#						print "DiLike"
#					except:
#							pass
#				else:
#						print "Sudah DiLike"
#			time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

#def autolike():
#    for zx in range(0,100):
#      hasil = wN1.activity(limit=100)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          wN1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#          wN1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by CBW ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
#          print "Like"
#        except:
#          pass
#      else:
#          print "Already Liked"
#time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

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
            if wait['autoAdd'] == True:
                wN1.findAndAddContactsByMid(op.param1)
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    wN1.sendText(op.param1,str(wait['message']))
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        wN1.sendText(msg.to,text)
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
            if op.param3 in mid6:
                if op.param2 in owner:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in owner:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in owner:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in owner:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in owner:
                    wN10.acceptGroupInvitation(op.param1)     
            if op.param3 in mid11:
                if op.param2 in owner:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in owner:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in owner:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in owner:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in owner:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in owner:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in owner:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in owner:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in owner:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in owner:
                    wN20.acceptGroupInvitation(op.param1)  
            if op.param3 in mid21:
                if op.param2 in owner:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in owner:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in owner:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in owner:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in owner:
                    wN25.acceptGroupInvitation(op.param1)        
#----------------
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
            if op.param3 in mid:
                if op.param2 in mid6:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid7:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid8:
                    wN1.acceptGroupInvitation(op.param1)       
            if op.param3 in mid:
                if op.param2 in mid9:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid10:
                    wN1.acceptGroupInvitation(op.param1)   
            if op.param3 in mid:
                if op.param2 in mid11:
                    wN1.acceptGroupInvitation(op.param1)         
            if op.param3 in mid:
                if op.param2 in mid12:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid13:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid14:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid15:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid16:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid17:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid18:
                    wN1.acceptGroupInvitation(op.param1)       
            if op.param3 in mid:
                if op.param2 in mid19:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid20:
                    wN1.acceptGroupInvitation(op.param1)    
            if op.param3 in mid:
                if op.param2 in mid20:
                    wN1.acceptGroupInvitation(op.param1)         
            if op.param3 in mid:
                if op.param2 in mid22:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid23:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid24:
                    wN1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid25:
                    wN1.acceptGroupInvitation(op.param1)
         
#-----
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
            if op.param3 in mid2:
                if op.param2 in mid6:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid7:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid8:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid9:
                    wN2.acceptGroupInvitation(op.param1)        
            if op.param3 in mid2:
                if op.param2 in mid10:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid11:
                    wN2.acceptGroupInvitation(op.param1)        
            if op.param3 in mid2:
                if op.param2 in mid12:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid13:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid14:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid15:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid16:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid17:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid18:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid19:
                    wN2.acceptGroupInvitation(op.param1)        
            if op.param3 in mid2:
                if op.param2 in mid20:
                    wN2.acceptGroupInvitation(op.param1)     
            if op.param3 in mid2:
                if op.param2 in mid21:
                    wN2.acceptGroupInvitation(op.param1)            
            if op.param3 in mid2:
                if op.param2 in mid22:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid23:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid24:
                    wN2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid25:
                    wN2.acceptGroupInvitation(op.param1)
                   
#--------                    
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
            if op.param3 in mid3:
                if op.param2 in mid6:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid7:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid8:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid9:
                    wN3.acceptGroupInvitation(op.param1)        
            if op.param3 in mid3:
                if op.param2 in mid10:
                    wN3.acceptGroupInvitation(op.param1)  
            if op.param3 in mid3:
                if op.param2 in mid11:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid12:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid13:
                    wN3.acceptGroupInvitation(op.param1)        
            if op.param3 in mid3:
                if op.param2 in mid14:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid15:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid16:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid17:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid18:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid19:
                    wN3.acceptGroupInvitation(op.param1)        
            if op.param3 in mid3:
                if op.param2 in mid20:
                    wN3.acceptGroupInvitation(op.param1)            
            if op.param3 in mid3:
                if op.param2 in mid21:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid22:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid23:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid24:
                    wN3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid25:
                    wN3.acceptGroupInvitation(op.param1)
    #----------                         
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
            if op.param3 in mid4:
                if op.param2 in mid6:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid7:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid8:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid9:
                    wN4.acceptGroupInvitation(op.param1)        
            if op.param3 in mid4:
                if op.param2 in mid10:
                    wN4.acceptGroupInvitation(op.param1)        
            if op.param3 in mid4:
                if op.param2 in mid11:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid12:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid13:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid14:
                    wN4.acceptGroupInvitation(op.param1)        
            if op.param3 in mid4:
                if op.param2 in mid15:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid16:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid17:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid18:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid19:
                    wN4.acceptGroupInvitation(op.param1)        
            if op.param3 in mid4:
                if op.param2 in mid20:
                    wN4.acceptGroupInvitation(op.param1)        
            if op.param3 in mid4:
                if op.param2 in mid21:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid22:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid23:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid24:
                    wN4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid25:
                    wN4.acceptGroupInvitation(op.param1)
               
#--------                         
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
            if op.param3 in mid5:
                if op.param2 in mid6:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid7:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid8:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid9:
                    wN5.acceptGroupInvitation(op.param1)   
            if op.param3 in mid5:
                if op.param2 in mid10:
                    wN5.acceptGroupInvitation(op.param1)  
            if op.param3 in mid5:
                if op.param2 in mid11:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid12:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid13:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid14:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid15:
                    wN5.acceptGroupInvitation(op.param1)        
            if op.param3 in mid5:
                if op.param2 in mid16:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid17:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid18:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid19:
                    wN5.acceptGroupInvitation(op.param1)   
            if op.param3 in mid5:
                if op.param2 in mid20:
                    wN5.acceptGroupInvitation(op.param1)  
            if op.param3 in mid5:
                if op.param2 in mid21:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid22:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid23:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid24:
                    wN5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid25:
                    wN5.acceptGroupInvitation(op.param1)
          
#------------                    
            if op.param3 in mid6:
                if op.param2 in mid:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid2:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid3:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid4:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid5:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid7:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid8:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid9:
                    wN6.acceptGroupInvitation(op.param1)   
            if op.param3 in mid6:
                if op.param2 in mid10:
                    wN6.acceptGroupInvitation(op.param1)   
            if op.param3 in mid6:
                if op.param2 in mid11:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid12:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid13:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid14:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid15:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid116:
                    wN6.acceptGroupInvitation(op.param1)       
            if op.param3 in mid6:
                if op.param2 in mid17:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid18:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid19:
                    wN6.acceptGroupInvitation(op.param1)   
            if op.param3 in mid6:
                if op.param2 in mid20:
                    wN6.acceptGroupInvitation(op.param1)       
            if op.param3 in mid6:
                if op.param2 in mid21:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid22:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid23:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid24:
                    wN6.acceptGroupInvitation(op.param1)
            if op.param3 in mid6:
                if op.param2 in mid25:
                    wN6.acceptGroupInvitation(op.param1)
                  
#------------  
            if op.param3 in mid7:
                if op.param2 in mid:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid2:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid3:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid4:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid5:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid6:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid8:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid9:
                    wN7.acceptGroupInvitation(op.param1)   
            if op.param3 in mid7:
                if op.param2 in mid10:
                    wN7.acceptGroupInvitation(op.param1)   
            if op.param3 in mid7:
                if op.param2 in mid11:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid12:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid13:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid14:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid15:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid16:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid17:
                    wN7.acceptGroupInvitation(op.param1)        
            if op.param3 in mid7:
                if op.param2 in mid18:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid19:
                    wN7.acceptGroupInvitation(op.param1)   
            if op.param3 in mid7:
                if op.param2 in mid20:
                    wN7.acceptGroupInvitation(op.param1) 
            if op.param3 in mid7:
                if op.param2 in mid21:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid22:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid23:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid24:
                    wN7.acceptGroupInvitation(op.param1)
            if op.param3 in mid7:
                if op.param2 in mid25:
                    wN7.acceptGroupInvitation(op.param1)
            
#------------                              
            if op.param3 in mid8:
                if op.param2 in mid:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid2:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid3:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid4:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid5:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid6:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid7:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid9:
                    wN8.acceptGroupInvitation(op.param1)   
            if op.param3 in mid8:
                if op.param2 in mid10:
                    wN8.acceptGroupInvitation(op.param1)  
            if op.param3 in mid8:
                if op.param2 in mid11:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid12:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid13:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid14:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid15:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid16:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid17:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid19:
                    wN8.acceptGroupInvitation(op.param1)         
            if op.param3 in mid8:
                if op.param2 in mid19:
                    wN8.acceptGroupInvitation(op.param1)   
            if op.param3 in mid8:
                if op.param2 in mid20:
                    wN8.acceptGroupInvitation(op.param1) 
            if op.param3 in mid8:
                if op.param2 in mid21:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid22:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid23:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid24:
                    wN8.acceptGroupInvitation(op.param1)
            if op.param3 in mid8:
                if op.param2 in mid25:
                    wN8.acceptGroupInvitation(op.param1)  
#------------                                                       
            if op.param3 in mid9:
                if op.param2 in mid:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid2:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid3:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid4:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid5:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid6:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid7:
                    wN9.acceptGroupInvitation(op.param1)   
            if op.param3 in mid9:
                if op.param2 in mid8:
                    wN9.acceptGroupInvitation(op.param1) 
            if op.param3 in mid9:
                if op.param2 in mid10:
                    wN9.acceptGroupInvitation(op.param1)    
            if op.param3 in mid9:
                if op.param2 in mid11:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid12:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid13:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid14:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid15:
                   wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid16:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid17:
                    wN9.acceptGroupInvitation(op.param1)   
            if op.param3 in mid9:
                if op.param2 in mid18:
                    wN9.acceptGroupInvitation(op.param1) 
            if op.param3 in mid9:
                if op.param2 in mid19:
                    wN9.acceptGroupInvitation(op.param1)         
            if op.param3 in mid9:
                if op.param2 in mid20:
                    wN9.acceptGroupInvitation(op.param1)             
            if op.param3 in mid9:
                if op.param2 in mid21:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid22:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid23:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid24:
                    wN9.acceptGroupInvitation(op.param1)
            if op.param3 in mid9:
                if op.param2 in mid25:
                    wN9.acceptGroupInvitation(op.param1)
            
#--------
            if op.param3 in mid10:
                if op.param2 in mid:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid2:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid3:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid4:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid5:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid6:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid7:
                    wN10.acceptGroupInvitation(op.param1)   
            if op.param3 in mid10:
                if op.param2 in mid8:
                    wN10.acceptGroupInvitation(op.param1) 
            if op.param3 in mid10:
                if op.param2 in mid9:
                    wN10.acceptGroupInvitation(op.param1)        
            if op.param3 in mid10:
                if op.param2 in mid11:
                    wN10.acceptGroupInvitation(op.param1)        
            if op.param3 in mid10:
                if op.param2 in mid12:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid13:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid14:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid15:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid16:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid17:
                    wN10.acceptGroupInvitation(op.param1)   
            if op.param3 in mid10:
                if op.param2 in mid18:
                    wN10.acceptGroupInvitation(op.param1) 
            if op.param3 in mid10:
                if op.param2 in mid19:
                    wN10.acceptGroupInvitation(op.param1)  
            if op.param3 in mid10:
                if op.param2 in mid20:
                    wN10.acceptGroupInvitation(op.param1)        
            if op.param3 in mid10:
                if op.param2 in mid21:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid22:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid23:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid24:
                    wN10.acceptGroupInvitation(op.param1)
            if op.param3 in mid10:
                if op.param2 in mid25:
                    wN10.acceptGroupInvitation(op.param1)
                 
#--------------      
            if op.param3 in mid11:
                if op.param2 in mid:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid2:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid3:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid4:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid5:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid6:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid7:
                    wN11.acceptGroupInvitation(op.param1)   
            if op.param3 in mid11:
                if op.param2 in mid8:
                    wN11.acceptGroupInvitation(op.param1) 
            if op.param3 in mid11:
                if op.param2 in mid9:
                    wN11.acceptGroupInvitation(op.param1)        
            if op.param3 in mid11:
                if op.param2 in mid10:
                    wN11.acceptGroupInvitation(op.param1)   
            if op.param3 in mid11:
                if op.param2 in mid12:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid13:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid14:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid15:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid16:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid17:
                    wN11.acceptGroupInvitation(op.param1)   
            if op.param3 in mid11:
                if op.param2 in mid18:
                    wN11.acceptGroupInvitation(op.param1) 
            if op.param3 in mid11:
                if op.param2 in mid19:
                    wN11.acceptGroupInvitation(op.param1)  
            if op.param3 in mid11:
                if op.param2 in mid20:
                    wN11.acceptGroupInvitation(op.param1)        
            if op.param3 in mid1:
                if op.param2 in mid21:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid22:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid23:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid24:
                    wN11.acceptGroupInvitation(op.param1)
            if op.param3 in mid11:
                if op.param2 in mid25:
                    wN11.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid12:
                if op.param2 in mid:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid2:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid3:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid4:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid5:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid6:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid7:
                    wN12.acceptGroupInvitation(op.param1)   
            if op.param3 in mid12:
                if op.param2 in mid8:
                    wN12.acceptGroupInvitation(op.param1) 
            if op.param3 in mid12:
                if op.param2 in mid9:
                    wN12.acceptGroupInvitation(op.param1)        
            if op.param3 in mid12:
                if op.param2 in mid10:
                    wN12.acceptGroupInvitation(op.param1)   
            if op.param3 in mid12:
                if op.param2 in mid11:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid13:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid14:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid15:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid16:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid17:
                    wN12.acceptGroupInvitation(op.param1)   
            if op.param3 in mid12:
                if op.param2 in mid18:
                    wN12.acceptGroupInvitation(op.param1) 
            if op.param3 in mid12:
                if op.param2 in mid19:
                    wN12.acceptGroupInvitation(op.param1)  
            if op.param3 in mid12:
                if op.param2 in mid20:
                    wN12.acceptGroupInvitation(op.param1)        
            if op.param3 in mid12:
                if op.param2 in mid21:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid22:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid23:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid24:
                    wN12.acceptGroupInvitation(op.param1)
            if op.param3 in mid12:
                if op.param2 in mid25:
                    wN12.acceptGroupInvitation(op.param1) 
#------------      
            if op.param3 in mid13:
                if op.param2 in mid:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid2:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid3:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid4:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid5:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid6:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid7:
                    wN13.acceptGroupInvitation(op.param1)   
            if op.param3 in mid13:
                if op.param2 in mid8:
                    wN13.acceptGroupInvitation(op.param1) 
            if op.param3 in mid13:
                if op.param2 in mid9:
                    wN13.acceptGroupInvitation(op.param1)        
            if op.param3 in mid13:
                if op.param2 in mid10:
                    wN13.acceptGroupInvitation(op.param1)   
            if op.param3 in mid13:
                if op.param2 in mid11:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid13:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid14:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid15:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid16:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid17:
                    wN13.acceptGroupInvitation(op.param1)   
            if op.param3 in mid13:
                if op.param2 in mid18:
                    wN13.acceptGroupInvitation(op.param1) 
            if op.param3 in mid13:
                if op.param2 in mid19:
                    wN13.acceptGroupInvitation(op.param1)  
            if op.param3 in mid13:
                if op.param2 in mid20:
                    wN13.acceptGroupInvitation(op.param1)        
            if op.param3 in mid13:
                if op.param2 in mid21:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid22:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid23:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid24:
                    wN13.acceptGroupInvitation(op.param1)
            if op.param3 in mid13:
                if op.param2 in mid25:
                    wN13.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid14:
                if op.param2 in mid:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid2:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid3:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid4:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid5:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid6:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid7:
                    wN14.acceptGroupInvitation(op.param1)   
            if op.param3 in mid14:
                if op.param2 in mid8:
                    wN14.acceptGroupInvitation(op.param1) 
            if op.param3 in mid14:
                if op.param2 in mid9:
                    wN14.acceptGroupInvitation(op.param1)        
            if op.param3 in mid14:
                if op.param2 in mid10:
                    wN14.acceptGroupInvitation(op.param1)   
            if op.param3 in mid14:
                if op.param2 in mid11:
                    wN14.acceptGroupInvitation(op.param1)       
            if op.param3 in mid14:
                if op.param2 in mid12:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid13:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid15:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid16:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid17:
                    wN14.acceptGroupInvitation(op.param1)   
            if op.param3 in mid14:
                if op.param2 in mid18:
                    wN14.acceptGroupInvitation(op.param1) 
            if op.param3 in mid14:
                if op.param2 in mid19:
                    wN14.acceptGroupInvitation(op.param1)  
            if op.param3 in mid14:
                if op.param2 in mid20:
                    wN14.acceptGroupInvitation(op.param1)        
            if op.param3 in mid14:
                if op.param2 in mid21:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid22:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid23:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid24:
                    wN14.acceptGroupInvitation(op.param1)
            if op.param3 in mid14:
                if op.param2 in mid25:
                    wN14.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid15:
                if op.param2 in mid:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid2:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid3:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid4:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid5:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid6:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid7:
                    wN15.acceptGroupInvitation(op.param1)   
            if op.param3 in mid15:
                if op.param2 in mid8:
                    wN15.acceptGroupInvitation(op.param1) 
            if op.param3 in mid15:
                if op.param2 in mid9:
                    wN15.acceptGroupInvitation(op.param1)        
            if op.param3 in mid15:
                if op.param2 in mid10:
                    wN15.acceptGroupInvitation(op.param1)   
            if op.param3 in mid15:
                if op.param2 in mid11:
                    wN15.acceptGroupInvitation(op.param1)       
            if op.param3 in mid15:
                if op.param2 in mid12:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid13:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid14:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid16:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid17:
                    wN15.acceptGroupInvitation(op.param1)   
            if op.param3 in mid15:
                if op.param2 in mid18:
                    wN15.acceptGroupInvitation(op.param1) 
            if op.param3 in mid15:
                if op.param2 in mid19:
                    wN15.acceptGroupInvitation(op.param1)  
            if op.param3 in mid15:
                if op.param2 in mid20:
                    wN15.acceptGroupInvitation(op.param1)        
            if op.param3 in mid15:
                if op.param2 in mid21:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid22:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid23:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid24:
                    wN15.acceptGroupInvitation(op.param1)
            if op.param3 in mid15:
                if op.param2 in mid25:
                    wN15.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid16:
                if op.param2 in mid:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid2:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid3:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid4:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid5:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid6:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid7:
                    wN16.acceptGroupInvitation(op.param1)   
            if op.param3 in mid16:
                if op.param2 in mid8:
                    wN16.acceptGroupInvitation(op.param1) 
            if op.param3 in mid16:
                if op.param2 in mid9:
                    wN16.acceptGroupInvitation(op.param1)        
            if op.param3 in mid16:
                if op.param2 in mid10:
                    wN16.acceptGroupInvitation(op.param1)   
            if op.param3 in mid16:
                if op.param2 in mid11:
                    wN16.acceptGroupInvitation(op.param1)        
            if op.param3 in mid16:
                if op.param2 in mid12:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid13:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid14:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid15:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid17:
                    wN16.acceptGroupInvitation(op.param1)   
            if op.param3 in mid16:
                if op.param2 in mid18:
                    wN16.acceptGroupInvitation(op.param1) 
            if op.param3 in mid16:
                if op.param2 in mid19:
                    wN16.acceptGroupInvitation(op.param1)  
            if op.param3 in mid16:
                if op.param2 in mid20:
                    wN16.acceptGroupInvitation(op.param1)        
            if op.param3 in mid16:
                if op.param2 in mid21:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid22:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid23:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid24:
                    wN16.acceptGroupInvitation(op.param1)
            if op.param3 in mid16:
                if op.param2 in mid25:
                    wN16.acceptGroupInvitation(op.param1)
#----------                  
            if op.param3 in mid17:
                if op.param2 in mid:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid2:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid3:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid4:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid5:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid6:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid7:
                    wN17.acceptGroupInvitation(op.param1)   
            if op.param3 in mid17:
                if op.param2 in mid8:
                    wN17.acceptGroupInvitation(op.param1) 
            if op.param3 in mid17:
                if op.param2 in mid9:
                    wN17.acceptGroupInvitation(op.param1)        
            if op.param3 in mid17:
                if op.param2 in mid10:
                    wN17.acceptGroupInvitation(op.param1) 
            if op.param3 in mid17:
                if op.param2 in mid11:
                    wN17.acceptGroupInvitation(op.param1)           
            if op.param3 in mid17:
                if op.param2 in mid12:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid13:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid14:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid15:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid16:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid18:
                    wN17.acceptGroupInvitation(op.param1) 
            if op.param3 in mid17:
                if op.param2 in mid19:
                    wN17.acceptGroupInvitation(op.param1)  
            if op.param3 in mid17:
                if op.param2 in mid20:
                    wN17.acceptGroupInvitation(op.param1)        
            if op.param3 in mid17:
                if op.param2 in mid21:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid22:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid23:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid24:
                    wN17.acceptGroupInvitation(op.param1)
            if op.param3 in mid17:
                if op.param2 in mid25:
                    wN17.acceptGroupInvitation(op.param1)
#----------                
            if op.param3 in mid18:
                if op.param2 in mid:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid2:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid3:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid4:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid5:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid6:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid7:
                    wN18.acceptGroupInvitation(op.param1)   
            if op.param3 in mid18:
                if op.param2 in mid8:
                    wN18.acceptGroupInvitation(op.param1) 
            if op.param3 in mid18:
                if op.param2 in mid9:
                    wN18.acceptGroupInvitation(op.param1)        
            if op.param3 in mid18:
                if op.param2 in mid10:
                    wN18.acceptGroupInvitation(op.param1)   
            if op.param3 in mid18:
                if op.param2 in mid11:
                    wN18.acceptGroupInvitation(op.param1)         
            if op.param3 in mid18:
                if op.param2 in mid12:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid13:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid14:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid15:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid16:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid17:
                    wN18.acceptGroupInvitation(op.param1)   
            if op.param3 in mid18:
                if op.param2 in mid19:
                    wN18.acceptGroupInvitation(op.param1)  
            if op.param3 in mid18:
                if op.param2 in mid20:
                    wN18.acceptGroupInvitation(op.param1)        
            if op.param3 in mid18:
                if op.param2 in mid21:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid22:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid23:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid24:
                    wN18.acceptGroupInvitation(op.param1)
            if op.param3 in mid18:
                if op.param2 in mid25:
                    wN18.acceptGroupInvitation(op.param1)
#----------                
            if op.param3 in mid19:
                if op.param2 in mid:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid2:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid3:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid4:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid5:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid6:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid7:
                    wN19.acceptGroupInvitation(op.param1)   
            if op.param3 in mid19:
                if op.param2 in mid8:
                    wN19.acceptGroupInvitation(op.param1) 
            if op.param3 in mid19:
                if op.param2 in mid9:
                    wN19.acceptGroupInvitation(op.param1)        
            if op.param3 in mid19:
                if op.param2 in mid10:
                    wN19.acceptGroupInvitation(op.param1)   
            if op.param3 in mid19:
                if op.param2 in mid11:
                    wN19.acceptGroupInvitation(op.param1)        
            if op.param3 in mid19:
                if op.param2 in mid12:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid13:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid14:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid15:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid16:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid17:
                    wN19.acceptGroupInvitation(op.param1)   
            if op.param3 in mid19:
                if op.param2 in mid18:
                    wN19.acceptGroupInvitation(op.param1)  
            if op.param3 in mid19:
                if op.param2 in mid20:
                    wN19.acceptGroupInvitation(op.param1)        
            if op.param3 in mid19:
                if op.param2 in mid21:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid22:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid23:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid24:
                    wN19.acceptGroupInvitation(op.param1)
            if op.param3 in mid19:
                if op.param2 in mid25:
                    wN19.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid20:
                if op.param2 in mid:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid2:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid3:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid4:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid5:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid6:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid7:
                    wN20.acceptGroupInvitation(op.param1)   
            if op.param3 in mid20:
                if op.param2 in mid8:
                    wN20.acceptGroupInvitation(op.param1) 
            if op.param3 in mid20:
                if op.param2 in mid9:
                    wN20.acceptGroupInvitation(op.param1)        
            if op.param3 in mid20:
                if op.param2 in mid10:
                    wN20.acceptGroupInvitation(op.param1)  
            if op.param3 in mid20:
                if op.param2 in mid11:
                    wN20.acceptGroupInvitation(op.param1)        
            if op.param3 in mid20:
                if op.param2 in mid12:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid13:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid14:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid15:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid16:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid17:
                    wN20.acceptGroupInvitation(op.param1)   
            if op.param3 in mid20:
                if op.param2 in mid18:
                    wN20.acceptGroupInvitation(op.param1) 
            if op.param3 in mid20:
                if op.param2 in mid19:
                    wN20.acceptGroupInvitation(op.param1)         
            if op.param3 in mid20:
                if op.param2 in mid21:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid22:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid23:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid24:
                    wN20.acceptGroupInvitation(op.param1)
            if op.param3 in mid20:
                if op.param2 in mid25:
                    wN20.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid21:
                if op.param2 in mid:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid2:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid3:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid4:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid5:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid6:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid7:
                    wN21.acceptGroupInvitation(op.param1)   
            if op.param3 in mid21:
                if op.param2 in mid8:
                    wN21.acceptGroupInvitation(op.param1) 
            if op.param3 in mid21:
                if op.param2 in mid9:
                    wN21.acceptGroupInvitation(op.param1)        
            if op.param3 in mid21:
                if op.param2 in mid10:
                    wN21.acceptGroupInvitation(op.param1)   
            if op.param3 in mid21:
                if op.param2 in mid11:
                    wN21.acceptGroupInvitation(op.param1)           
            if op.param3 in mid21:
                if op.param2 in mid12:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid13:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid14:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid15:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid16:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid17:
                    wN21.acceptGroupInvitation(op.param1)   
            if op.param3 in mid21:
                if op.param2 in mid18:
                    wN21.acceptGroupInvitation(op.param1) 
            if op.param3 in mid21:
                if op.param2 in mid19:
                    wN21.acceptGroupInvitation(op.param1)       
            if op.param3 in mid21:
                if op.param2 in mid20:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid22:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid23:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid24:
                    wN21.acceptGroupInvitation(op.param1)
            if op.param3 in mid21:
                if op.param2 in mid25:
                    wN21.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid22:
                if op.param2 in mid:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid2:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid3:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid4:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid5:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid6:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid7:
                    wN22.acceptGroupInvitation(op.param1)   
            if op.param3 in mid22:
                if op.param2 in mid8:
                    wN22.acceptGroupInvitation(op.param1) 
            if op.param3 in mid22:
                if op.param2 in mid9:
                    wN22.acceptGroupInvitation(op.param1)        
            if op.param3 in mid22:
                if op.param2 in mid10:
                    wN22.acceptGroupInvitation(op.param1)  
            if op.param3 in mid22:
                if op.param2 in mid11:
                    wN22.acceptGroupInvitation(op.param1)        
            if op.param3 in mid22:
                if op.param2 in mid12:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid13:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid14:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid15:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid16:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid17:
                    wN22.acceptGroupInvitation(op.param1)   
            if op.param3 in mid22:
                if op.param2 in mid18:
                    wN22.acceptGroupInvitation(op.param1) 
            if op.param3 in mid22:
                if op.param2 in mid19:
                    wN22.acceptGroupInvitation(op.param1)  
            if op.param3 in mid22:
                if op.param2 in mid20:
                    wN22.acceptGroupInvitation(op.param1)        
            if op.param3 in mid22:
                if op.param2 in mid21:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid23:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid24:
                    wN22.acceptGroupInvitation(op.param1)
            if op.param3 in mid22:
                if op.param2 in mid25:
                    wN22.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid23:
                if op.param2 in mid:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid2:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid3:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid4:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid5:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid6:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid7:
                    wN23.acceptGroupInvitation(op.param1)   
            if op.param3 in mid23:
                if op.param2 in mid8:
                    wN23.acceptGroupInvitation(op.param1) 
            if op.param3 in mid23:
                if op.param2 in mid9:
                    wN23.acceptGroupInvitation(op.param1)        
            if op.param3 in mid23:
                if op.param2 in mid10:
                    wN23.acceptGroupInvitation(op.param1)  
            if op.param3 in mid23:
                if op.param2 in mid11:
                    wN23.acceptGroupInvitation(op.param1)         
            if op.param3 in mid23:
                if op.param2 in mid12:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid13:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid14:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid15:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid16:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid17:
                    wN23.acceptGroupInvitation(op.param1)   
            if op.param3 in mid23:
                if op.param2 in mid18:
                    wN23.acceptGroupInvitation(op.param1) 
            if op.param3 in mid23:
                if op.param2 in mid19:
                    wN23.acceptGroupInvitation(op.param1)  
            if op.param3 in mid23:
                if op.param2 in mid20:
                    wN23.acceptGroupInvitation(op.param1)        
            if op.param3 in mid23:
                if op.param2 in mid21:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid22:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid24:
                    wN23.acceptGroupInvitation(op.param1)
            if op.param3 in mid23:
                if op.param2 in mid25:
                    wN23.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid24:
                if op.param2 in mid:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid2:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid3:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid4:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid5:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid6:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid7:
                    wN24.acceptGroupInvitation(op.param1)   
            if op.param3 in mid24:
                if op.param2 in mid8:
                    wN24.acceptGroupInvitation(op.param1) 
            if op.param3 in mid24:
                if op.param2 in mid9:
                    wN24.acceptGroupInvitation(op.param1)        
            if op.param3 in mid24:
                if op.param2 in mid10:
                    wN24.acceptGroupInvitation(op.param1) 
            if op.param3 in mid24:
                if op.param2 in mid11:
                    wN24.acceptGroupInvitation(op.param1)         
            if op.param3 in mid24:
                if op.param2 in mid12:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid13:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid14:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid15:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid16:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid17:
                    wN24.acceptGroupInvitation(op.param1)   
            if op.param3 in mid24:
                if op.param2 in mid18:
                    wN24.acceptGroupInvitation(op.param1) 
            if op.param3 in mid24:
                if op.param2 in mid19:
                    wN24.acceptGroupInvitation(op.param1)    
            if op.param3 in mid24:
                if op.param2 in mid20:
                    wN24.acceptGroupInvitation(op.param1)        
            if op.param3 in mid24:
                if op.param2 in mid21:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid22:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid23:
                    wN24.acceptGroupInvitation(op.param1)
            if op.param3 in mid24:
                if op.param2 in mid25:
                    wN24.acceptGroupInvitation(op.param1)
#----------                 
            if op.param3 in mid25:
                if op.param2 in mid:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid2:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid3:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid4:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid5:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid6:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid7:
                    wN25.acceptGroupInvitation(op.param1)   
            if op.param3 in mid25:
                if op.param2 in mid8:
                    wN25.acceptGroupInvitation(op.param1) 
            if op.param3 in mid25:
                if op.param2 in mid9:
                    wN25.acceptGroupInvitation(op.param1)        
            if op.param3 in mid25:
                if op.param2 in mid10:
                    wN25.acceptGroupInvitation(op.param1) 
            if op.param3 in mid25:
                if op.param2 in mid11:
                    wN25.acceptGroupInvitation(op.param1)        
            if op.param3 in mid25:
                if op.param2 in mid12:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid13:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid14:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid15:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid16:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid17:
                    wN25.acceptGroupInvitation(op.param1)   
            if op.param3 in mid25:
                if op.param2 in mid18:
                    wN25.acceptGroupInvitation(op.param1) 
            if op.param3 in mid25:
                if op.param2 in mid19:
                    wN25.acceptGroupInvitation(op.param1)  
            if op.param3 in mid25:
                if op.param2 in mid20:
                    wN25.acceptGroupInvitation(op.param1)       
            if op.param3 in mid25:
                if op.param2 in mid21:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid22:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid23:
                    wN25.acceptGroupInvitation(op.param1)
            if op.param3 in mid25:
                if op.param2 in mid24:
                    wN25.acceptGroupInvitation(op.param1)        
#--------------                  
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
                
            if mid6 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN6.acceptGroupInvitation(op.param1)
                else:
                  wN6.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"     
                
            if mid7 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN7.acceptGroupInvitation(op.param1)
                else:
                  wN7.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"    
                
            if mid8 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN8.acceptGroupInvitation(op.param1)
                else:
                  wN8.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"     
                
            if mid9 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN9.acceptGroupInvitation(op.param1)
                else:
                  wN9.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"      
                
            if mid10 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN10.acceptGroupInvitation(op.param1)
                else:
                  wN10.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"    
                
            if mid11 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN11.acceptGroupInvitation(op.param1)
                else:
                  wN11.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid12 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN12.acceptGroupInvitation(op.param1)
                else:
                  wN12.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid13 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN13.acceptGroupInvitation(op.param1)
                else:
                  wN13.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid14 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN14.acceptGroupInvitation(op.param1)
                else:
                  wN14.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid15 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN15.acceptGroupInvitation(op.param1)
                else:
                  wN15.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
            if mid16 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN16.acceptGroupInvitation(op.param1)
                else:
                  wN16.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"     
                
            if mid17 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN17.acceptGroupInvitation(op.param1)
                else:
                  wN17.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"    
                
            if mid18 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN18.acceptGroupInvitation(op.param1)
                else:
                  wN18.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"     
                
            if mid19 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN19.acceptGroupInvitation(op.param1)
                else:
                  wN19.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"      
                
            if mid20 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN20.acceptGroupInvitation(op.param1)
                else:
                  wN20.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"      
                
            if mid21 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN21.acceptGroupInvitation(op.param1)
                else:
                  wN21.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid22 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN22.acceptGroupInvitation(op.param1)
                else:
                  wN22.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid23 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN23.acceptGroupInvitation(op.param1)
                else:
                  wN23.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid24 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN24.acceptGroupInvitation(op.param1)
                else:
                  wN24.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid25 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or owner:
                  wN25.acceptGroupInvitation(op.param1)
                else:
                  wN25.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"    
#--------------                      
#--------------                  
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
                  G = wN6.getGroup(op.param1)
                  wN5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN6.updateGroup(G)
                  Ticket = wN6.reissueGroupTicket(op.param1)
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
                  G = wN6.getGroup(op.param1)
                  G = wN7.getGroup(op.param1)
                  wN6.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN7.updateGroup(G)
                  Ticket = wN7.reissueGroupTicket(op.param1)
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
                    
            if op.param3 in mid6:
              if op.param2 not in Bots or admin:
                try:
                  G = wN7.getGroup(op.param1)
                  G = wN8.getGroup(op.param1)
                  wN7.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN8.updateGroup(G)
                  Ticket = wN8.reissueGroupTicket(op.param1)
                  wN6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN6.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)  
                    
            if op.param3 in mid7:
              if op.param2 not in Bots or admin:
                try:
                  G = wN8.getGroup(op.param1)
                  G = wN9.getGroup(op.param1)
                  wN8.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN9.updateGroup(G)
                  Ticket = wN9.reissueGroupTicket(op.param1)
                  wN7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN7.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)          
                    
            if op.param3 in mid8:
              if op.param2 not in Bots or admin:
                try:
                  G = wN9.getGroup(op.param1)
                  G = wN10.getGroup(op.param1)
                  wN9.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN10.updateGroup(G)
                  Ticket = wN10.reissueGroupTicket(op.param1)
                  wN8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN8.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)   
                    
            if op.param3 in mid9:
              if op.param2 not in Bots or admin:
                try:
                  G = wN10.getGroup(op.param1)
                  G = wN11.getGroup(op.param1)
                  wN10.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN11.updateGroup(G)
                  Ticket = wN11.reissueGroupTicket(op.param1)
                  wN9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN9.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)     
                    
            if op.param3 in mid10:
              if op.param2 not in Bots or admin:
                try:
                  G = wN11.getGroup(op.param1)
                  G = wN12.getGroup(op.param1)
                  wN11.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN12.updateGroup(G)
                  Ticket = wN12.reissueGroupTicket(op.param1)
                  wN10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN10.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN10.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)         
                    
            if op.param3 in mid11:
              if op.param2 not in Bots or admin:
                try:
                  G = wN12.getGroup(op.param1)
                  G = wN13.getGroup(op.param1)
                  wN12.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN13.updateGroup(G)
                  Ticket = wN13.reissueGroupTicket(op.param1)
                  wN11.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN11.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN11.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid12:
              if op.param2 not in Bots or admin:
                try:
                  G = wN13.getGroup(op.param1)
                  G = wN14.getGroup(op.param1)
                  wN13.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN14.updateGroup(G)
                  Ticket = wN14.reissueGroupTicket(op.param1)
                  wN12.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN12.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN12.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid13:
              if op.param2 not in Bots or admin:
                try:
                  G = wN14.getGroup(op.param1)
                  G = wN15.getGroup(op.param1)
                  wN14.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN15.updateGroup(G)
                  Ticket = wN15.reissueGroupTicket(op.param1)
                  wN13.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN13.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN13.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    
            if op.param3 in mid14:
              if op.param2 not in Bots or admin:
                try:
                  G = wN15.getGroup(op.param1)
                  G = wN16.getGroup(op.param1)
                  wN15.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN16.updateGroup(G)
                  Ticket = wN16.reissueGroupTicket(op.param1)
                  wN14.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN14.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN14.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    
            if op.param3 in mid15:
              if op.param2 not in Bots or admin:
                try:
                  G = wN16.getGroup(op.param1)
                  G = wN17.getGroup(op.param1)
                  wN16.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN17.updateGroup(G)
                  Ticket = wN17.reissueGroupTicket(op.param1)
                  wN15.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN15.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN15.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)   
                    
            if op.param3 in mid16:
              if op.param2 not in Bots or admin:
                try:
                  G = wN17.getGroup(op.param1)
                  G = wN18.getGroup(op.param1)
                  wN17.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN18.updateGroup(G)
                  Ticket = wN18.reissueGroupTicket(op.param1)
                  wN16.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN16.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN16.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)  
                    
            if op.param3 in mid17:
              if op.param2 not in Bots or admin:
                try:
                  G = wN18.getGroup(op.param1)
                  G = wN19.getGroup(op.param1)
                  wN18.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN19.updateGroup(G)
                  Ticket = wN19.reissueGroupTicket(op.param1)
                  wN17.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN17.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN17.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)          
                    
            if op.param3 in mid18:
              if op.param2 not in Bots or admin:
                try:
                  G = wN19.getGroup(op.param1)
                  G = wN20.getGroup(op.param1)
                  wN19.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN20.updateGroup(G)
                  Ticket = wN20.reissueGroupTicket(op.param1)
                  wN18.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN18.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN18.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)   
                    
            if op.param3 in mid19:
              if op.param2 not in Bots or admin:
                try:
                  G = wN20.getGroup(op.param1)
                  G = wN21.getGroup(op.param1)
                  wN20.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN21.updateGroup(G)
                  Ticket = wN21.reissueGroupTicket(op.param1)
                  wN19.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN19.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN19.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)     
                    
            if op.param3 in mid20:
              if op.param2 not in Bots or admin:
                try:
                  G = wN21.getGroup(op.param1)
                  G = wN22.getGroup(op.param1)
                  wN21.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN22.updateGroup(G)
                  Ticket = wN22.reissueGroupTicket(op.param1)
                  wN20.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN20.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN20.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)      
                    
            if op.param3 in mid21:
              if op.param2 not in Bots or admin:
                try:
                  G = wN22.getGroup(op.param1)
                  G = wN23.getGroup(op.param1)
                  wN22.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN23.updateGroup(G)
                  Ticket = wN23.reissueGroupTicket(op.param1)
                  wN21.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN21.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN21.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid22:
              if op.param2 not in Bots or admin:
                try:
                  G = wN23.getGroup(op.param1)
                  G = wN24.getGroup(op.param1)
                  wN23.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN24.updateGroup(G)
                  Ticket = wN24.reissueGroupTicket(op.param1)
                  wN22.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN22.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN22.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid23:
              if op.param2 not in Bots or admin:
                try:
                  G = wN24.getGroup(op.param1)
                  G = wN25.getGroup(op.param1)
                  wN24.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN25.updateGroup(G)
                  Ticket = wN25.reissueGroupTicket(op.param1)
                  wN23.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN23.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN23.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    
            if op.param3 in mid24:
              if op.param2 not in Bots or admin:
                try:
                  G = wN25.getGroup(op.param1)
                  G = wN1.getGroup(op.param1)
                  wN25.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN1.updateGroup(G)
                  Ticket = wN1.reissueGroupTicket(op.param1)
                  wN24.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN24.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN24.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    
            if op.param3 in mid25:
              if op.param2 not in Bots or admin:
                try:
                  G = wN1.getGroup(op.param1)
                  G = wN2.getGroup(op.param1)
                  wN2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  wN1.updateGroup(G)
                  Ticket = wN1.reissueGroupTicket(op.param1)
                  wN25.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  wN25.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  wN25.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)                  
#-------                                 
            if op.param3 in admin:
              if op.param2 not in admin:
                try:
                  wN1.kickoutFromGroup(op.param1,[op.param2])
                  wN1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  try:
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    wN1.inviteIntoGroup(op.param1,[admin])
                    wait["blacklist"][op.param2] = True
                  except:
                    try:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                      wait["blacklist"][op.param2] = True

            if op.param3 in admin or Bots:
                if op.param2 in admin or Bots:
                    try:
                        wN1.inviteIntoGroup(op.param1,admin)
                        wN1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,[admin])
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
                wN6.leaveRoom(op.param1)
                wN7.leaveRoom(op.param1)
                wN8.leaveRoom(op.param1)
                wN9.leaveRoom(op.param1)
                wN10.leaveRoom(op.param1)
                wN11.leaveRoom(op.param1)
                wN12.leaveRoom(op.param1)
                wN13.leaveRoom(op.param1)
                wN14.leaveRoom(op.param1)
                wN15.leaveRoom(op.param1)
                wN16.leaveRoom(op.param1)
                wN17.leaveRoom(op.param1)
                wN18.leaveRoom(op.param1)
                wN19.leaveRoom(op.param1)
                wN20.leaveRoom(op.param1)
                wN21.leaveRoom(op.param1)
                wN22.leaveRoom(op.param1)
                wN23.leaveRoom(op.param1)
                wN24.leaveRoom(op.param1)
                wN25.leaveRoom(op.param1)
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
                wN11.leaveRoom(op.param1)
                wN12.leaveRoom(op.param1)
                wN13.leaveRoom(op.param1)
                wN14.leaveRoom(op.param1)
                wN15.leaveRoom(op.param1)
                wN16.leaveRoom(op.param1)
                wN17.leaveRoom(op.param1)
                wN18.leaveRoom(op.param1)
                wN19.leaveRoom(op.param1)
                wN20.leaveRoom(op.param1)
                wN21.leaveRoom(op.param1)
                wN22.leaveRoom(op.param1)
                wN23.leaveRoom(op.param1)
                wN24.leaveRoom(op.param1)
                wN25.leaveRoom(op.param1)
                
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
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        wN1.sendText(msg.to,text)
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
                                
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = wN1.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["kangen bilang, gak usah ngetag mulu, dasar jones 😂😜",cName + "nah mending pc aja kak kalau penting.😛.!!",cName + "kenapa, say ada yg bisa d banting 😂 ",cName + "kangen aku ya?beb😗?",cName + "kangen bilang, gak usah ngetag mulu, dasar jones 😂😜",cName + "sekali lagi ngetag, bayar  2000 😯😏..!!!",cName + "Tuh kan jones 😆😂",cName + "ngetag lagi, mojok aja yux say 😗.!!!"]
                     ret_ = "[Auto Respon] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  wN1.sendText(msg.to,ret_)
                                  break            
                    
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
                                  break
            
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

            #if msg.contentType == 13:
            #    if wait['steal'] == True:
            #        _name = msg.contentMetadata["displayName"]
            #        copy = msg.contentMetadata["mid"]
            #        groups = wN1.getGroup(msg.to)
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
            #                    wN1.findAndAddContactsByMid(target)
            #                    contact = wN1.getContact(target)
            #                    cu = wN1.channel.getCover(target)
            #                    path = str(cu)
            #                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            #                    wN1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
            #                    wN1.sendText(msg.to,"Profile Picture " + contact.displayName)
            #                    wN1.sendImageWithURL(msg.to,image)
            #                    wN1.sendText(msg.to,"Cover " + contact.displayName)
            #                    wN1.sendImageWithURL(msg.to,path)
            #                    wait['steal'] = False
            #                    break
            #                except:
            #                        pass    
                                
            if wait['alwayRead'] == True:
                if msg.toType == 0:
                    wN1.sendChatChecked(msg.from_,msg.id)
                else:
                    wN1.sendChatChecked(msg.to,msg.id)
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
            elif msg.text.lower() == 'keytran':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,helptranslate)
                    else:
                        wN1.sendText(msg.to,helptranslate)
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
            elif msg.text.lower() == '#crash':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                    wN1.sendMessage(msg)
                    wN1.sendMessage(msg)
                    wN2.sendMessage(msg)
                    wN2.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                wN1.sendMessage(msg)
                
            elif "facebook " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("facebook ","")
                    b = urllib.quote(a)
                    wN1.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    wN1.sendText(msg.to, "https://www.facebook.com" + b)
                    wN1.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")    
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
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]                                               
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except: pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                wN1.sendText(msg.to,"Sider,,main yuk 😆😆")                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    wN1.sendText(msg.to, "Cek Sider Off")
                else:
                    wN1.sendText(msg.to, "Hihi Belom Di Set")                
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
                    msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                    wN1.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN1.sendMessage(msg)
                wN1.sendText(msg.to,'❂➣ Creator yang manis kalem  􀜁􀄯􏿿')
 #           elif msg.text.lower() == 'autoadd on':
 #               if msg.from_ in admin:
 #                   if wait['autoAdd'] == True:
 #                       if wait["lang"] == "JP":
 #                           wN1.sendText(msg.to,"Auto add set to on")
 #                       else:
 #                           wN1.sendText(msg.to,"Auto add already on")
 #                   else:
 #                       wait['autoAdd'] = True
 #                       if wait["lang"] == "JP":
 #                           wN1.sendText(msg.to,"Auto add set to on")
 #                       else:
 #                           wN1.sendText(msg.to,"Auto add already on")
 #           elif msg.text.lower() == 'autoadd off':
 #               if msg.from_ in admin:
 #                   if wait['autoAdd'] == False:
 #                       if wait["lang"] == "JP":
 #                           wN1.sendText(msg.to,"Auto add set to off")
 #                       else:
 #                           wN1.sendText(msg.to,"Auto add already off")
 #                   else:
 #                       wait['autoAdd'] = False
 #                       if wait["lang"] == "JP":
 #                           wN1.sendText(msg.to,"Auto add set to off")
 #                       else:
 #                           wN1.sendText(msg.to,"Auto add already off")
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
#========================== FOR COMMAND BOT FINISHED =============================#
            elif "Spam change:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam change:","")
                        wN1.sendText(msg.to,"spam changed")

            elif "Spam add:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam add:","")
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"spam changed")
                        else:
                            wN1.sendText(msg.to,"Done")

            elif "Spam:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        strnum = msg.text.replace("Spam:","")
                        num = int(strnum)
                        for var in range(0,num):
                            wN1.sendText(msg.to, wait['spam'])
#=====================================
            elif "##Spam " in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        bctxt = msg.text.replace("##Spam ", "")
                        t = wN1.getAllContactIds()
                        t = 500
                        while(t):
                            wN1.sendText(msg.to, (bctxt))
                            t-=1
#==============================================
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

            elif "crashkontak @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("crashkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = wN1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName + g.mid
                            xlen = str(len(xname)+1)
                            msg.contentType = 13
                            msg.text = 'mid'+xname+''
                            msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                            msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                            msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendText("crash kontak selesai")
                            print " Spammed crash !"
#==============================================================================#
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    wN1.sendText(msg.to,"Kirim Contact")
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
                    wN1.sendText(msg.to,"Send Contact")
                
 #           elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
 #               if msg.from_ in admin:
 #                   print "[Command]Like executed"
 #                   wN1.sendText(msg.to,"Like Status Owner")
 #                   try:
 #                       likeme()
 #                   except:
 #                       pass
 #               
 #           elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
 #               if msg.from_ in admin:
 #                   print "[Command]Like executed"
 #                   wN1.sendText(msg.to,"Like Status Teman")
 #                   try:
 #                       likefriend()
 #                   except:
 #                       pass
 #           
 #           elif msg.text in ["Like:on","Like on"]:
 #               if msg.from_ in admin:
 #                   if wait['likeOn'] == True:
 #                       if wait["lang"] == "JP":
 #                           wN1.sendText(msg.to,"Done")
 #                   else:
 #                       wait['likeOn'] = True
 #                       if wait["lang"] == "JP":
 #                           wN1.sendText(msg.to,"Already")
 #                       
            elif msg.text in ["Like off","Like:off"]:
                if msg.from_ in admin:
                    if wait['likeOn'] == False:
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = False
                        if wait["lang"] == "JP":
                            wN1.sendText(msg.to,"Already")
                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = True
                    wN1.sendText(msg.to,"Simi mode On")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = False
                    wN1.sendText(msg.to,"Simi mode Off")
                
            elif msg.text in ["Autoread on","Read:on"]:
                if msg.from_ in admin:
                    wait['alwayRead'] = True
                    wN1.sendText(msg.to,"Auto read On")
                
            elif msg.text in ["Autoread off","Read:off"]:
                if msg.from_ in admin:
                    wait['alwayRead'] = False
                    wN1.sendText(msg.to,"Auto read Off")
                
            elif msg.text in ["Tag on","tag on"]:
                if msg.from_ in admin:
                    wait['detectMention'] = True
                    wN1.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in ["Tag off","tag off"]:
                if msg.from_ in admin:
                    wait['detectMention'] = False
                    wN1.sendText(msg.to,"Auto respon tag Off")
            
            elif msg.text in ["Poto on","poto on"]:
                if msg.from_ in admin:
                    wait['potoMention'] = True
                    wN1.sendText(msg.to,"Auto respon tag poto On")
                
            elif msg.text in ["Poto off","poto off"]:
                if msg.from_ in admin:
                    wait['potoMention'] = False
                    wN1.sendText(msg.to,"Auto respon tag poto Off")
            
            elif msg.text in ["Tag2 on","tag2 on"]:
                if msg.from_ in admin:
                    wait['kickMention'] = True
                    wN1.sendText(msg.to,"Auto Kick tag ON")
                
            elif msg.text in ["Tag2 off","tag2 off"]:
                if msg.from_ in admin:
                    wait['kickMention'] = False
                    wN1.sendText(msg.to,"Auto Kick tag OFF")
            elif "Time" in msg.text:
                if msg.toType == 2:
                    wN1.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
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
#==============================================================================#
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
                            gs = wN10.getGroup(msg.to)
                            gs = wN13.getGroup(msg.to)
                            gs = wN14.getGroup(msg.to)
                            gs = wN15.getGroup(msg.to)
                            gs = wN16.getGroup(msg.to)
                            gs = wN17.getGroup(msg.to)
                            gs = wN18.getGroup(msg.to)
                            gs = wN21.getGroup(msg.to)
                            gs = wN22.getGroup(msg.to)
                            gs = wN23.getGroup(msg.to)
                            gs = wN24.getGroup(msg.to)
                            gs = wN25.getGroup(msg.to) 
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
            elif msg.text in ["Salam1"]:
                wN1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN2.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                wN1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                wN2.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
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
            
            elif ("Gname: " in msg.text):
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = wN1.getGroup(msg.to)
                        X.name = msg.text.replace("Gname: ","")
                        wN1.updateGroup(X)
            
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
            
            elif msg.text.lower() == 'grup id':
                if msg.from_ in owner:
                    gid = wN1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (wN1.getGroup(i).name,i)
                    wN1.sendText(msg.to,h)
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
                         
            elif "Auto add" in msg.text:
                if msg.from_ in admin:
                    thisgroup = wN1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    wN1.findAndAddContactsByMids(mi_d)
                    wN1.sendText(msg.to,"Success Add all")
                    
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
                gs = wN11.getGroup(msg.to)
                gs = wN12.getGroup(msg.to)
                gs = wN13.getGroup(msg.to)
                gs = wN14.getGroup(msg.to)
                gs = wN15.getGroup(msg.to)
                gs = wN16.getGroup(msg.to)
                gs = wN17.getGroup(msg.to)
                gs = wN18.getGroup(msg.to)
                gs = wN19.getGroup(msg.to)
                gs = wN20.getGroup(msg.to)
                gs = wN21.getGroup(msg.to)
                gs = wN22.getGroup(msg.to)
                gs = wN23.getGroup(msg.to)
                gs = wN24.getGroup(msg.to)
                gs = wN25.getGroup(msg.to)
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
                gs = wN6.getGroup(msg.to)
                gs = wN7.getGroup(msg.to)
                gs = wN8.getGroup(msg.to)
                gs = wN9.getGroup(msg.to)
                gs = wN10.getGroup(msg.to)
                gs = wN11.getGroup(msg.to)
                gs = wN12.getGroup(msg.to)
                gs = wN13.getGroup(msg.to)
                gs = wN14.getGroup(msg.to)
                gs = wN15.getGroup(msg.to)
                gs = wN16.getGroup(msg.to)
                gs = wN17.getGroup(msg.to)
                gs = wN18.getGroup(msg.to)
                gs = wN19.getGroup(msg.to)
                gs = wN20.getGroup(msg.to)
                gs = wN21.getGroup(msg.to)
                gs = wN22.getGroup(msg.to)
                gs = wN23.getGroup(msg.to)
                gs = wN24.getGroup(msg.to)
                gs = wN25.getGroup(msg.to)
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
                    wN11.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN12.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN13.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN14.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN15.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN16.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN17.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN18.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN19.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN20.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN21.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN22.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN23.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN24.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    wN25.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    G = wN1.getGroup(msg.to)
                    ginfo = wN1.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    wN1.updateGroup(G)
                    wN5.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
                    print "Semua Sudah Lengkap"
                        
            elif "Kabur all" in msg.text:#keluar semua bots
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
                        ginfo = wN11.getGroup(msg.to)
                        ginfo = wN12.getGroup(msg.to)
                        ginfo = wN13.getGroup(msg.to)
                        ginfo = wN14.getGroup(msg.to)
                        ginfo = wN15.getGroup(msg.to)
                        ginfo = wN16.getGroup(msg.to)
                        ginfo = wN17.getGroup(msg.to)
                        ginfo = wN18.getGroup(msg.to)
                        ginfo = wN19.getGroup(msg.to)
                        ginfo = wN20.getGroup(msg.to)
                        ginfo = wN21.getGroup(msg.to)
                        ginfo = wN22.getGroup(msg.to)
                        ginfo = wN23.getGroup(msg.to)
                        ginfo = wN24.getGroup(msg.to)
                        ginfo = wN25.getGroup(msg.to)
                        try:
                            wN1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN2.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN5.leaveGroup(msg.to)
                            wN6.leaveGroup(msg.to)
                            wN7.leaveGroup(msg.to)
                            wN8.leaveGroup(msg.to)
                            wN9.leaveGroup(msg.to)
                            wN10.leaveGroup(msg.to)
                            wN11.leaveGroup(msg.to)
                            wN12.leaveGroup(msg.to)
                            wN13.leaveGroup(msg.to)
                            wN14.leaveGroup(msg.to)
                            wN15.leaveGroup(msg.to)
                            wN16.leaveGroup(msg.to)
                            wN17.leaveGroup(msg.to)
                            wN18.leaveGroup(msg.to)
                            wN19.leaveGroup(msg.to)
                            wN20.leaveGroup(msg.to)
                            wN21.leaveGroup(msg.to)
                            wN22.leaveGroup(msg.to)
                            wN23.leaveGroup(msg.to)
                            wN24.leaveGroup(msg.to)
                            wN25.leaveGroup(msg.to)
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
                        ginfo = wN6.getGroup(msg.to)
                        ginfo = wN7.getGroup(msg.to)
                        ginfo = wN8.getGroup(msg.to)
                        ginfo = wN9.getGroup(msg.to)
                        ginfo = wN10.getGroup(msg.to)
                        ginfo = wN11.getGroup(msg.to)
                        ginfo = wN12.getGroup(msg.to)
                        ginfo = wN13.getGroup(msg.to)
                        ginfo = wN14.getGroup(msg.to)
                        ginfo = wN15.getGroup(msg.to)
                        ginfo = wN16.getGroup(msg.to)
                        ginfo = wN17.getGroup(msg.to)
                        ginfo = wN18.getGroup(msg.to)
                        ginfo = wN19.getGroup(msg.to)
                        ginfo = wN20.getGroup(msg.to)
                        ginfo = wN21.getGroup(msg.to)
                        ginfo = wN22.getGroup(msg.to)
                        ginfo = wN23.getGroup(msg.to)
                        ginfo = wN24.getGroup(msg.to)
                        ginfo = wN25.getGroup(msg.to)
                        try:
                            wN2.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN3.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN4.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN5.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN6.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN7.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN8.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN9.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN10.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN11.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN12.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN13.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN14.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN15.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN16.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN17.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN18.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN19.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN20.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN21.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN22.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN23.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN24.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            wN25.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")   
                            wN2.leaveGroup(msg.to)
                            wN3.leaveGroup(msg.to)
                            wN4.leaveGroup(msg.to)
                            wN5.leaveGroup(msg.to)
                            wN6.leaveGroup(msg.to)
                            wN7.leaveGroup(msg.to)
                            wN8.leaveGroup(msg.to)
                            wN9.leaveGroup(msg.to)
                            wN10.leaveGroup(msg.to)
                            wN11.leaveGroup(msg.to)
                            wN12.leaveGroup(msg.to)
                            wN13.leaveGroup(msg.to)
                            wN14.leaveGroup(msg.to)
                            wN15.leaveGroup(msg.to)
                            wN16.leaveGroup(msg.to)
                            wN17.leaveGroup(msg.to)
                            wN18.leaveGroup(msg.to)
                            wN19.leaveGroup(msg.to)
                            wN20.leaveGroup(msg.to)
                            wN21.leaveGroup(msg.to)
                            wN22.leaveGroup(msg.to)
                            wN23.leaveGroup(msg.to)
                            wN24.leaveGroup(msg.to)
                            wN25.leaveGroup(msg.to)
                            #wN1.leaveGroup(msg.to)
                        except:
                            pass
#==============================================================================#
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
                    #cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    wN1.sendText(msg.to,"Ciluk baa...😲😲")
                    wN1.sendMessage(cnt)

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

            elif msg.text in ["Lihat","lihat"]:
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
            
            elif "Spam change: " in msg.text:
                if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam change: ","")
                    wN1.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam add: ","")
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"spam changed")
                    else:
                        wN1.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                if msg.from_ in admin:
                    strnum = msg.text.replace("Spam: ","")
                    num = int(strnum)
                    for var in range(0,num):
                        wN1.sendText(msg.to, wait['spam'])
            
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
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN1.sendMessage(msg)
                            wN1.sendMessage(msg)
                        else:
                            pass
            
            elif "#spam" in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("#Spam "+str(txt[1])+" "+str(jmlh)+" ","")
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
                    
            elif msg.text in ["Miclist"]:
                if msg.from_ in admin:
                    if mimic["target"] == {}:
                        wN1.sendText(msg.to,"nothing")
                    else:
                        mc = "Target mimic user\n"
                        for mi_d in mimic["target"]:
                            mc += "?? "+wN1.getContact(mi_d).displayName + "\n"
                        wN1.sendText(msg.to,mc)

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
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN11.getProfile()
                        profile.displayName = string
                        wN11.updateProfile(profile)
                        wN11.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN12.getProfile()
                        profile.displayName = string
                        wN12.updateProfile(profile)
                        wN12.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN13.getProfile()
                        profile.displayName = string
                        wN13.updateProfile(profile)
                        wN13.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN14.getProfile()
                        profile.displayName = string
                        wN14.updateProfile(profile)
                        wN14.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN15.getProfile()
                        profile.displayName = string
                        wN15.updateProfile(profile)
                        wN15.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN16.getProfile()
                        profile.displayName = string
                        wN16.updateProfile(profile)
                        wN16.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN17.getProfile()
                        profile.displayName = string
                        wN17.updateProfile(profile)
                        wN17.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN18.getProfile()
                        profile.displayName = string
                        wN18.updateProfile(profile)
                        wN18.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN19.getProfile()
                        profile.displayName = string
                        wN19.updateProfile(profile)
                        wN19.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN20.getProfile()
                        profile.displayName = string
                        wN20.updateProfile(profile)
                        wN20.sendText(msg.to,"Changed " + string + "")  
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN21.getProfile()
                        profile.displayName = string
                        wN21.updateProfile(profile)
                        wN21.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN22.getProfile()
                        profile.displayName = string
                        wN22.updateProfile(profile)
                        wN22.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN23.getProfile()
                        profile.displayName = string
                        wN23.updateProfile(profile)
                        wN23.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN24.getProfile()
                        profile.displayName = string
                        wN24.updateProfile(profile)
                        wN24.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN25.getProfile()
                        profile.displayName = string
                        wN25.updateProfile(profile)
                        wN25.sendText(msg.to,"Changed " + string + "")       
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
            elif "Namebot11: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot11: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN11.getProfile()
                        profile.displayName = string
                        wN11.updateProfile(profile)
                        wN11.sendText(msg.to,"Changed " + string + "")
            elif "Namebot12: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot12: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN12.getProfile()
                        profile.displayName = string
                        wN12.updateProfile(profile)
                        wN12.sendText(msg.to,"Changed " + string + "")
            elif "Namebot13: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot13: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN13.getProfile()
                        profile.displayName = string
                        wN13.updateProfile(profile)
                        wN13.sendText(msg.to,"Changed " + string + "")
            elif "Namebot14: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebo1t14: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN14.getProfile()
                        profile.displayName = string
                        wN14.updateProfile(profile)
                        wN14.sendText(msg.to,"Changed " + string + "")
            elif "Namebot15: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot15: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN15.getProfile()
                        profile.displayName = string
                        wN15.updateProfile(profile)
                        wN15.sendText(msg.to,"Changed " + string + "")
            elif "Namebot16: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot16: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN16.getProfile()
                        profile.displayName = string
                        wN16.updateProfile(profile)
                        wN16.sendText(msg.to,"Changed " + string + "")
            elif "Namebot17: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot17: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN17.getProfile()
                        profile.displayName = string
                        wN17.updateProfile(profile)
                        wN17.sendText(msg.to,"Changed " + string + "")
            elif "Namebot18: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot18: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN18.getProfile()
                        profile.displayName = string
                        wN18.updateProfile(profile)
                        wN18.sendText(msg.to,"Changed " + string + "")
            elif "Namebot19: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot19: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN19.getProfile()
                        profile.displayName = string
                        wN19.updateProfile(profile)
                        wN19.sendText(msg.to,"Changed " + string + "")
            elif "Namebot20: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot20: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN20.getProfile()
                        profile.displayName = string
                        wN20.updateProfile(profile)
                        wN20.sendText(msg.to,"Changed " + string + "")  
            elif "Namebot21: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot21: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN21.getProfile()
                        profile.displayName = string
                        wN21.updateProfile(profile)
                        wN21.sendText(msg.to,"Changed " + string + "")
            elif "Namebot22: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot22: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN22.getProfile()
                        profile.displayName = string
                        wN22.updateProfile(profile)
                        wN22.sendText(msg.to,"Changed " + string + "")
            elif "Namebot23: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot23: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN23.getProfile()
                        profile.displayName = string
                        wN23.updateProfile(profile)
                        wN23.sendText(msg.to,"Changed " + string + "")
            elif "Namebot24: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebo1t24: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN24.getProfile()
                        profile.displayName = string
                        wN24.updateProfile(profile)
                        wN24.sendText(msg.to,"Changed " + string + "")
            elif "Namebot25: " in msg.text:
                if msg.from_ in owner:
                    string = msg.text.replace("Namebot25: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN25.getProfile()
                        profile.displayName = string
                        wN25.updateProfile(profile)
                        wN25.sendText(msg.to,"Changed " + string + "")               
                        
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
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN11.getProfile()
                        profile.statusMessage = string
                        wN11.updateProfile(profile)
                        wN11.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN12.getProfile()
                        profile.statusMessage = string
                        wN12.updateProfile(profile)
                        wN12.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN13.getProfile()
                        profile.statusMessage = string
                        wN13.updateProfile(profile)
                        wN13.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN14.getProfile()
                        profile.statusMessage = string
                        wN14.updateProfile(profile)
                        wN14.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN15.getProfile()
                        profile.statusMessage = string
                        wN15.updateProfile(profile)
                        wN15.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN16.getProfile()
                        profile.statusMessage = string
                        wN16.updateProfile(profile)
                        wN16.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN17.getProfile()
                        profile.statusMessage = string
                        wN17.updateProfile(profile)
                        wN17.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN18.getProfile()
                        profile.statusMessage = string
                        wN18.updateProfile(profile)
                        wN18.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN19.getProfile()
                        profile.statusMessage = string
                        wN19.updateProfile(profile)
                        wN19.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN20.getProfile()
                        profile.statusMessage = string
                        wN20.updateProfile(profile)
                        wN20.sendText(msg.to,"Changed " + string)      
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN21.getProfile()
                        profile.statusMessage = string
                        wN21.updateProfile(profile)
                        wN21.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN22.getProfile()
                        profile.statusMessage = string
                        wN22.updateProfile(profile)
                        wN22.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN23.getProfile()
                        profile.statusMessage = string
                        wN23.updateProfile(profile)
                        wN23.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN24.getProfile()
                        profile.statusMessage = string
                        wN24.updateProfile(profile)
                        wN24.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = wN25.getProfile()
                        profile.statusMessage = string
                        wN25.updateProfile(profile)
                        wN25.sendText(msg.to,"Changed " + string)       
            elif msg.text in ["Myname"]:
                    h = wN1.getContact(mid)
                    wN1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybot"]:
                    h = wN1.getContact(mid)
                    h = wN2.getContact(mid2)
                    h = wN3.getContact(mid3)
                    h = wN4.getContact(mid4)
                    h = wN5.getContact(mid5)
                    h = wN6.getContact(mid6)
                    h = wN7.getContact(mid7)
                    h = wN8.getContact(mid8)
                    h = wN9.getContact(mid9)
                    h = wN10.getContact(mid10)
                    h = wN11.getContact(mid11)
                    h = wN12.getContact(mid12)
                    h = wN13.getContact(mid13)
                    h = wN14.getContact(mid14)
                    h = wN15.getContact(mid15)
                    h = wN16.getContact(mid16)
                    h = wN17.getContact(mid17)
                    h = wN18.getContact(mid18)
                    h = wN19.getContact(mid19)
                    h = wN20.getContact(mid20)
                    h = wN21.getContact(mid21)
                    h = wN22.getContact(mid22)
                    h = wN23.getContact(mid23)
                    h = wN24.getContact(mid24)
                    h = wN25.getContact(mid25)
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
                    wN11.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN12.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN13.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN14.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN15.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN16.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN17.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN18.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN19.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN20.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN21.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN22.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN23.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN24.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    wN25.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
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
                
            elif msg.text.lower() == 'welcome':
                ginfo = wN1.getGroup(msg.to)
                wN1.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                wN1.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                wN1.sendAudio(msg.to,'tts.mp3')
            
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
                
            elif "Kapan " in msg.text:
                tanya = msg.text.replace("Kapan ","")
                jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                wN1.sendAudio(msg.to,'tts.mp3')
                wN1.sendText(msg.to,jawaban)
                wN2.sendText(msg.to,jawaban)
                wN2.sendText(msg.to,jawaban)
                  
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                wN1.sendAudio(msg.to,'tts.mp3')
                wN1.sendText(msg.to,jawaban)
                wN2.sendText(msg.to,jawaban)
                wN2.sendText(msg.to,jawaban)
                  
            elif "Nah" in msg.text:
                wN1.sendText(msg.to,'Kan')
                wN3.sendText(msg.to,'Kan')
                wN2.sendText(msg.to,'Kan')
            
            elif "Absen" in msg.text:
                if msg.from_ in admin:
                    wN1.sendText(msg.to,"👉★1★√")
                    wN2.sendText(msg.to,"👉★2★√")
                    wN3.sendText(msg.to,"👉★3★√")
                    wN4.sendText(msg.to,"👉★4★√")
                    wN5.sendText(msg.to,"👉★5★√")
                    wN6.sendText(msg.to,"👉★6★√")
                    wN7.sendText(msg.to,"👉★7★√")
                    wN8.sendText(msg.to,"👉★8★√")
                    wN9.sendText(msg.to,"👉★9★√")
                    wN10.sendText(msg.to,"👉★10★√")
                    wN11.sendText(msg.to,"👉★11★√")
                    wN12.sendText(msg.to,"👉★12★√")
                    wN13.sendText(msg.to,"👉★13★√")
                    wN14.sendText(msg.to,"👉★14★√")
                    wN15.sendText(msg.to,"👉★15★√")
                    wN16.sendText(msg.to,"👉★16★√")
                    wN17.sendText(msg.to,"👉★17★√")
                    wN18.sendText(msg.to,"👉★18★√")
                    wN19.sendText(msg.to,"👉★19★√")
                    wN20.sendText(msg.to,"👉★20★√")
                    wN21.sendText(msg.to,"👉★21★√")
                    wN22.sendText(msg.to,"👉★22★√")
                    wN23.sendText(msg.to,"👉★23★√")
                    wN24.sendText(msg.to,"👉★24★√")
                    wN25.sendText(msg.to,"👉★25★√")
                    wN1.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
            
            elif "Bcast " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Bcast ","")
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        wN1.sendText(i,"●▬▬▬▬ஜ۩[BROADCAST]۩ஜ▬▬▬▬●\n\n"+bc+"\n\n#BROADCAST!!")
            
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

            elif msg.text in ["Kalender","Waktu"]:
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
#==============================================================================#
            elif msg.text.lower() == '#ifconfig':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == '#system':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == '#kernel':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == '#cpu':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    wN1.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
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
                    gid = wN6.getGroupIdsJoined()
                    gid = wN7.getGroupIdsJoined()
                    gid = wN8.getGroupIdsJoined()
                    gid = wN9.getGroupIdsJoined()
                    gid = wN10.getGroupIdsJoined()
                    gid = wN11.getGroupIdsJoined()
                    gid = wN12.getGroupIdsJoined()
                    gid = wN13.getGroupIdsJoined()
                    gid = wN14.getGroupIdsJoined()
                    gid = wN15.getGroupIdsJoined()
                    gid = wN16.getGroupIdsJoined()
                    gid = wN17.getGroupIdsJoined()
                    gid = wN18.getGroupIdsJoined()
                    gid = wN19.getGroupIdsJoined()
                    gid = wN20.getGroupIdsJoined()
                    gid = wN21.getGroupIdsJoined()
                    gid = wN22.getGroupIdsJoined()
                    gid = wN23.getGroupIdsJoined()
                    gid = wN24.getGroupIdsJoined()
                    gid = wN25.getGroupIdsJoined()
                    for i in gid:
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
                        wN11.leaveGroup(i)
                        wN12.leaveGroup(i)
                        wN13.leaveGroup(i)
                        wN14.leaveGroup(i)
                        wN15.leaveGroup(i)
                        wN16.leaveGroup(i)
                        wN17.leaveGroup(i)
                        wN18.leaveGroup(i)
                        wN19.leaveGroup(i)
                        wN20.leaveGroup(i)
                        wN21.leaveGroup(i)
                        wN22.leaveGroup(i)
                        wN23.leaveGroup(i)
                        wN24.leaveGroup(i)
                        wN25.leaveGroup(i)
                    if wait["lang"] == "JP":
                        wN1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        wN1.sendText(msg.to,"He declined all invitations")
                        
            elif msg.text in ["#cab","#Cab"]:
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
                
            elif msg.text in ["#Team","#Logo"]:
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
                    wN13.sendImageWithURL(msg.to, url1)
                    wN11.sendImageWithURL(msg.to, url2)
                    wN12.sendImageWithURL(msg.to, url3)
                    wN15.sendImageWithURL(msg.to, url4)
                    wN14.sendImageWithURL(msg.to, url5)
                    wN23.sendImageWithURL(msg.to, url6)
                    wN22.sendImageWithURL(msg.to, url7)
                
            elif msg.text in ["#Kibar","#kibar"]:
                if msg.from_ in admin:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    wN21.sendImageWithURL(msg.to, url)
                    wN12.sendImageWithURL(msg.to, url1)
                    wN23.sendImageWithURL(msg.to, url6)
                    wN14.sendImageWithURL(msg.to, url7)
#================================ CBW SCRIPT STARTED ==============================================#
            elif "google " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    wN1.sendText(msg.to,"Sedang Mencari om...")
                    wN1.sendText(msg.to, "https://www.google.com/" + b)
                    wN1.sendText(msg.to,"Ketemu om ^")

            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc301fa8f0962f52b1f2d83dc251589cb"}
                wN1.sendMessage(msg)

            elif "friendpp: " in msg.text:
                if msg.from_ in admin:
                    suf = msg.text.replace('friendpp: ','')
                    gid = wN1.getAllContactIds()
                    for i in gid:
                        h = wN1.getContact(i).displayName
                        gna = wN1.getContact(i)
                        if h == suf:
                            wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)

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
                
            elif "Friendpict: " in msg.text:
                if msg.from_ in owner:
                    saya = msg.text.replace('Friendpict: ','')
                    gid = wN1.getAllContactIds()
                    for i in gid:
                        h = wN1.getContact(i).displayName
                        gna = wN1.getContact(i)
                        if h == saya:
                            wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
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
                    
            elif "Grupimage: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupimage: ','')
                    gid = wN1.getGroupIdsJoined()
                    for i in gid:
                        h = wN1.getGroup(i).name
                        gna = wN1.getGroup(i)
                        if h == saya:
                            wN1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Grupname" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupname','')
                    gid = wN1.getGroup(msg.to)
                    wN1.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Grupid','')
                    gid = wN1.getGroup(msg.to)
                    wN1.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
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

            elif "playstore " in msg.text.lower():
                if msg.from_ in admin:
                    tob = msg.text.lower().replace("playstore ","")
                    wN1.sendText(msg.to,"Sedang Mencari boss...")
                    wN1.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    wN1.sendText(msg.to,"Ketemu boss ^")
                    
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
                            
            elif "say " in msg.text.lower():
                if msg.from_ in admin:
                    say = msg.text.lower().replace("say ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    wN1.sendAudio(msg.to,"hasil.mp3")
                
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
                
            elif "idline: " in msg.text:
                if msg.from_ in admin:
                    msgg = msg.text.replace('idline: ','')
                    conn = wN1.findContactsByUserid(msgg)
                    if True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': conn.mid}
                        wN1.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                        wN1.sendMessage(msg)
                        
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
                wN1.sendText(msg.to, rst)
                
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
                	
            elif msg.text in ["#Attack"]:
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
                
            elif msg.text.lower() == '###':
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN1.sendMessage(msg)    
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
            elif "Cab spamtag @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Cab spamtag @","")
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
                            wN2.sendMessage(msg)
                            wN3.sendMessage(msg)
                            wN4.sendMessage(msg)
                            wN5.sendMessage(msg)
                            wN6.sendMessage(msg)
                            wN7.sendMessage(msg)
                            wN8.sendMessage(msg)
                            wN9.sendMessage(msg)
                            wN5.sendMessage(msg)
                            wN10.sendMessage(msg)
                            wN2.sendMessage(msg)
                            wN3.sendMessage(msg)
                            wN4.sendMessage(msg)
                            wN5.sendMessage(msg)
                            wN10.sendMessage(msg)
                            wN6.sendMessage(msg)
                            wN7.sendMessage(msg)
                            wN8.sendMessage(msg)
                            wN9.sendMessage(msg)
                        else:
                            pass
                        
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
            elif "Cab megs " in msg.text:
                if msg.from_ in owner:
                    gName = msg.text.replace("Kr megs ","")
                    ap = wN1.getGroups([msg.to])
                    semua = [contact.mid for contact in ap[0].members]
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        wN1.createGroup(gName, semua)
                        wN2.createGroup(gName, semua)
                        wN3.createGroup(gName, semua)
                        wN4.createGroup(gName, semua)
                        wN5.createGroup(gName, semua)
                        wN6.createGroup(gName, semua)
                        wN7.createGroup(gName, semua)
                        wN8.createGroup(gName, semua)
                        wN9.createGroup(gName, semua)
                        wN10.createGroup(gName, semua)
                        wN4.createGroup(gName, semua)
                        wN1.createGroup(gName, semua)
                        wN11.createGroup(gName, semua)
                        wN12.createGroup(gName, semua)
                        wN13.createGroup(gName, semua)
                        wN14.createGroup(gName, semua)
                        wN15.createGroup(gName, semua)
                        wN16.createGroup(gName, semua)
                        wN17.createGroup(gName, semua)
                        wN18.createGroup(gName, semua)
                        wN19.createGroup(gName, semua)
                        wN10.createGroup(gName, semua)
                        wN24.createGroup(gName, semua)
                        wN21.createGroup(gName, semua)
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
                        wN2.createGroup(gName, semua)
                        wN3.createGroup(gName, semua)
                        wN4.createGroup(gName, semua)
                        wN5.createGroup(gName, semua)
                        wN6.createGroup(gName, semua)
                        wN7.createGroup(gName, semua)
                        wN8.createGroup(gName, semua)
                        wN9.createGroup(gName, semua)
                        wN10.createGroup(gName, semua)
                        wN12.createGroup(gName, semua)
                        wN13.createGroup(gName, semua)
                        wN14.createGroup(gName, semua)
                        wN15.createGroup(gName, semua)
                        wN16.createGroup(gName, semua)
                        wN17.createGroup(gName, semua)
                        wN18.createGroup(gName, semua)
                        wN19.createGroup(gName, semua)
                        wN10.createGroup(gName, semua)
                        wN11.createGroup(gName, semua)
                        team.findAndAddContactsByMid(Mi_d)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
            elif "recover" in msg.text:
                if msg.from_ in owner:
                    thisgroup = wN1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    wN1.createGroup("recover", mi_d)
                    wN1.sendText(msg.to,"Success recover")
            elif "Cab spin" in msg.text:
                if msg.from_ in owner:
                    thisgroup = wN1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    wN1.createGroup("Nah kan", mi_d)
                    wN2.createGroup("Nah kan", mi_d)
                    wN3.createGroup("Nah kan", mi_d)
                    wN4.createGroup("Nah kan", mi_d)
                    wN5.createGroup("Nah kan", mi_d)
                    wN1.createGroup("Nah kan", mi_d)
                    wN2.createGroup("Nah kan", mi_d)
                    wN3.createGroup("Nah kan", mi_d)
                    wN4.createGroup("Nah kan", mi_d)
                    wN5.createGroup("Nah kan", mi_d)
                    wN6.createGroup("Nah kan", mi_d)
                    wN7.createGroup("Nah kan", mi_d)
                    wN8.createGroup("Nah kan", mi_d)
                    wN9.createGroup("Nah kan", mi_d)
                    wN10.createGroup("Nah kan", mi_d)
                    wN6.createGroup("Nah kan", mi_d)
                    wN7.createGroup("Nah kan", mi_d)
                    wN8.createGroup("Nah kan", mi_d)
                    wN9.createGroup("Nah kan", mi_d)
                    wN10.createGroup("Nah kan", mi_d)
                    wN11.createGroup("Nah kan", mi_d)
                    wN12.createGroup("Nah kan", mi_d)
                    wN13.createGroup("Nah kan", mi_d)
                    wN14.createGroup("Nah kan", mi_d)
                    wN15.createGroup("Nah kan", mi_d)
                    wN11.createGroup("Nah kan", mi_d)
                    wN12.createGroup("Nah kan", mi_d)
                    wN13.createGroup("Nah kan", mi_d)
                    wN14.createGroup("Nah kan", mi_d)
                    wN15.createGroup("Nah kan", mi_d)
                    wN16.createGroup("Nah kan", mi_d)
                    wN17.createGroup("Nah kan", mi_d)
                    wN18.createGroup("Nah kan", mi_d)
                    wN19.createGroup("Nah kan", mi_d)
                    wN20.createGroup("Nah kan", mi_d)
                    wN16.createGroup("Nah kan", mi_d)
                    wN17.createGroup("Nah kan", mi_d)
                    wN18.createGroup("Nah kan", mi_d)
                    wN19.createGroup("Nah kan", mi_d)
                    wN10.createGroup("Nah kan", mi_d)
                    wN1.sendText(msg.to,"Success...!!!!")
            elif msg.text in ["Remove all chat"]:
                if msg.from_ in owner:
                    wN1.removeAllMessages(op.param2)
                    wN1.removeAllMessages(op.param2)
                    wN1.sendText(msg.to,"Removed all chat Finish")
            elif msg.text in ["Cab muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    wN1.sendMessage(msg)
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
                if op.param2 not in admin:
                    wN1.cancelGroupInvitation(op.param1,[op.param3])
                    wN1.kickoutFromGroup(op.param1,[op.param2])
                    if wait["inviteprotect"] == True:
                        wait ["blacklist"][op.param2] = True
                        if op.param2 in Bots or admin:
                            pass
                        if op.param2 not in admin:
                            wN1.cancelGroupInvitation(op.param1,[op.param3])
                            if wait["cancelprotect"] == True:
                                wait ["blacklist"][op.param2] = True
                                wN1.cancelGroupInvitation(op.param1,[op.param3])                                           
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
                    wN1.kickoutFromGroup(op.param1,[op.param3])
                    wN1.updateGroup(G)
        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = wN1.getGroup(op.param1)
               wN1.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc"] == True:
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
                
        if op.type == 15:
            if wait["Lv"] == True:
               if op.param2 in Bots:
                   return
               G = wN1.getGroup(op.param1)
               h = wN1.getContact(op.param2)
               wN1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
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
                            Name = wN1.getContact(op.param2).displayName
                            Name = wN2.getContact(op.param2).displayName
                            Name = wN3.getContact(op.param2).displayName
                            Name = wN4.getContact(op.param2).displayName
                            Name = wN5.getContact(op.param2).displayName
                            Name = wN6.getContact(op.param2).displayName
                            Name = wN7.getContact(op.param2).displayName
                            Name = wN8.getContact(op.param2).displayName
                            Name = wN9.getContact(op.param2).displayName
                            Name = wN10.getContact(op.param2).displayName 
                            Name = wN11.getContact(op.param2).displayName
                            Name = wN12.getContact(op.param2).displayName
                            Name = wN13.getContact(op.param2).displayName
                            Name = wN14.getContact(op.param2).displayName
                            Name = wN15.getContact(op.param2).displayName
                            Name = wN16.getContact(op.param2).displayName
                            Name = wN17.getContact(op.param2).displayName
                            Name = wN18.getContact(op.param2).displayName
                            Name = wN19.getContact(op.param2).displayName
                            Name = wN20.getContact(op.param2).displayName 
                            Name = wN21.getContact(op.param2).displayName
                            Name = wN22.getContact(op.param2).displayName
                            Name = wN23.getContact(op.param2).displayName
                            Name = wN24.getContact(op.param2).displayName
                            Name = wN25.getContact(op.param2).displayName
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
#    while True:
#        try:
#           for posts in wN1.activity(1)["result"]["posts"]:
#             if posts["postInfo"]["liked"] is False:
#                if wait['likeOn'] == True:
#                   wN1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   print "Like"
#                   if wait["commentOn"] == True:
#                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
#                         pass
#                      else:
#                          wN1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
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
#      hasil = wN1.activity(limit=20)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          wN1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
#          wN1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by CBW ⭐👈 »»» http://line.me/ti/p/~CBWsthea «««")
#          print "Like"
#        except:
#           pass
 #      else:
# print "Already Liked Om"
# time.sleep(0.60)

# def likeme():
#     for zx in range(0,20):
#         hasil = wN1.activity(limit=20)
#         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#             if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
#                try:
#                     wN1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#                     wN1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by CBW ⭐👈 »»» http://line.me/ti/p/~CBWsthea «««")
#                     print "Like"
#                 except:
#                    pass
#             else:
#                print "Status Sudah di Like Om"


while True:
    try:
        Ops = wN1.fetchOps(wN1.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(wN1.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            wN1.Poll.rev = max(wN1.Poll.rev, Op.revision)
            bot(Op)
