package com.example.hello.study.kong

fun main() {

//    val age: String? = "23"
    val age: String? = null
//    val name: String = null   //报错
    val school: String? = null

//    val ages = age!!.toInt()
//    val ages = age?.toInt()

    //age为空返回-1
    val ages = age?.toInt() ?: -1
    println(ages)

}