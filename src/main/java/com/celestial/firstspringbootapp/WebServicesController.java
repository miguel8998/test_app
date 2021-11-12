/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.celestial.firstspringbootapp;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 *
 * @author selvy
 */
@RestController
public class WebServicesController
{
    @GetMapping("api/rest")
    public  String  takeRest()
    {
        return "Rest is only necessary - Not the end goal";
    }
    
}
