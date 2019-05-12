package com.example.cat.different;


import static groovy.util.GroovyTestCase.assertEquals;

public class Hello1 {

    int method(String arg) {

        return 1;

    }

    int method(Object arg) {
        return 2;
    }

    public static void main(String[] args) {

        Object o = "Object";

        int result = new Hello1().method(o);
        assertEquals(2, result);

    }

}
