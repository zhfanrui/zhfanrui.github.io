---
layout:   post
title:    "通过实例入门 Android （1）"
subtitle: "瞎鸡儿写着玩的"
date:     2017-10-04 09:55:25
author:   "Stephen"
header-img: "img/post-bg.jpg"
catalog: true
tag:
    - Android
---
# 通过实例入门 Android （1）
---
## 起源

我初始化了一个带有 NavigationBar 的符合 Material Design 的官方示例项目，想通过示例的运行方式与结果熟悉并上手 Android 开发。

## AndroidManifest.xml
``` xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.admin.myapplication">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity
            android:name=".MainActivity"
            android:label="@string/app_name"
            android:theme="@style/AppTheme.NoActionBar">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

1. 首先看 xml 标签定义了 xml 版本号与编码格式。
2. manifest 标签是整个内容的主标签。xmlns 是 xml namespace 的意思，定义了 android 的命名空间（一般来说对应关键字的命名空间是固定的）（实际上命名空间这个问题还是需要再次理解的）；package定义了包名，与项目设定一致。
3. application 标签定义的是一个应用[?]。
4. activity 定义了应用内的活动。name 表示活动名称，与之对应的是一个同名的Java Class，用于控制活动的进行；label 定义了应用的名称，此处调用了 res/valuse/strings 下的 app_name ；theme 定义了主题，此处调用了 res/valuse/strings 下的 AppTheme.NoActionBar ，意思是取消系统默认的 ActionBar 。一个应用可以有多个活动，而且可以都不为主活动。
5. intent-filter[?]
6. 整个应用注册是通过此文件执行的，并且有几个主 activity 就有几个图标，没有主的则没有图标。
