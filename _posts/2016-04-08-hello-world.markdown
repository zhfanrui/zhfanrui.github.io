---
layout:     post
title:      "Hello 2015"
subtitle:   " \"Hello World, Hello Blog\""
date:       2015-01-29 12:00:00
author:     "Stephen"
header-img: "img/post-bg.jpg"
catalog: 	true
tags:
    - 生活
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

* 首先是本地的
*
*


配置的过程中也没遇到什么坑，基本就是 Git 的流程，相当顺手

大的 Jekyll 主题上直接 fork 了 Clean Blog（这个主题也相当有名，就不多赘述了。唯一的缺点大概就是没有标签支持，于是我给它补上了。）

本地调试环境需要 `gem install jekyll`，结果 rubygem 的源居然被墙了……后来手动改成了我大淘宝的镜像源才成功

Theme 的 CSS 是基于 Bootstrap 定制的，看得不爽的地方直接在 Less 里改就好了（平时更习惯 SCSS 些），**不过其实我一直觉得 Bootstrap 在移动端的体验做得相当一般，比我在淘宝参与的团队 CSS 框架差多了……**所以为了体验，也补了不少 CSS 进去

最后就进入了耗时反而最长的**做图、写字**阶段，也算是进入了**写博客**的正轨，因为是类似 Hack Day 的方式去搭这个站的，所以折腾折腾着大半夜就过去了。

第二天考虑中文字体的渲染，fork 了 [Type is Beautiful](http://www.typeisbeautiful.com/) 的 `font` CSS，调整了字号，适配了 Win 的渣渲染，中英文混排效果好多了。


## 后记

回顾这个博客的诞生，纯粹是出于个人兴趣。在知乎相关问题上回答并获得一定的 star 后，我决定把这个博客主题当作一个小小的开源项目来维护。

在经历 v1.0 - v1.5 的蜕变后，这个博客主题愈发完整，不但增加了诸多 UI 层的优化（opinionated）；在代码层面，更加丰富的配置项也使得这个主题拥有了更好的灵活性与可拓展性。而作为一个开源项目，我也积极的为其完善文档与解决 issue。

如果你恰好逛到了这里，希望你也能喜欢这个博客主题。

—— Hux 后记于 2015.10


