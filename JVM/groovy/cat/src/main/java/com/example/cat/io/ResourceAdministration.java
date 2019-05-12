package com.example.cat.io;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ResourceAdministration {

    public static void main(String[] args) {

        Path file = Paths.get("E:\\Language\\JVM\\groovy\\cat\\src\\main\\java\\com\\example\\cat\\io\\a.txt");

        Charset charset = Charset.forName("UTF-8");

        try (BufferedReader reader = Files.newBufferedReader(file, charset)) {

            String line;
            while ((line = reader.readLine()) != null) {

                System.out.println(line);

            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }


}
