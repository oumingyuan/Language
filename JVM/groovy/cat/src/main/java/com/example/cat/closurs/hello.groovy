package com.example.cat.closurs

def greeting = { println("hello $it!") }


greeting("world")

/**
 * closures to traversal list
 */
[1, 2, 3, 4, 5,].each { println(it) }


["张三": 100, "李四": 200, "王五": 300].each { println(it) }

[1, 2, 3, 4, 5].each { num -> if (num % 2 == 0) println(num) }

def item = ["张三": 100, "李四": 200, "王五": 300].find { it.value > 100 }

println(item)

def items = ["张三": 100, "李四": 200, "王五": 300].findAll { it.value > 100 }

println(items)