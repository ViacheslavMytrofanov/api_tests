node {

    stage("Checkout repo"){
        git branch: 'master',
        credentialsId: '9085ac67-9308-4190-b604-32a2c814837a',
        url: 'https://github.com/ViacheslavMytrofanov/api_tests'
    }

    stage("Install deps") {
        sh 'pipenv install'
    }

    stage('Test') {
        sh 'pipenv run pytest tests -sv --alluredir=allure_results'
    }
}