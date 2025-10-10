// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 git 'https://github.com/sassy2711/scientific-calculator.git'
//             }
//         }
//         stage('Run Tests') {
//             steps {
//                 sh 'python3 -m unittest discover app'
//             }
//         }
//         stage('Build Docker') {
//             steps {
//                 sh 'docker build -t username/scientific-calculator:latest .'
//             }
//         }
//         stage('Push Docker') {
//             steps {
//                 withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
//                     sh 'echo $DOCKER_PASS | docker login -u sassy2341 --password-stdin'
//                     sh 'docker push sassy2341/scientific-calculator:latest'
//                 }
//             }
//         }
//     }
// }

pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'sassy2341'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_USER/scientific-calculator:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKERHUB_USER/scientific-calculator:latest'
            }
        }

        stage('Deploy via Ansible') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
            // Optional: send email here
        }
        failure {
            echo 'Pipeline failed!'
            // Optional: send email here
        }
    }
}
