FROM eclipse-temurin:17-jre-jammy
WORKDIR /app
COPY target/*-jar-with-dependencies.jar app.jar
CMD ["java", "-jar", "app.jar"]