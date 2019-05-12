package com.example.cat.io


def file = new File("a.txt")

println("read file using two parameters")

file.eachLine { line, lineNo ->

    println("${lineNo} ${line}")

}

println("read file using one parameters")

file.eachLine { line ->

    println("${line}")
}


new File('a.txt').eachLine('UTF-8') {

    println(it)

}
