grammar JSON;

TRUE : 'True' | 'true' ;
FALSE : 'False' | 'false' ; 
NULL : 'null' | 'NULL' ;
INTEGER : '0' | [1-9][0-9]* ;
TEXT : [a-zA-Z_$][a-zA-Z0-9_$]* ;
STRING : '"' TEXT '"' ;
WS : [ \t\n\r\f]+ -> skip ;

json : '{' (field (',' field)*)? '}' ;

field : STRING ':' value;

value
    : STRING #String
    | INTEGER #Integer
    | '{' (field (',' field)*)? '}' #Dictionary
    | '[' (value (',' value)*)? ']' #List
    | TRUE #TrueBoolean
    | FALSE #FalseBoolean
    | NULL #NullValue
    | WS #Whitespace
    ;

