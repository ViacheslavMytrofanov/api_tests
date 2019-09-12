import logging
import allure


class AssertableResponse(object):

    def __init__(self, response):
        logging.info("Request url={} body={}".format(response.request.url, response.request.body))
        logging.info("Response status={} body={}".format(response.status_code, response.text))
        self._response = response

    # @allure.step('status code should be "{code}"')
    # def status_code(self, code):
    #     logging.info("Assert: status code should be {}".format(code))
    #     return self._response.status_code == code
    #
    # @allure.step
    # def field(self, name):
    #     return self._response.json()[name]

    @allure.step("response should have {condition}")
    def should_have(self, condition):
        logging.info("About checking " + str(condition))
        condition.match(self. _response)
        return self