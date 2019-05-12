package com.example.hello.study

class Person {


    var lastName: String = "zhang"
        get() = field.toUpperCase()

    var no: Int = 100
        set(value) {
            field = if (value < 10) {
                value
            } else {
                -1
            }
        }

    var height: Float = 145.4f
        private set

}

fun main() {
    val person: Person = Person()

    person.lastName = "wang"

    println("lastName: ${person.lastName}")

    person.no = 9
    println("no:${person.no}")

    person.no = 20
    println("no: ${person.no}")

}


