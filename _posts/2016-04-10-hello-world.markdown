---
layout:     post
title:      "Hello 2015"
subtitle:   " \"Hello World, Hello Blog\""
date:       2016-04-09 12:00:00
author:     "Stephen"
header-img: "img/post-bg.jpg"
catalog: 	true
tags:
    - 综述
---


## 前言

这是我博客的第一篇。

恐怕我用了将近一天的时间才让整个系统运行起来，心情还是比较激动的。我打算写一个技术博客，也就是从2016年起，将以前学习的和将要学习的各种知识总结出来，相信也是对自己的一种激励，也是每个人必经的一个过程。

---

## 正文

接下来说说搭建这个博客的技术细节。  

正好之前就有关注过 [GitHub Pages](https://pages.github.com/) + [Jekyll](http://jekyllrb.com/) 快速 Building Blog 的技术方案，非常轻松时尚。

其优点非常明显：

* **Markdown** 带来的优雅写作体验
* 非常熟悉的 Git workflow ，**Git Commit 即 Blog Post**
* 利用 GitHub Pages 的域名和免费无限空间，不用自己折腾主机
	* 如果需要自定义域名，也只需要简单改改 DNS 加个 CNAME 就好了 
* Jekyll 的自定制非常容易，基本就是个模版引擎


个人也比较喜欢简洁与极客风格，并要求知识分类。所以说Jekyll是一个比较好的解决方案。

---

配置中的坑还是很多的。

* 首先是本地的 [Ruby](http://www.ruby-lang.org/en/) 安装出现问题，Windows 下并不好用，所以转型 [Ubuntu](http://www.ubuntu.com/) ，所以出现了第二个问题。后来发现可以不用本地服务器而直接云端调试，所以放弃本地。
	* Ubuntu 版本的使用要使用 **LTS** 版本，否则软件无法正常安装。
* 皮肤我是 folk Hux 大神的，关于修改理解包括弱智的拼写错误是整个工程耽误时间的原因。
	* Liquid 是网页模板语言，[后期我将进行总结]()。
	* HTML5 Boilerplate 模板是关于目录结构的，[后期我将进行总结]()。
* 再次我们看一下皮肤作者的原话

> Theme 的 CSS 是基于 Bootstrap 定制的，看得不爽的地方直接在 Less 里改就好了（平时更习惯 SCSS 些），**不过其实我一直觉得 Bootstrap 在移动端的体验做得相当一般，比我在淘宝参与的团队 CSS 框架差多了……**所以为了体验，也补了不少 CSS 进去。

* 本次修改并不完全，字体，图等没有做，预计于 V 2.0 版本完善。

> 第二天考虑中文字体的渲染，fork 了 [Type is Beautiful](http://www.typeisbeautiful.com/) 的 `font` CSS，调整了字号，适配了 Win 的渣渲染，中英文混排效果好多了。

## 后记

总之就是努力，毕竟小白，积累才是最重要的。


