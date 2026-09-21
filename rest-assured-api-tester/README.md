# Project 6: REST Assured API Tester CI/CD Demo

## Overview
This project demonstrates how to package an automated QA testing suite into a Docker container. The key learning objective is **Running an automated QA suite container against a deployed app**. Instead of deploying a long-running service, this pipeline builds a test runner image and executes it dynamically.

## Prerequisites
Ensure the following are installed and running on your Jenkins server:
- Docker
- Java 17 & Maven

## Step 1: Network Setup
Create a shared Docker network for your infrastructure and deployments:
`docker network create jenkins-net`

## Step 2: Infrastructure Setup
Run SonarQube and Jenkins on the `jenkins-net` network:
# Run SonarQube
`docker run -d --name sonarqube -p 9000:9000 --network jenkins-net sonarqube:lts-community`

# Run Jenkins (with Docker socket mounted)
`docker run -d --name jenkins -p 8080:8080 -p 50000:50000 --network jenkins-net -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts`

## Step 3: Jenkins Configuration
1. Log into Jenkins.
2. Install necessary plugins: Docker Pipeline, SonarQube Scanner, Pipeline.
3. Configure SonarQube Server in Manage Jenkins -> System.
4. Configure Global Tools (Maven, Sonar Scanner).

## Step 4: Pipeline Execution
1. Create a new Pipeline job in Jenkins.
2. Choose "Pipeline script from SCM" or paste the contents of Jenkinsfile.
3. Run the build. 
*Note: During the "Execute Automated QA Suite" stage, Jenkins spins up a temporary Docker container purely to run `mvn test` against a target API, and then destroys the container immediately afterward using the `--rm` flag.*

## Step 5: Verification
Review the Jenkins console output to confirm the REST Assured API tests executed successfully and passed.
