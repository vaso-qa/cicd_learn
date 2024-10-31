pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // Клонируем репозиторий
                git url: 'https://github.com/vaso-qa/cicd_learn' // Замените на свой URL репозитория
            }
        }
        stage('Build') {
            steps {
                script {
                    // Собираем Docker-образ
                    sh 'docker-compose build'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Запускаем контейнеры
                    sh 'docker-compose up -d'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Запускаем тесты внутри контейнера
                    sh 'docker-compose exec web pytest test_app.py' // Замените 'web' на имя вашего сервиса
                }
            }
        }
        stage('Stop') {
            steps {
                script {
                    // Останавливаем контейнеры
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            // Останавливаем контейнеры, даже если были ошибки
            script {
                sh 'docker-compose down'
            }
        }
    }
}
