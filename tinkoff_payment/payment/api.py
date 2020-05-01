import requests as re
from django.core.exceptions import ObjectDoesNotExist

from .models import Transaction, Balance
from .utils.request_objects import InitPaymentRequest
from .utils.response_objects import InitPaymentResponse, InitError
from .utils.encoder import RequestEncoder
from .utils.constants import TinkoffURLs, TransactionStatuses
from .utils.exceptions import APIHandlerException


class APIHandler:
    def __init__(self, init_payment_request_obj: InitPaymentRequest, user_id, custom=False):
        self.user_id = user_id
        self.request_obj = init_payment_request_obj
        self.custom = custom
        self.is_validation_checked = False
        self.has_error = False
        self.data = None

    def do_request(self):
        self.data = self.do_request_to_tinkoff(
            RequestEncoder(self.request_obj).to_json()
        )

    def has_no_error(self) -> bool:
        self.is_validation_checked = True
        self.has_error = not self.data.error_code == "0"
        if not self.has_error:
            if not self.custom:
                try:
                    balance = Balance.objects.get(user__id=self.user_id)
                except ObjectDoesNotExist:
                    raise APIHandlerException(f"For id {self.user_id} balance does not exist")
                transaction = Transaction(balance)
                transaction.direction = 1
                transaction.amount = self.request_obj.Amount
                transaction.status = TransactionStatuses.NEW
                transaction.save()
        return not self.has_error

    def get_errors(self) -> InitError:
        return InitError(
            self.data.error_code,
            self.data.message,
            self.data.details
        )

    def get_url(self) -> str:
        if not self.has_error and self.is_validation_checked:
            return self.data.payment_url

    def get_data(self) -> InitPaymentResponse:
        return self.data

    @staticmethod
    def do_request_to_tinkoff(json_body):
        request = re.post(TinkoffURLs.INIT_URL, data=json_body)
        if request.status_code == 200:
            return InitPaymentResponse(request.json())

