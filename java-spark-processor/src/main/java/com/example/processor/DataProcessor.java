package com.example.processor;

import org.apache.commons.lang3.StringUtils;

public class DataProcessor {
    public static void main(String[] args) {
        System.out.println("Starting Data Processor...");
        String data = "  devops  pipeline  data  ";
        System.out.println("Raw Data: '" + data + "'");
        System.out.println("Cleaned Data: '" + StringUtils.trimToEmpty(data) + "'");
        System.out.println("Data Processor finished successfully.");
        
        // Keep container running for demo purposes
        try {
            Thread.sleep(600000); // Sleep for 10 minutes
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}