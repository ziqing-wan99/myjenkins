pipeline { // Starts the Jenkins pipeline script.
    agent any // Specifies that the pipeline can run on any available Jenkins agent.

    environment {
        VIRTUAL_ENV = '.venv' // Sets the virtual environment directory name to .venv
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
                pytest --alluredir=allure-results
                '''
            }
        }

        stage('Archive Results') {
            steps {
                // Archive test reports in Jenkins
                archiveArtifacts artifacts: 'report.html', fingerprint: true
                archiveArtifacts artifacts: 'allure-results/**/*', fingerprint: true
            }
        }
        stage('Generate Allure Report') {
            steps {
                // Use the Allure plugin to generate and publish the report
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
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
