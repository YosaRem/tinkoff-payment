import requests as re

from .utils.request_objects import InitPaymentRequest
from .utils.response_objects import InitPaymentResponse
from .utils.encoder import RequestEncoder
from .utils.constants import TinkoffURLs


class APIHandler:
    @staticmethod
    def do_request_to_tinkoff(json_body):
        request = re.post(TinkoffURLs.INIT_URL, data=json_body)
        if request.status_code == 200:
            return InitPaymentResponse(request.json())






