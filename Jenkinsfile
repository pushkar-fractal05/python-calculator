pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat 'python --version'
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v --junitxml=test-results.xml'
            }

            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results.xml'
                }
            }
        }

        stage('Build') {
            steps {
                bat 

                archiveArtifacts artifacts: 'dist/calculator.zip', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    if not exist C:\\calculator-deployment mkdir C:\\calculator-deployment
                    copy /Y dist\\calculator.zip C:\\calculator-deployment\\calculator.zip
                '''
            }
        }
    }
}