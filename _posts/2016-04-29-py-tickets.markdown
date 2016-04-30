---
layout:   post
title:    "Python 抓取 12306 余票信息"
subtitle: "Python 下海第一回"
date:     2016-04-29 16:33:29
author:   "Stephen"
header-img: "img/post-bg.jpg"
catalog: true
tag:
    - Python
    - Web Scraper
    - 12306
---

## 前情提要

临近五一，大家必然按耐不住自己归乡的情绪。我也不例外，所以早早计划买票回家。然而这烂记性是从小的毛病，怎么治也治不好，票的事情就一拖再拖。

直到放假前一个星期五，我突然醒悟过来：卧槽！票！！

然后急忙上了 12306 去找票，发现虽然不是一张没有，但都是晚上的了。这让我很纠结，况且我本来就有选择困难，这样一来更困难了：到底是现在就买还是等等买退票？但是如果等退票的话万一这有的票也没了那就麻烦了。

我想到了监控！

所以我写了一个小脚本。

## 实现过程

### 第一步

通过 Chrome 观察了 12306 的抓包过程，发现抓取的文件就是标准的 JSON 格式的文件，所以直接做解析就可以了！万事大吉！

接口的地址是：

> https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-04-29&from_station=TJP&to_station=SJP

数据信息通俗易懂:

* 票种 purpose_codes=ADULT
* 开车日期 queryDate=2016-04-29
* 出发站 from_station=TJP
* 到达站 to_station=SJP

猜想别的应用恐怕也是通过这个接口实现数据抓取的吧！我暂时还没有测试如果过度查询会不会封 IP ，但我觉得的应该是会的吧，要不太 BUG 了！

### 第二步

接下来就是写脚本了，过程也是相当简单，通过 Python 的预制 JSON 库就可以完成数据的分析。

然而还有一个需要注意的问题，那就是 Python 大小写敏感，所以不能识别 true 而只能识别 True 。所以需要先 replace 掉。

### 第三部

当获得数据后，确定所选车次，做简单判断即可。

设想中其实还有定时判断，邮件提醒的功能，奈何票量骤减，所以果断入手了，后续功能就没加进去。

## 代码

``` python
import requests
import json
import time

while 1:
    url="https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-04-29&from_station=TJP&to_station=SJP"
    s=requests.get(url,verify=False)
    b=s.text.replace("true","True")
    dic=eval(b)
    for i in dic['data']['datas']:
        if i['station_train_code'] == 'G6283':
            print(i['ze_num'])
        if i['station_train_code'] == 'D6725':
            print(i['ze_num'])    
    time.sleep(30)
```



