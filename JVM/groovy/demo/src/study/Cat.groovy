package study

class Cat {

    static void main(String[] args) {

        for (int i = 0; i < 10; i++) {
            println(i)
        }

    }


}

class Example {
    static void main(String[] args) {
        int[] array = [0, 1, 2, 3]

        for (int i in array) {
            println(i)
        }
    }
}

class Example1 {
    static void main(String[] args) {

        for (int i in 1..5) {
            println(i)
        }

    }
}


class Example2 {
    static void main(String[] args) {
        def employee = ["Ken": 21, "John": 25, "Sally": 22]

        for (emp in employee) {
            println(emp)
        }
    }
}

class Example3 {
    static def DisplayName() {
        println("This is how methods work in groovy")
        println("This is an example of a simple method")
    }

    static void main(String[] args) {
        DisplayName()
    }
}