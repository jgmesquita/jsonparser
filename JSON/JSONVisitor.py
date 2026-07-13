# Generated from JSON.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSON.JSONParser import JSONParser

# This class defines a complete generic visitor for a parse tree produced by JSONParser.

class JSONVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSONParser#json.
    def visitJson(self, ctx:JSONParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#field.
    def visitField(self, ctx:JSONParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#String.
    def visitString(self, ctx:JSONParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#Integer.
    def visitInteger(self, ctx:JSONParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#Dictionary.
    def visitDictionary(self, ctx:JSONParser.DictionaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#List.
    def visitList(self, ctx:JSONParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#TrueBoolean.
    def visitTrueBoolean(self, ctx:JSONParser.TrueBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#FalseBoolean.
    def visitFalseBoolean(self, ctx:JSONParser.FalseBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#NullValue.
    def visitNullValue(self, ctx:JSONParser.NullValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#Whitespace.
    def visitWhitespace(self, ctx:JSONParser.WhitespaceContext):
        return self.visitChildren(ctx)



del JSONParser