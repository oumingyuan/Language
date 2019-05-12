package com.example.cat.lambda;

import java.util.ArrayList;
import java.util.List;

public class Hello {


    public static void main(String[] args) {

//        Runnable run = () -> System.out.println("run");

        List<Integer> list = new ArrayList<>();

        list.add(1);
        list.add(2);

        list.forEach(System.out::println);

    }

}
