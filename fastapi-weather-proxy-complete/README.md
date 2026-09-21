# Project 1: Python FastAPI Weather Proxy CI/CD Demo

## Overview
This project demonstrates a complete CI/CD pipeline using Jenkins, SonarQube, Docker, and Trivy for a Python FastAPI application.

## Prerequisites
Ensure the following are installed and running on your Jenkins server:
- Docker
- Trivy
- Python 3 & pip

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
1. Log into Jenkins at `http://localhost:8080`.
2. Install necessary plugins: Docker Pipeline, SonarQube Scanner, Pipeline.
3. Configure SonarQube Server:
   - Go to Manage Jenkins -> System.
   - Add a SonarQube server named SonarQube and point it to http://sonarqube:9000.
4. Configure Global Tools:
   - Go to Manage Jenkins -> Tools.
   - Add a SonarQube Scanner installation.

## Step 4: Pipeline Execution
1. Create a new Pipeline job in Jenkins.
2. Under the Pipeline section, choose "Pipeline script from SCM" (if hosted on Git) or paste the contents of Jenkinsfile.
3. Run the build. 

## Step 5: Verification
Once the pipeline finishes successfully, access the deployed FastAPI app:
- URL: http://localhost:8000
- Expected Output: {"Hello": "Weather Proxy"}
