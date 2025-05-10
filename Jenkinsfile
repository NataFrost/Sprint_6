pipeline {
    agent any

    stages {
        stage('Clean workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone repo') {
            steps {
                git branch: 'develop', url: 'https://github.com/NataFrost/Sprint_6.git'
            }
        }

        stage('Set up & test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest -v
                '''
            }
        }

        stage('Show commit') {
            steps {
                sh 'git log -1 --oneline'
            }
        }
    }
}