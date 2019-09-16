import logging
import allure


class AssertableResponse:

    def __init__(self, response):
        logging.info("Request url={} body={}".format(response.request.url, response.request.body))
        logging.info("Response status={} body={}".format(response.status_code, response.text))
        self._response = response

    @allure.step("response should have {condition}")
    def should_have(self, condition):
        logging.info("About checking " + str(condition))
        condition.match(self. _response)
        return self