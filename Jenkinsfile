pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 test_app.py'
            }
        }

        stage('Create Artifact') {
            steps {
                echo 'Creating artifact...'
                sh '''
                    mkdir -p build
                    cp app.py build/
                '''
                archiveArtifacts artifacts: 'build/app.py'
            }
        }
    }
}
