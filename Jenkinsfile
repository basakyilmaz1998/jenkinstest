pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh """
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . venv/bin/activate
                    pytest -v
                """
            }
        }
    }
}
