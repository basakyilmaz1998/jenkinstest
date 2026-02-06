pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-venv python3-pip
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
    steps {
        sh '''
            . venv/bin/activate
            playwright install
            mkdir -p test_reports
            bash test.sh
        '''
    }
}
    }
}
