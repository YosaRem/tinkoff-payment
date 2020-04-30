from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

