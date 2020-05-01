

class InitPaymentResponse:
    def __init__(self, data: dict):
        self.terminal_key = data["TerminalKey"]
        self.amount = data.get("Amount")
        self.order_id = data.get("OrderId")
        self.success = data.get("Success")
        self.status = data.get("Status")
        self.payment_id = data.get("PaymentId")
        self.error_code = data.get("ErrorCode")
        if self.error_code == "0":
            self.payment_url = data.get("PaymentURL")
        else:
            self.message = data.get("Message")
            self.details = data.get("Details")


class InitError:
    def __init__(self, code, message, details):
        self.code = code
        self.message = message
        self.details = details
