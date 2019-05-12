package com.example.hello.study

/*

the different between class and object

 */

// class definition

//if the class is not used, there will be a line under it
class Runoob {
    //the name of class
    //the function in class
    fun foo() {
        print("foo function")
    }

    //the attribute of class
    var name: String = "oumingyuan"
    var age: String = "18"
}

//an empty class
class Empty

fun main() {

    //we can get object without new keyword
    val runoobObject = Runoob()

    //we can get the attribute by object name + .
    println(runoobObject.name)
    println(runoobObject.age)
}


