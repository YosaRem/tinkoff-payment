TRANSACTION_STATUSES_CHOICES = [
    ["NEW", "Создан"],
    ["FORMSHOWED", "Платёжная форма была открыта пользователем"],
    ["DEADLINE_EXPIRED", "Просрочен"],
    ["CANCELED", "Отменён"],
    ["PREAUTHORIZING", "Проверка платёжных данных"],
    ["AUTHORIZING", "Резервируется"],
    ["AUTHORIZED", "Зарезервирован"],
    ["AUTH_FAIL", "Не прошел авторизацию"],
    ["REJECTED", "Отклонен"],
    ["3DS_CHECKING", "Проверяется по протоколу 3-D Secure"],
    ["3DS_CHECKED", "Проверен по протоколу 3-D Secure"],
    ["REVERSING", "Резервирование отменяется"],
    ["REVERSED", "Резервирование отменено"],
    ["CONFIRMING", "Подтверждается"],
    ["CONFIRMED", "Подтвержден"],
    ["REFUNDING", "Возвращается"],
    ["PARTIAL_REFUNDED", "Возвращен частично"],
    ["REFUNDED", "Возвращен полностью"],
]


class TransactionStatues:
    NEW = "NEW"
    FORMSHOWED = "FORMSHOWED"
    DEADLINE_EXPIRED = "DEADLINE_EXPIRED"
    CANCELED = "CANCELED"
    PREAUTHORIZING = "PREAUTHORIZING"
    AUTHORIZING = "AUTHORIZING"
    AUTHORIZED = "AUTHORIZED"
    AUTH_FAIL = "AUTH_FAIL"
    REJECTED = "REJECTED"
    THREE_DS_CHECKING = "3DS_CHECKING"
    THREE_DS_CHECKED = "3DS_CHECKED"
    REVERSING = "REVERSING"
    REVERSED = "REVERSED"
    CONFIRMING = "CONFIRMING"
    CONFIRMED = "CONFIRMED"
    REFUNDING = "REFUNDING"
    PARTIAL_REFUNDED = "PARTIAL_REFUNDED"
    REFUNDED = "REFUNDED"


class VATRates:
    WITHOUT_VAT = "none"
    VAT_0 = "vat0"
    VAT_10 = "vat10"
    VAT_20 = "vat20"
    VAT_110 = "vat110"
    VAT_120 = "vat120"


class PaymentMethods:
    FULL_PAYMENT = "full_payment"
    FULL_PREPAYMENT = "full_prepayment"
    PREPAYMENT = "prepayment"
    ADVANCE = "advance"
    PARTIAL_PAYMENT = "partial_payment"
    CREDIT = "credit"
    CREDIT_PAYMENT = "credit_payment"


class PaymentObjects:
    COMMODITY = "commodity"
    EXCISE = "excise"
    JOB = "job"
    SERVICE = "service"
    GAMBLING_BET = "gambling_bet"
    GAMBLING_PRIZE = "gambling_prize"
    LOTTERY = "lottery"
    LOTTERY_PRIZE = "lottery_prize"
    INTELLECTUAL_ACTIVITY = "intellectual_activity"
    PAYMENT = "payment"
    COMPOSITE = "composite"
    ANOTHER = "another"


class TaxSystems:
    OSN = "osn"
    USN_INCOME = "usn_income"
    USN_INCOME_OUTCOME = "usn_income_outcome"
    PATENT = "patent"
    ENVD = "envd"
    ESN = "esn"


class PaymentTypes:
    SINGLE_STAGE = "O"
    TWO_STAGE = "T"


class PaymentSystemLanguage:
    RUSSIAN = "ru"
    ENGLISH = "en"


class TinkoffURLs:
    INIT_URL = "https://securepay.tinkoff.ru/v2/Init"



