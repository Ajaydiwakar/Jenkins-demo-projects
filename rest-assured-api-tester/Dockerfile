# Use a Maven image so we can run tests inside the container
FROM maven:3.9.4-eclipse-temurin-17

WORKDIR /app

# Copy pom.xml and download dependencies (caching layer)
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy the actual test source code
COPY src ./src

# The command runs the tests when the container starts
CMD ["mvn", "test"]
