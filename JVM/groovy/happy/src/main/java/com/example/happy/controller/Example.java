package com.example.happy.controller;

import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;

@RestController
@EnableAutoConfiguration
public class Example {


    @RequestMapping("/")
    String home() {
        return "Hello World!";
    }


}
