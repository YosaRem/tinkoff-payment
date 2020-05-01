from hashlib import sha256


def generate_token(data: dict):
    values_str = ""
    for key in sorted(data.keys()):
        values_str += str(data[key])
    payment_hash = sha256()
    payment_hash.update(values_str.encode("utf-8"))
    return payment_hash.hexdigest()


def check_notification_token(tinkoff_data: dict):
    token = tinkoff_data.get("Token")
    data = tinkoff_data.copy()
    if "DATA" in data: del data["DATA"]
    if "Receipt" in data: del data["Receipt"]
    if "Token" in data: del data["Token"]
    return token == generate_token(data)


