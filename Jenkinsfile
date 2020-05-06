pipeline {
    agent any
    stages {
        stage('Python Tests') {
            steps {
                sh '''
                    cd pythontest

                    # venv
                    source ~/work/build/venv/bin/activate

                    # pytest w/ coverage
                    source ./pypath && pytest --junitxml results.xml --cov-report xml:coverage.xml --cov ../python tests
                '''
            }
            post {
                always {
                    junit 'pythontest/results.xml'
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'pythontest/coverage.xml',
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 0,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
                }
            }
        }
    }
}
