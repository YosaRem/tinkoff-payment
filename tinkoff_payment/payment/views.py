from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.http import HttpResponse

from .models import Transaction
from .utils.token_handler import check_notification_token


class NotificationHandler:
    class DefaultHandler(View):
        def post(self, request, *args, **kwargs):
            data = request.POST
            if check_notification_token(data):
                try:
                    transaction = Transaction.objects.get(data.get("OrderId"))
                except ObjectDoesNotExist:
                    return
                transaction.status = data["Status"]
                transaction.save()
                return HttpResponse("OK", status_code=200)

    class CustomHandler(View):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.func = None

        def add_handler(self, func):
            self.func = func

        def post(self, request, *args, **kwargs):
            data = request.POST
            if check_notification_token(data):
                if self.func is not None:
                    self.func(request)
                    return HttpResponse("OK", status_code=200)
