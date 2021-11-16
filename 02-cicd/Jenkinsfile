pipeline {
    agent any
    stages {
        stage("Run test") {
            steps {
                sh 'pipenv sync'
                sh 'pipenv run python -m unittest discover -s tests -v'
            }
        }
        stage("StartDocker") {
            steps {
                sh 'sudo service docker start'
            }
        }
        stage("Build Docker image") {
            steps {
                sh 'docker build -t my_image .'
            }
        }
        stage("Deploy container") {
            steps {
                sh 'docker run -p 5000:5000 my_image'
                sh ''
            }
        }
    }
}


