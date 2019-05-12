package com.example.idea.hello;


public class Java8Tester {

    public static void main(String args[]) {
        var x = 1;
        Integer sum = sum(x);
        System.out.println(sum);
    }

    private static Integer sum(Integer a) {
        return a + (Integer) 2;
    }

}
