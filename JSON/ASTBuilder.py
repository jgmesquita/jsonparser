from .JSONVisitor import JSONVisitor
from .NodesJSON import (
    BooleanNode,
    FieldNode,
    IntegerNode,
    ListNode,
    NullNode,
    ObjectNode,
    StringNode
)

class ASTBuilder(JSONVisitor):
    def visitJson(self, ctx):
        fields = []
        for field_ctx in ctx.field():
            fields.append(self.visit(field_ctx))
        return ObjectNode(fields)
    
    
    def visitField(self, ctx):
        name = ctx.STRING().getText()
        name = name[1:-1]  

        value = self.visit(ctx.value())

        return FieldNode(name, value)

    def visitString(self, ctx):
        text = ctx.STRING().getText()
        value = text[1:-1] 

        return StringNode(value)

    def visitInteger(self, ctx):
        value = int(ctx.INTEGER().getText())

        return IntegerNode(value)

    def visitDictionary(self, ctx):
        fields = []

        for field_ctx in ctx.field():
            fields.append(self.visit(field_ctx))

        return ObjectNode(fields)

    def visitList(self, ctx):
        items = []

        for value_ctx in ctx.value():
            items.append(self.visit(value_ctx))

        return ListNode(items)

    def visitTrueBoolean(self, ctx):
        return BooleanNode(True)

    def visitFalseBoolean(self, ctx):
        return BooleanNode(False)

    def visitNullValue(self, ctx):
        return NullNode()
