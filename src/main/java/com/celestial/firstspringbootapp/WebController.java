/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.celestial.firstspringbootapp;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 *
 * @author selvy
 */
@Controller
@RequestMapping("/api/")
public class WebController
{
    @RequestMapping("hello")
    public  String  helloHandler(Model theModel)
    {
        System.out.println("Hello from Spring Controller...");
        theModel.addAttribute("message", "Welcome to my world from SpringBoot in Netbeans");
        return "hello";
    }
    
}
