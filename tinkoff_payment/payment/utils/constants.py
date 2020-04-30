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

