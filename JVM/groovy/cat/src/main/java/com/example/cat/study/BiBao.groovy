package com.example.cat.study


def closure = { int a, String b ->

    println("a=${a},b=${b},I am closure")

}


def test = { a, b ->

    println("a=${a},b=${b},I am closure")
}

//def ryg = {y|y=a + b
//
//}

//println(ryg(100, 300))

closure(100, "hello")

test(1, 2)

//ryg(100, 200)

println()

//def y(x, y) {
//    return x + y
//}