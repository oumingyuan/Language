package com.example.idea.try_with;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;

public class Try {


    static String readData7(String message) throws IOException {


        Reader inputString = new StringReader(message);

        try (BufferedReader br = new BufferedReader(inputString)) {
            return br.readLine();
        }


    }

    static String readData9(String message) throws IOException {

        Reader inputString = new StringReader(message);

        BufferedReader br = new BufferedReader(inputString);

        try (br) {
            return br.readLine();
        }


    }

}
