from hashlib import sha256

from .exceptions import InvalidUseException
from django.conf import settings
from .constants import PaymentTypes


class PaymentRequest:
    def __init__(self, order_id: str, amount=None, redirect_due_date=None,
                 customer_ip=None, language=None, description=None,
                 notification_url=None, success_url=None,
                 fail_url=None, receipt=None, **data):
        """
        :param redirect_due_date: Lifetime of customer's payment url
        :param customer_ip:
        :param language: Language of payment form on Tinkoff's site
        :param notification_url: Url for notification about payments
        :param success_url:
        :param fail_url:
        :param receipt: Receipt object
        :param amount: Cost of goods in kopecks
        :param order_id: Customer ID in seller service
        :param description: Description of goods
        :param data: Extra data that will be returned to notification_url
        """
        if amount is not None: self.Amount = amount
        if description is not None: self.Description = description
        if customer_ip is not None: self.IP = customer_ip
        self.Receipt = receipt if receipt is not None else None
        self.Language = settings.TINKOFF_PAYMENT_DEFAULT_LANGUAGE if language is None else language
        self.RedirectDueDate = settings.TINKOFF_PAYMENT_DEFAULT_URL_LIFETIME if \
            redirect_due_date is None else redirect_due_date
        self.NotificationURL = settings.TINKOFF_PAYMENT_DEFAULT_NOTIFICATION_URL if \
            notification_url is None else notification_url
        self.SuccessURL = settings.TINKOFF_PAYMENT_SUCCESS_URL if success_url is None else success_url
        self.FailURL = settings.TINKOFF_PAYMENT_FAIL_URL if fail_url is None else fail_url
        self.TerminalKey = settings.TINKOFF_PAYMENT_TERMINAL_KEY
        self.OrderId = order_id
        self.DATA = data
        self.PayType = PaymentTypes.SINGLE_STAGE
        self.Token = self.generate_token()

    def generate_token(self):
        fields = self.__dict__.copy()
        del fields["DATA"]
        del fields["Receipt"]
        fields["Password"] = settings.TINKOFF_PAYMENT_PASSWORD
        values_str = ""
        for key in sorted(fields.keys()):
            values_str += str(fields[key])
        hash = sha256()
        hash.update(values_str.encode("utf-8"))
        return hash.hexdigest()


class Item:
    def __init__(self, name: str, price: str, amount: int, quantity: float,
                 tax: str, payment_method=None, payment_object=None):
        """
        Class for item of product that customer want to buy
        :param name: Name of unit of goods
        :param price: Cost of unit of goods
        :param amount: Cost of goods in kopecks
        :param quantity: Quantity or weight of goods
        :param tax: VAT rate
        :param payment_method:
        :param payment_object:
        """
        self.Name = name
        self.Amount = amount
        self.Price = price
        self.Quantity = quantity
        self.Tax = tax
        if payment_method is not None:
            self.PaymentMethod = payment_method
        if payment_object is not None:
            self.PaymentObject = payment_object


class Receipt:
    def __init__(self, taxation: str, items: list, email_company=None,
                 email=None, phone_number=None):
        """
        :param email: customer's email
        :param phone_number: customer's phone
        :param email_company: company's email
        :param taxation: tax system
        """
        if email is None and phone_number is None:
            raise InvalidUseException("Email and phone_number can't be None at the same time")
        if email is not None:
            self.Email = email
        else:
            self.Phone = phone_number
        self.Items = items
        self.EmailCompany = settings.TINKOFF_PAYMENT_COMPANY_EMAIL if email_company is None else email_company
        self.Taxation = taxation
