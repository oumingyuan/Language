package com.example.idea.mynull;

import org.apache.commons.lang3.StringUtils;
//import org.jetbrains.annotations.NotNull;


public class Str {

    public static void main(String[] args) {

//        @NotNull
        var a = 1;

//        @NotNull
        String b = null;

        System.out.println(StringUtils.equals(null, null));

        System.out.println(StringUtils.equals("1", "2"));

        System.out.println(StringUtils.equals("1", "1"));


    }

}
