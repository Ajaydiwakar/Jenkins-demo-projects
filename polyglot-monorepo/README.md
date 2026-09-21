# Project 10: Polyglot Monorepo CI/CD Demo

## Overview
This project demonstrates how to structure and deploy a **Monorepo** containing multiple applications written in different languages. The key learning objective is **Pipeline routing: building a Java backend and Python frontend in one Jenkinsfile**.

We will build two separate Docker images (`polyglot-backend` and `polyglot-frontend`) and deploy them to the shared `jenkins-net` network, where the frontend will communicate with the backend via internal DNS resolution.

## Prerequisites
Ensure the following are installed and running on your Jenkins server:
- Docker & Trivy
- Python 3 & pip
- Java 17 & Maven

## Step 1: Network Setup
Create a shared Docker network for your infrastructure and deployments:
`docker network create jenkins-net`

## Step 2: Infrastructure Setup
Run SonarQube and Jenkins on the `jenkins-net` network:
# Run SonarQube
`docker run -d --name sonarqube -p 9000:9000 --network jenkins-net sonarqube:lts-community`

# Run Jenkins 
`docker run -d --name jenkins -p 8081:8080 -p 50000:50000 --network jenkins-net -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts`
*(Map Jenkins to 8081 if 8080 is used by the backend app).*

## Step 3: Jenkins Configuration
1. Log into Jenkins.
2. Install necessary plugins: Docker Pipeline, SonarQube Scanner, Pipeline.
3. Configure SonarQube Server in Manage Jenkins -> System.
4. Configure Global Tools (Maven, JDK, Sonar Scanner).

## Step 4: Pipeline Execution
1. Create a new Pipeline job in Jenkins.
2. Choose "Pipeline script from SCM" or paste the contents of Jenkinsfile.
3. Run the build. Observe how Jenkins navigates into the `backend/` and `frontend/` directories using the `dir()` step to execute language-specific builds!

## Step 5: Verification
Access the deployed Frontend Application, which will securely query the Java Backend:
- URL: `http://localhost:5000`
- Expected Output: `{"backend_response":{"message":"Hello from the Java Spring Boot Backend!"},"frontend_status":"Active"}`
