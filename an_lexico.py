import ply.lex as lex

resultado_lexema = []

tokens = (
    'IDENTIFICADOR',
    'NUMERO',
    'ASIGNAR',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'PARIZQ',
    'PARDER',
    'FUNCTION',
)

#Expresiones Regualres para los tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_POTENCIA = r'\^'
t_ASIGNAR = r'='
t_PARIZQ = r'\('
t_PARDER = r'\)'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FUNCTION(t):
    r'SEN|COS|TAN|EXP|LN|LOG'
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4}\n Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "\nTipo " + str(tok.type) + " Lexema " + str(tok.value) + " Posicion " + str(tok.lexpos)
        resultado_lexema.append(estado)
    return resultado_lexema

analizador = lex.lex()