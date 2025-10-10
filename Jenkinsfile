// // pipeline {
// //     agent any

// //     stages {
// //         stage('Checkout') {
// //             steps {
// //                 git 'https://github.com/sassy2711/scientific-calculator.git'
// //             }
// //         }
// //         stage('Run Tests') {
// //             steps {
// //                 sh 'python3 -m unittest discover app'
// //             }
// //         }
// //         stage('Build Docker') {
// //             steps {
// //                 sh 'docker build -t username/scientific-calculator:latest .'
// //             }
// //         }
// //         stage('Push Docker') {
// //             steps {
// //                 withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
// //                     sh 'echo $DOCKER_PASS | docker login -u sassy2341 --password-stdin'
// //                     sh 'docker push sassy2341/scientific-calculator:latest'
// //                 }
// //             }
// //         }
// //     }
// // }

// pipeline {
//     agent any

//     environment {
//         DOCKERHUB_USER = 'sassy2341'
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Test') {
//             steps {
//                 sh 'python3 -m unittest discover'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t $DOCKERHUB_USER/scientific-calculator:latest .'
//             }
//         }

//         stage('Login to Docker Hub') {
//             steps {
//                 withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
//                     sh 'echo $DOCKER_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
//                 }
//             }
//         }

//         stage('Push Docker Image') {
//             steps {
//                 sh 'docker push $DOCKERHUB_USER/scientific-calculator:latest'
//             }
//         }

//         stage('Deploy via Ansible') {
//             steps {
//                 sh 'ansible-playbook deploy.yml'
//             }
//         }
//     }

//     post {
//         success {
//             echo 'Pipeline succeeded!'
//             // Optional: send email here
//         }
//         failure {
//             echo 'Pipeline failed!'
//             // Optional: send email here
//         }
//     }
// }


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
                // Explicitly run these commands within WSL2.
                // You might need to adjust 'wsl.exe -e bash -c' depending on your Jenkins's shell configuration.
                // For 'sh' step on Windows, it often finds 'bash' if Git Bash or WSL is in PATH.
                // Let's assume 'sh' resolves to a WSL bash shell.

                // Install Ansible if not already available in the default WSL python env
                sh 'python3 -m pip install ansible --user' // Install for the current user in WSL
                
                // Ensure ansible-galaxy is in path
                sh 'export PATH="$HOME/.local/bin:$PATH"' // Add user bin to PATH for Ansible

                // Install the community.docker collection within WSL2
                sh 'ansible-galaxy collection install community.docker'

                // Install the Docker SDK for Python within the same Python environment in WSL2
                sh 'python3 -m pip install docker --user' // Install for the current user in WSL
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
