from antlr4 import FileStream, CommonTokenStream
from .JSONLexer import JSONLexer
from .JSONParser import JSONParser
from .ASTBuilder import ASTBuilder
from .NodesJSON import *

class ObjectJSON:
    def __init__(self, path):
        source_file = path
        input_stream = FileStream(source_file, encoding="utf-8")
        lexer = JSONLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = JSONParser(token_stream)
        tree = parser.json()
        self.ast = ASTBuilder().visit(tree)
    
    def print(self):
        self.ast.print()

    def serialize(self, path):
        with open(path, 'w') as f:
            f.write(self.ast.to_json(indent=0))
            f.close()
    
    def get(self, name):
        for field in self.ast.fields:
            if field.getName() == name:
                return field.getValue()
    
    def set(self, name, value):
        t = type(value).__name__
        if t == "str":
            node = StringNode(value)
        if t == "int":
            node = IntegerNode(value)
        if t == "bool":
            node = BooleanNode(value)
        if t == "NoneType":
            node = NullNode()
        if t == "list":
            node = ListNode(value)
        flag = False
        for field in self.ast.fields:
            if field.getName() == name:
                flag = True
                field.setValue(node)
        if not flag:
            field = FieldNode(name, node)
            self.ast.fields.append(field)