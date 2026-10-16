// GitHub -> Jenkins -> Docker: rebuilds and restarts the career-students container on every push.
pipeline {
  agent any
  options { disableConcurrentBuilds(); timeout(time: 15, unit: 'MINUTES') }
  stages {
    stage('Checkout')    { steps { checkout scm } }
    stage('Build image') { steps { sh 'docker compose build --pull' } }
    stage('Deploy')      { steps { sh 'docker compose up -d --remove-orphans' } }
    stage('Health check') {
      steps {
        // the app has no public port, so check it from inside the nginx container on the same network
        sh 'sleep 3 && docker exec ggtech-nginx-live wget -q -O /dev/null http://career-students:5010/'
      }
    }
    stage('Clean up')    { steps { sh 'docker image prune -f' } }
  }
}
