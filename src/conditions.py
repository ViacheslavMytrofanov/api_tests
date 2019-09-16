import abc
import jsonpath_rw
from assertpy import assert_that


class Condition:

    def __init__(self):
        pass

    @abc.abstractmethod
    def match(self, response):
        return


class StatusCodeCondition(Condition):

    def match(self, response):
        assert response.status_code == self._status_code

    def __init__(self, code):
        super().__init__()
        self._status_code = code

    def __repr__(self):
        return "status code is {}".format(self._status_code)


status_code = StatusCodeCondition


class BodyFieldCondition(Condition):

    def match(self, response):
        json = response.json()
        value = jsonpath_rw.parse(self._json_path).find(json)
        assert_that(value, self._matcher)

    def __init__(self, json_path, matcher):
        super().__init__()
        self._json_path = json_path
        self._matcher = matcher

    def __repr__(self):
        return "body field {} {}".format(self._json_path, self._matcher)


body = BodyFieldCondition
