pipeline {
    agent any

    environment {
        APP_NAME = "ai-symptom-checker"
    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins will automatically checkout the code if linked to the repo
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                sh 'pip install --break-system-packages -r requirements.txt'
                sh 'python3 data/generate_dataset.py'
                sh 'python3 ml_model/train.py'
                sh 'python3 -m pytest tests/'
            }
        }

        stage('Build Image') {
            steps {
                echo 'Building Docker Image...'
                // Build the image locally on the host Docker engine
                sh "docker build -t ${APP_NAME}:latest ."
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Local Kubernetes Cluster...'
                // Deploy using the local-deploy manifest
                sh 'kubectl apply -f k8s/local-deploy.yaml'
            }
        }

        stage('Verify') {
            steps {
                echo 'Deployment complete. Verifying status...'
                sh 'kubectl get pods'
                sh 'kubectl get svc'
                echo "Access the app at http://localhost:30000"
            }
        }
    }
}
