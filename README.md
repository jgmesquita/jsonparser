# JSON Library

This project was made to refine my knowledge about parsers and data structures in Python. I used ANTLR which is the most familiar library to me. 

I used AI only for installing and troubleshooting some problems with dependencies and packages. I didn't use it to generate any code. It would defeat the purpose of this project! :P


## Grammar

This grammar is as simples as we can make it. It still doesn't support decimal numbers. It might fail some edge cases I haven't taken care. I followed the official JSON website (https://www.json.org/json-en.html) to get an idea on how I could tackle the structure of the grammar.

```
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
```

## ObjectJSON Class

These are some examples of methods from ObjectJSON class:

```py
def main():
    json_file = ObjectJSON("test.json")  # Create object 
    json_file.print()                    # Print to the terminal
    json_file.get("skills")              # Print to the terminal the value from a field
    json_file.set("age", 24)             # Field exists
    json_file.set("Test", 1)             # Field doesn't exist
    json_file.serialize("output.json")   # Output to another file
```


## Dependencies
To execute this library, you will need to install Java and the following library from Python:

```
pip install antlr4-python3-runtime==4.13.2
```
