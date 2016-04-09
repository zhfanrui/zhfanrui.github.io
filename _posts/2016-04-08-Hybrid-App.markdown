---
layout:  post
title:   "Native.js 的开发"
subtitle: "HTML5 App 开发"
date:    2016-04-08 23:58:32
author:  "Stephen"
header-img: "img/post-bg.jpg"
catalog: true
tag:
    - NJS
    - HTML5
    - HTML
---

> [NJS官方文档](http://ask.dcloud.net.cn/article/88)
> [5+ App开发Native.js入门指南](http://ask.dcloud.net.cn/article/88)

## 概述
Native.js技术，简称NJS，是一种将手机操作系统的原生对象转义，映射为JS对象，在JS里编写原生代码的技术。
如果说Node.js把js扩展到服务器世界，那么Native.js则把js扩展到手机App的原生世界。
HTML/JS/Css全部语法只有7万多，而原生语法有几十万，Native.js大幅提升了HTML5的能力。
NJS突破了浏览器的功能限制，也不再需要像Hybrid那样由原生语言开发插件才能补足浏览器欠缺的功能。
NJS编写的代码，最终需要在HBuilder里打包发行为App安装包，或者在支持Native.js技术的浏览器里运行。目前Native.js技术不能在普通手机浏览器里直接运行。


NJS大幅扩展了HTML5的能力范围，原本只有原生或Hybrid App的原生插件才能实现的功能如今可以使用JS实现。

NJS大幅提升了App开发效率，将iOS、Android、Web的3个工程师组队才能完成的App，变为1个web工程师就搞定。

NJS不再需要配置原生开发和编译环境，调试、打包均在HBuilder里进行。没有mac和xcode一样可以开发iOS应用。

如果不熟悉原生API也没关系，我们汇总了很多NJS的代码示例，复制粘贴就可以用。http://ask.dcloud.net.cn/article/114

再次强调，Native.js不是一个js库，不需要下载引入到页面的script中，也不像nodejs那样有单独的运行环境，Native.js的运行环境是集成在5+runtime里的，使用HBuilder打包的app或流应用都可以直接使用Native.js。


## 开始使用

### 判断平台

Native API具有平台依赖性，所以需要通过以下方式判断当前的运行平台：
``` javascript
function judgePlatform(){
    switch ( plus.os.name ) {
        case "Android":
        // Android平台: plus.android.*
        break;
        case "iOS":
        // iOS平台: plus.ios.*
        break;
        default:
        // 其它平台
        break;
    }
}
```

### Hello World
``` javascript
/**
 * 在Android平台通过NJS显示系统提示框
 */
function njsAlertForAndroid(){
    // 导入AlertDialog类
    var AlertDialog = plus.android.importClass("android.app.AlertDialog");
    // 创建提示框构造对象，构造函数需要提供程序全局环境对象，通过plus.android.runtimeMainActivity()方法获取
    var dlg = new AlertDialog.Builder(plus.android.runtimeMainActivity());
    // 设置提示框标题
    dlg.setTitle("自定义标题");
    // 设置提示框内容
    dlg.setMessage("使用NJS的原生弹出框，可自定义弹出框的标题、按钮");
    // 设置提示框按钮
    dlg.setPositiveButton("确定(或者其他字符)",null);
    // 显示提示框
    dlg.show();
}
//...
```
`注意：NJS代码中创建提示框构造对象要求传入程序全局环境对象，可通过plus.android.runtimeMainActivity()方法获取应用的主Activity对象，它是HTML5+应用运行期自动创建的程序全局环境对象。`

`注意：其实HTML5+规范已经封装过原生提示框消息API：plus.ui.alert( message, alertCB, title, buttonCapture)。此处NJS的示例仅为了开发者方便理解，实际使用时调用plus.ui.alert更简单，性能也更高。`


``` javascript
/**
 * 在iOS平台通过NJS显示系统提示框
 */
function njsAlertForiOS(){
    // 导入UIAlertView类
    var UIAlertView = plus.ios.importClass("UIAlertView");
    // 创建UIAlertView类的实例对象
    var view = new UIAlertView();
    // 设置提示对话上的内容
    view.initWithTitlemessagedelegatecancelButtonTitleotherButtonTitles("自定义标题" // 提示框标题
        , "使用NJS的原生弹出框，可自定义弹出框的标题、按钮" // 提示框上显示的内容
        , null // 操作提示框后的通知代理对象，暂不设置
        , "确定(或者其他字符)" // 提示框上取消按钮的文字
        , null ); // 提示框上其它按钮的文字，设置为null表示不显示
    // 调用show方法显示提示对话框，在JS中使用()语法调用对象的方法
    view.show();
}
//...
```
`注意：在OC语法中方法的定义格式为:
“(返回值类型) 函数名: (参数1类型) 形参1 参数2名称: (参数2类型) 形参2”
方法的完整名称为: “函数名:参数2名称:”。
如:“（void）setPositionX:(int)x Y:(int)y;”，方法的完整名称为“setPositionX:Y:”
调用时语法为：“[pos setPositionX:x Y:y];”。
在JS语法中函数名称不能包含“:”字符，所以OC对象的方法名映射成NJS对象方法名时将其中的“:”字符自动删除，上面方法名映射为“setPositionXY”，在NJS调用的语法为：“pos.setPositionXY(x,y);”。`

## Debuging

