import os
import time
import codecs

t1=time.strftime("%Y-%m-")
t2='%02d'%(int(time.strftime("%d"))-1)
c=input('name')
name=t1+t2+'-'+c+'.markdown'
fp=codecs.open(name,'w','utf-8')
title=input('title')
subtitle=input('subtitle')


t3=time.strftime(" %H:%M:%S")
date=t1+t2+t3

str='''---
layout:  post
title:   "%s"
subtitle:"%s"
date:    %s
auther:  "Stephen"
header-img: "img/post-bg.jpg"
catalog: true
tag:
    - 
---
'''%(title,subtitle,date)

fp.write(str)
fp.close()