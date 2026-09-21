package com.example.inventory;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;

@RestController
public class InventoryController {
    
    @GetMapping("/inventory")
    public Map<String, Object> getInventory() {
        return Map.of(
            "item", "Laptop",
            "quantity", 50,
            "status", "In Stock"
        );
    }
}
