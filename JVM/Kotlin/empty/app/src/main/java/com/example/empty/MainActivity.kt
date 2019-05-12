package com.example.empty

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /**
         * 按钮1的单击事件
         */
        button1.setOnClickListener {
            Toast.makeText(this, "点击了", Toast.LENGTH_SHORT).show()
        }

        /**
         * 按钮2的单击事件
         */
        button_password.setOnClickListener {

            Toast.makeText(this, editText_password.text, Toast.LENGTH_SHORT).show()

        }
    }
}
