

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        print(value.__str__())
        return value.__str__()