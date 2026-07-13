# Generated from JSON.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,56,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,5,0,11,8,0,10,
        0,12,0,14,9,0,3,0,16,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,3,2,35,8,2,1,2,1,2,1,2,1,2,1,
        2,5,2,42,8,2,10,2,12,2,45,9,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,3,2,
        54,8,2,1,2,0,0,3,0,2,4,0,0,65,0,6,1,0,0,0,2,19,1,0,0,0,4,53,1,0,
        0,0,6,15,5,1,0,0,7,12,3,2,1,0,8,9,5,2,0,0,9,11,3,2,1,0,10,8,1,0,
        0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,16,1,0,0,0,14,12,
        1,0,0,0,15,7,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,3,0,0,18,
        1,1,0,0,0,19,20,5,12,0,0,20,21,5,4,0,0,21,22,3,4,2,0,22,3,1,0,0,
        0,23,54,5,12,0,0,24,54,5,10,0,0,25,34,5,1,0,0,26,31,3,2,1,0,27,28,
        5,2,0,0,28,30,3,2,1,0,29,27,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,
        31,32,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,34,26,1,0,0,0,34,35,1,
        0,0,0,35,36,1,0,0,0,36,54,5,3,0,0,37,46,5,5,0,0,38,43,3,4,2,0,39,
        40,5,2,0,0,40,42,3,4,2,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,
        0,43,44,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,46,38,1,0,0,0,46,47,
        1,0,0,0,47,48,1,0,0,0,48,54,5,6,0,0,49,54,5,7,0,0,50,54,5,8,0,0,
        51,54,5,9,0,0,52,54,5,13,0,0,53,23,1,0,0,0,53,24,1,0,0,0,53,25,1,
        0,0,0,53,37,1,0,0,0,53,49,1,0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,
        52,1,0,0,0,54,5,1,0,0,0,7,12,15,31,34,43,46,53
    ]

class JSONParser ( Parser ):

    grammarFileName = "JSON.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TRUE", "FALSE", 
                      "NULL", "INTEGER", "TEXT", "STRING", "WS" ]

    RULE_json = 0
    RULE_field = 1
    RULE_value = 2

    ruleNames =  [ "json", "field", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    TRUE=7
    FALSE=8
    NULL=9
    INTEGER=10
    TEXT=11
    STRING=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.FieldContext)
            else:
                return self.getTypedRuleContext(JSONParser.FieldContext,i)


        def getRuleIndex(self):
            return JSONParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = JSONParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(JSONParser.T__0)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 7
                self.field()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 8
                    self.match(JSONParser.T__1)
                    self.state = 9
                    self.field()
                    self.state = 14
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 17
            self.match(JSONParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = JSONParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(JSONParser.STRING)
            self.state = 20
            self.match(JSONParser.T__3)
            self.state = 21
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(JSONParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class DictionaryContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.FieldContext)
            else:
                return self.getTypedRuleContext(JSONParser.FieldContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary" ):
                listener.enterDictionary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary" ):
                listener.exitDictionary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionary" ):
                return visitor.visitDictionary(self)
            else:
                return visitor.visitChildren(self)


    class NullValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(JSONParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullValue" ):
                listener.enterNullValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullValue" ):
                listener.exitNullValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullValue" ):
                return visitor.visitNullValue(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)


    class TrueBooleanContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(JSONParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueBoolean" ):
                listener.enterTrueBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueBoolean" ):
                listener.exitTrueBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueBoolean" ):
                return visitor.visitTrueBoolean(self)
            else:
                return visitor.visitChildren(self)


    class FalseBooleanContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(JSONParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseBoolean" ):
                listener.enterFalseBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseBoolean" ):
                listener.exitFalseBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseBoolean" ):
                return visitor.visitFalseBoolean(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class WhitespaceContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WS(self):
            return self.getToken(JSONParser.WS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhitespace" ):
                listener.enterWhitespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhitespace" ):
                listener.exitWhitespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhitespace" ):
                return visitor.visitWhitespace(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = JSONParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(JSONParser.STRING)
                pass
            elif token in [10]:
                localctx = JSONParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(JSONParser.INTEGER)
                pass
            elif token in [1]:
                localctx = JSONParser.DictionaryContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(JSONParser.T__0)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 26
                    self.field()
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 27
                        self.match(JSONParser.T__1)
                        self.state = 28
                        self.field()
                        self.state = 33
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 36
                self.match(JSONParser.T__2)
                pass
            elif token in [5]:
                localctx = JSONParser.ListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(JSONParser.T__4)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14242) != 0):
                    self.state = 38
                    self.value()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 39
                        self.match(JSONParser.T__1)
                        self.state = 40
                        self.value()
                        self.state = 45
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 48
                self.match(JSONParser.T__5)
                pass
            elif token in [7]:
                localctx = JSONParser.TrueBooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.match(JSONParser.TRUE)
                pass
            elif token in [8]:
                localctx = JSONParser.FalseBooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.match(JSONParser.FALSE)
                pass
            elif token in [9]:
                localctx = JSONParser.NullValueContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.match(JSONParser.NULL)
                pass
            elif token in [13]:
                localctx = JSONParser.WhitespaceContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.match(JSONParser.WS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





