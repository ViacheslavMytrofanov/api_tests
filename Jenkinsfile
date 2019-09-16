node {

    stage("Checkout repo"){
        git branch: 'master',
        url: 'https://github.com/ViacheslavMytrofanov/api_tests'
    }

    stage("Install deps") {
        sh 'pipenv install'
    }

    stage('Test') {
        sh 'pipenv run pytest tests -sv --alluredir=allure_results'
    }

    stage("Report") {
    script {
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure_results']]
            ])
            }
    }
}