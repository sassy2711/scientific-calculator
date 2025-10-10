pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<your-username>/scientific-calculator.git'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover app/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t <your-dockerhub-username>/scientific-calculator .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u <your-dockerhub-username> --password-stdin'
                    sh 'docker push <your-dockerhub-username>/scientific-calculator'
                }
            }
        }
    }
}
