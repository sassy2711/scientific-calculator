pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'sassy2341'
        DOCKER_IMAGE = "${DOCKERHUB_USER}/scientific-calculator:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests -p "test_*.py"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKERHUB_USER --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push $DOCKER_IMAGE"
            }
        }

        stage('Prepare Ansible in WSL2') {
                steps {
                    // *** CRITICAL: UPGRADE ANSIBLE ***
                    // We need to ensure Ansible itself is a newer version that correctly supports collections.
                    // The system-installed Ansible 2.9.6 is too old.
                    sh 'python3 -m pip install --upgrade ansible --user'
                    
                    // Add user bin to PATH for Ansible and other user-installed Python executables
                    sh 'export PATH="$HOME/.local/bin:$PATH"' 

                    // Install the community.docker collection within WSL2
                    // It will likely skip as it's installed, but this ensures it's there.
                    sh 'ansible-galaxy collection install community.docker'

                    // Install/ensure the Docker SDK for Python is installed within the same Python environment in WSL2
                    // It will likely skip as it's installed, but this ensures it's there.
                    sh 'python3 -m pip install docker --user' 

                    // OPTIONAL: Add a debug step to verify Ansible version
                    sh 'ansible --version'
                }
            }
        stage('Deploy via Ansible in WSL2') {
            steps {
                // Ensure ansible-playbook runs in the correct environment with PATH set
                sh '''
                    export PATH="$HOME/.local/bin:$PATH"
                    ansible-playbook deploy.yml
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
