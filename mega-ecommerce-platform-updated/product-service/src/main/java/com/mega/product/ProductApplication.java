package com.mega.product;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@SpringBootApplication
@RestController
public class ProductApplication {
    public static void main(String[] args) { SpringApplication.run(ProductApplication.class, args); }
    @GetMapping("/api/products")
    public List<String> getProducts() { return List.of("Laptop", "Smartphone", "Headphones"); }
}