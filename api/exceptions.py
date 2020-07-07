from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST


class BadRequestException(APIException):
    status_code = HTTP_400_BAD_REQUEST
    default_code = 'Bad Request'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code:
            self.status_code = status_code