---
layout:   post
title:    "手写 Python 爬虫"
subtitle: "医学文献处理引擎"
date:     2016-04-27 16:46:10
author:   "Stephen"
header-img: "img/post-bg.jpg"
catalog: true
tag:
    - Python
    - Web Scraper
---

## 前情提要

在蹭 [李建伟]() 老师的 [操作系统]() 课的时候，有一天他突然问起谁会 HTML ，我当然义不容辞的举手了。所以才有了一切的一切。

他带的研究生正在做一个关于医学的 APP 的课题，需要数据处理，而整个项目的难点在于：** 所有的文献是从不同的网站上保存下来的，所以文件的格式不尽相同 **。

## 解决方案一

一开始我认为，正则表达式是可以解决这个问题的。但经过多次调试发现次法并不好用。所以我咨询了正在教我们课的老师 Dr. Giovanni ，然后他的答复让我真正的省去了很多的麻烦。

## 解决方案二

Dr. Giovanni 让我使用一个 Python 库，名为 [BeautifulSoup]() 。这个库十分强大，可直接分析 HTML 语句，并且查找也十分方便。




