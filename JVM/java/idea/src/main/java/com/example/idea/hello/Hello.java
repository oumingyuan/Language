package com.example.idea.hello;

import java.util.*;
import java.util.stream.Stream;

public class Hello {


    /**
     * Variable is already assigned to this value
     */
    private long myCachedLength = -1;
    private long myCachedTimeStamp = myCachedLength = -1;

    void trimStrings(List<Object> list) {

        list.stream().filter(String.class::isInstance).map(s -> ((String) s).trim());

    }


    /**
     * Condition 'i < value' is always 'true'
     *
     * @param value the value
     */
    void m(int value) {
        for (int i = 0; i < value; i++) {
            if (i < value) {
                System.out.println();
            }
        }
    }

    /**
     * Method reference result is always 'false'
     *
     * @param s S
     * @return HELLO
     */
    Stream<?> stream(Stream<?> s) {
        return s.filter(x -> x instanceof String).filter(Objects::isNull);
    }


    /**
     * Immutable object is modified
     *
     * @param a parameter a
     * @param b parameter b
     */
    void testImmutable(String a, String b) {
        Collections.singletonList(a).add(b);
    }

    public static void main(String[] args) throws ClassNotFoundException {

        Integer value1 = null;
        Integer value2 = 10;

        // Optional.ofNullable - 允许传递为 null 参数
        Optional<Integer> a = Optional.empty();

        // Optional.of - 如果传递的参数是 null，抛出异常 NullPointerException
        Optional<Integer> b = Optional.empty();


    }


}
