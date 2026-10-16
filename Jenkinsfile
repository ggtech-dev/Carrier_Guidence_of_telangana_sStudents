// GitHub → Jenkins → Docker deploy on port 5010 (same style as your existing pipelines)
pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build image') { steps { sh 'docker compose build' } }
    stage('Deploy') { steps { sh 'docker compose up -d --remove-orphans' } }
    stage('Health check') { steps { sh 'sleep 3 && curl -fsS http://localhost:5010/ > /dev/null' } }
  }
}
