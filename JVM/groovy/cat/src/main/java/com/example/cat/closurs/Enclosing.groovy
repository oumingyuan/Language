package com.example.cat.closurs

class Enclosing {
    void run() {
        def whatIsThisObject = { getThisObject() }
        assert whatIsThisObject() == this
        def whatIsThis = { this }
        assert whatIsThis() == this
    }
}

class EnclosedInInnerClass {
    class Inner {
        Closure cl = { this }
    }

    void run() {
        def inner = new Inner()
        assert inner.cl() == inner
    }
}

class NestedClosures {
    void run() {
        def nestedClosures = {
            def cl = { this }
            cl()
        }
        assert nestedClosures() == this
    }
}
