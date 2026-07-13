class ObjectNode:
    def __init__(self, fields):
        self.fields = fields
    
    def print(self):
        print(self.to_json())

    def to_json(self, indent=0):
        if not self.fields:
            return "{}"

        padding = " " * indent
        children = ",\n".join(field.to_json(indent + 2) for field in self.fields)
        return f"{{\n{children}\n{padding}}}"
    
class FieldNode():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value.getValue()
    
    def setValue(self, value):
        self.value = value

    def to_json(self, indent=0):
        padding = " " * indent
        return f'{padding}{quote_string(self.name)}: {self.value.to_json(indent)}'

class ListNode():
    def __init__(self, items):
        self.items = items
    
    def getValue(self):
        lst = []
        for item in self.items:
            lst.append(item.getValue())
        return lst

    def to_json(self, indent=0):
        if not self.items:
            return "[]"

        padding = " " * indent
        item_padding = " " * (indent + 2)
        children = ",\n".join(
            f"{item_padding}{item.to_json(indent + 2)}" for item in self.items
        )
        return f"[\n{children}\n{padding}]"

class StringNode():
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def to_json(self, indent=0):
        return quote_string(self.value)

class IntegerNode():
    def __init__(self, value):
        self.value = value
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def to_json(self, indent=0):
        return str(self.value)

class BooleanNode():
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def to_json(self, indent=0):
        return "true" if self.value else "false"

class NullNode:
    def __init__(self):
        pass

    def to_json(self, indent=0):
        return "null"

def quote_string(value):
    escapes = {
        '"': '\\"',
        "\\": "\\\\",
        "\b": "\\b",
        "\f": "\\f",
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
    }
    escaped = "".join(escapes.get(character, character) for character in value)
    return f'"{escaped}"'
