from json import JSONEncoder
from json import dumps
from request_objects import PaymentRequest, Receipt, Item


class ItemEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class ReceiptEncoder(JSONEncoder):
    def default(self, o):
        res = o.__dict__
        items = res["Items"]
        items_list = []
        for item in items:
            items_list.append(ItemEncoder().default(item))
        res["Items"] = items_list
        return res


class RequestEncoder:
    def __init__(self, payment_request: PaymentRequest):
        self.request = payment_request

    def to_json(self):
        body = self.request.__dict__
        if body["Receipt"] is None:
            return dumps(body)
        else:
            body["Receipt"] = ReceiptEncoder().default(body["Receipt"])
        return dumps(body)
