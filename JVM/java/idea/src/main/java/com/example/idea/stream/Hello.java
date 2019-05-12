package com.example.idea.stream;





import java.util.*;
import java.util.stream.Collectors;


class Hello {


    /**
     * to remove the blank element in the string list
     *
     * @param stringList the string list before
     * @return the return list
     */
    static List<String> removeBlank(List<String> stringList) {


//        List<String> stringList = List.of("abc", "", "bc", "efg", "hello", "", "jkl");


        return stringList.stream().filter(str -> !str.isEmpty()).collect(Collectors.toList());


    }

    static List<String> removeNull1( List<String> stringList) {


        var listNull = new ArrayList<String>();
        listNull.add(null);

        stringList.removeAll(listNull);

        return stringList;
    }

    static List<String> removeNull2( List<String> stringList) {


        return stringList.stream().filter(Objects::nonNull).collect(Collectors.toList());
    }


    public void for_each() {
        Random random = new Random();
        random.ints().limit(10).forEach(System.out::println);
    }


    public void my_map() {

        List<Integer> numbers = Arrays.asList(3, 2, 2, 3, 7, 3, 5);
        // 获取对应的平方数
        List<Integer> squaresList = numbers.stream().map(i -> i * i).distinct().collect(Collectors.toList());

        System.out.println(squaresList);

    }


    public void null_filter() {
        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd", "", "jkl");
        // 获取空字符串的数量
        int count = (int) strings.stream().filter(String::isEmpty).count();

        System.out.println(count);
    }



    public void limit_char() {
        Random random = new Random();
        random.ints().limit(10).forEach(System.out::println);
    }

}
