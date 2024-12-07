pipeline {
    agent any

    environment {
        VIRTUAL_ENV = '.venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Checkout code from Git
                git branch: 'main', url: 'https://github.com/ziqing-wan99/myjenkins.git'
            }
        }

        stage('Setup Environment') {
            steps {
                // Set up Python environment and install dependencies
                sh '''
                python3 --version
                python3 -m venv $VIRTUAL_ENV
                source $VIRTUAL_ENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                // Run Pytest with Selenium tests
                sh '''
                source $VIRTUAL_ENV/bin/activate
                pytest --html=report.html --self-contained-html
                '''
            }
        }

        stage('Archive Results') {
            steps {
                // Archive test reports in Jenkins
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            // Clean up virtual environment
            sh 'rm -rf $VIRTUAL_ENV'
        }
        success {
            echo 'Tests ran successfully!'
        }
        failure {
            echo 'Tests failed. Check the logs.'
        }
    }
}
