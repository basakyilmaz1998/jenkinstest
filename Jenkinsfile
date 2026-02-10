pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-venv python3-pip

                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt

                    playwright install-deps
                    playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    set -e
                    . venv/bin/activate

                    chmod +x test.sh

                    echo "=== UI testleri başlıyor ==="
                    ./test.sh

                    echo "=== test_reports içeriği ==="
                    ls -la test_reports
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test_reports/**/*', allowEmptyArchive: true
            junit allowEmptyResults: true, testResults: 'test_reports/report.xml'
        }
    }
}
