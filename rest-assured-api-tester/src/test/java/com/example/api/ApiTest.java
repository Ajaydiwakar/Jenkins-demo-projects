package com.example.api;

import io.restassured.RestAssured;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class ApiTest {

    @BeforeAll
    public static void setup() {
        // Retrieve target URL from system properties, defaulting to a public mock API
        // In a real pipeline, this would point to http://my-app-container:8080
        String baseUri = System.getProperty("baseUri", "https://jsonplaceholder.typicode.com");
        RestAssured.baseURI = baseUri;
        System.out.println("Running tests against: " + RestAssured.baseURI);
    }

    @Test
    public void testGetPost() {
        given()
            .when().get("/posts/1")
            .then()
            .statusCode(200)
            .body("id", equalTo(1));
    }
}
