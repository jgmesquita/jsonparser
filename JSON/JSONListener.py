# Generated from JSON.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSON.JSONParser import JSONParser

# This class defines a complete listener for a parse tree produced by JSONParser.
class JSONListener(ParseTreeListener):

    # Enter a parse tree produced by JSONParser#json.
    def enterJson(self, ctx:JSONParser.JsonContext):
        pass

    # Exit a parse tree produced by JSONParser#json.
    def exitJson(self, ctx:JSONParser.JsonContext):
        pass


    # Enter a parse tree produced by JSONParser#field.
    def enterField(self, ctx:JSONParser.FieldContext):
        pass

    # Exit a parse tree produced by JSONParser#field.
    def exitField(self, ctx:JSONParser.FieldContext):
        pass


    # Enter a parse tree produced by JSONParser#String.
    def enterString(self, ctx:JSONParser.StringContext):
        pass

    # Exit a parse tree produced by JSONParser#String.
    def exitString(self, ctx:JSONParser.StringContext):
        pass


    # Enter a parse tree produced by JSONParser#Integer.
    def enterInteger(self, ctx:JSONParser.IntegerContext):
        pass

    # Exit a parse tree produced by JSONParser#Integer.
    def exitInteger(self, ctx:JSONParser.IntegerContext):
        pass


    # Enter a parse tree produced by JSONParser#Dictionary.
    def enterDictionary(self, ctx:JSONParser.DictionaryContext):
        pass

    # Exit a parse tree produced by JSONParser#Dictionary.
    def exitDictionary(self, ctx:JSONParser.DictionaryContext):
        pass


    # Enter a parse tree produced by JSONParser#List.
    def enterList(self, ctx:JSONParser.ListContext):
        pass

    # Exit a parse tree produced by JSONParser#List.
    def exitList(self, ctx:JSONParser.ListContext):
        pass


    # Enter a parse tree produced by JSONParser#TrueBoolean.
    def enterTrueBoolean(self, ctx:JSONParser.TrueBooleanContext):
        pass

    # Exit a parse tree produced by JSONParser#TrueBoolean.
    def exitTrueBoolean(self, ctx:JSONParser.TrueBooleanContext):
        pass


    # Enter a parse tree produced by JSONParser#FalseBoolean.
    def enterFalseBoolean(self, ctx:JSONParser.FalseBooleanContext):
        pass

    # Exit a parse tree produced by JSONParser#FalseBoolean.
    def exitFalseBoolean(self, ctx:JSONParser.FalseBooleanContext):
        pass


    # Enter a parse tree produced by JSONParser#NullValue.
    def enterNullValue(self, ctx:JSONParser.NullValueContext):
        pass

    # Exit a parse tree produced by JSONParser#NullValue.
    def exitNullValue(self, ctx:JSONParser.NullValueContext):
        pass


    # Enter a parse tree produced by JSONParser#Whitespace.
    def enterWhitespace(self, ctx:JSONParser.WhitespaceContext):
        pass

    # Exit a parse tree produced by JSONParser#Whitespace.
    def exitWhitespace(self, ctx:JSONParser.WhitespaceContext):
        pass



del JSONParser