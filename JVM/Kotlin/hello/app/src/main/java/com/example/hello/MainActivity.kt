package com.example.hello

import android.os.Bundle
import android.support.design.widget.BottomNavigationView
import android.support.v7.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

/**
 * main activity
 * 主要的活动
 *
 * application compat activity
 * 应用兼容活动
 *
 *
 * 继承关系
 */
class MainActivity : AppCompatActivity() {

    /**
     * 属性定义
     */
    private val mOnNavigationItemSelectedListener = BottomNavigationView.OnNavigationItemSelectedListener { item ->
        when (item.itemId) {
            R.id.navigation_home -> {
                message.setText(R.string.title_home)
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_dashboard -> {
                message.setText(R.string.title_dashboard)
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_notifications -> {
                message.setText(R.string.title_notifications)
                return@OnNavigationItemSelectedListener true
            }
        }
        false
    }

    /**
     * ? 代表空间可以存 null
     */
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)


        //设置主页面
        setContentView(R.layout.activity_main)

//        setContentView(R.layout)

        //貌似是增加监听事件
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener)
    }
}
