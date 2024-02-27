import ply.lex as lex

# Token definitions
tokens = (
    'PYTHON',
    'CPP',
    'JAVA',
    'PYTHON_DEF',
    'CPP_INCLUDE',
    'FUNCTION_DEF',
    'VAR_DECL', 
    'ASSIGN',    
    'RETURN',  
    'FUNCTION_CALL',
    'CALCULATION_OR_IDENTIFIER',
    'CPP_PRINT',
    'BRANCH',
    'FOR_LOOP',
    'WHILE_LOOP',
    'ACCESS_SPECIFIERS',
    'FUNCTION_DECL',
    'CLASS',
    'PYTHON_CLASS',
)

# Define the regular expressions for each language
def t_PYTHON_DEF(t):
    r'\bdef\b\s+[a-zA-Z_]\w*\s*\(\s*\)\s*:\s*'
    return t

def t_JAVA(t):
    r'\b(finally|super|this\.[a-zA-Z_]\w*|@Override|static|abstract|package)\b;?'
    return t

def t_CPP(t):
    r'\b(this->[a-zA-Z_]\w*|virtual|cin|using|namespace|std|<<|>>)\b[a-zA-Z_]?;?'
    return t

def t_CPP_INCLUDE(t):
    r'\#include\s*<.*?>'
    return t

def t_CPP_PRINT(t):
    r'\bcout\s*(<<\s*(?:[a-zA-Z_]\w*|"([^"]*)"))*\s*(<<endl)*;?'
    return t

def t_CLASS(t):
    r'\bclass\b\s+[a-zA-Z_]\w*\s*(\([^)]*\))?\s*{'
    return t

def t_PYTHON_CLASS(t):
    r'class\s+[a-zA-Z_]\w*\s*:'
    return t

def t_PYTHON(t):
    r'\b(self|pass|except|try)\b'
    return t

def t_ACCESS_SPECIFIERS(t):
    r'\b(public|private|protected)\b'
    return t

def t_FOR_LOOP(t):
    r'\bfor\s*\(\s*.*?\s*\)\s*{'
    return t

def t_WHILE_LOOP(t):
    r'\bwhile\s*\(\s*.*?\s*\)\s*{'
    return t

def t_BRANCH(t):
    r'\b(if|else\sif)\b\(\s*(.*?)\s*\){? |else'
    return t

def t_FUNCTION_CALL(t):
    r'\b(?:[a-zA-Z_]\w*\.)*[a-zA-Z_]\w*\(\s*(?:.+?)?\s*\);?'
    return t

def t_FUNCTION_DEF(t):
    r'\b(?:int|float|char|void)\s+[a-zA-Z_]\w*\s*\(\s*(?:[a-zA-Z_]\w*\s+[a-zA-Z_]\w*\s*)*\)\s*{'
    return t

def t_FUNCTION_DECL(t):
    r'\b(int|float|char|void)\s[a-zA-Z_]\w*\(\s*(?:.+?)?\s*\);?'
    return t

def t_VAR_DECL(t):
    r'\b(?:int|float|char)\s+[a-zA-Z_]\w*\s*(?:=\s*\S+)?\s*;?'
    return t

def t_ASSIGN(t):
    r'[a-zA-Z_]\w*\s*='
    t.value = t.value.rstrip('\n')
    return t

def t_RETURN(t):
    r'\breturn\b\s+([a-zA-Z_]|\d+)\w*(\s*[\+\-%\*/]\s*([a-zA-Z_]|\d+)\w*)*\s*;?'
    return t

def t_CALCULATION_OR_IDENTIFIER(t):
    r'([a-zA-Z_]|\d+)\w*(\s*[\+\-%\*/]\s*([a-zA-Z_]|\d+)\w*)*\s*;?'
    return t

# Ignore whitespace
t_ignore = ' \t\n}'

# Error handling
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
def test_lexer(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        tokens.append(tok)
    return tokens