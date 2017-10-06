---
layout:   post
title:    "通过实例入门 Android （2）"
subtitle: ""
date:     2017-10-05 09:00:37
author:   "Stephen"
header-img: "img/post-bg.jpg"
catalog: true
tag:
    - Android
---
# 通过实例入门 Android （2）
---

```Java
package com.example.admin.myapplication;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // 默认调用父类方法
        super.onCreate(savedInstanceState);
        // 用于定义 MainActivity 的布局
        setContentView(R.layout.activity_main);
        // 由于是默认取消 ActionBar ，所以需要定义一个 Toolbar 来取代
        // findViewById 是常用方法用于寻找 layout 目录下布局的控件
        // setSupportActionBar 是设定 ActionBar
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        // 此处定义了一个右下角的一个浮动按钮，并设置了监听器
        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Snackbar 是下方弹出框控件
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });

        // DrawerLayout 是 Google 为适应 Material Design 所推出的支持，主要用于左侧抽屉滑动菜单
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        // ActionBarDrawerToggle 是 DrawerListener的实现，配合 DrawerLayout 使用的动画控制器（我是这么理解的）。
        // 自动添加拉出隐藏动画，改变 android.R.id.home 返回图标
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        // 据说是初始化状态，可以进行试验[?]
        toggle.syncState();

        // NavigationView 是抽屉菜单的主要内容，定义了头部和菜单部分
        // 此处用于添加监听器（因为实现了抽象类 NavigationView.OnNavigationItemSelectedListener）
        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
        } else if (id == R.id.nav_gallery) {

        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
```


1. MainActivity 是主活动的控制器，与在 manifest 文件中活动对应名称一致。
2. MainActivity 继承 AppCompatActivity ，是默认继承。
3. 重写 onCreate 方法用于在活动创建时调用。
4. 重写 onBackPressed 方法用于返回键点击时调用。当抽屉打开时点击返回则关闭。
5. 重写 onCreateOptionsMenu 方法用于添加默认菜单。
6. 重写 onOptionsItemSelected 方法用于默认添加菜单的事件监听。
7. 重写 onNavigationItemSelected 方法用于添加抽屉菜单监听，并关闭抽屉。
