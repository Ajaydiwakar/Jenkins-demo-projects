# Use a lightweight JRE base image
FROM eclipse-temurin:17-jre-jammy

# Set the working directory
WORKDIR /app

# Copy the built fat-JAR into the image
# (Assuming Jenkins ran `mvn clean install` prior to docker build)
COPY target/inventory-api-1.0.0.jar app.jar

# Expose the application port
EXPOSE 8080

# Run the Java application
CMD ["java", "-jar", "app.jar"]
