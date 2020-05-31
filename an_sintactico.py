import ply.yacc as yacc
from an_lexico import tokens
from an_lexico import analizador
import math

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('left', 'UMINUS'),
    ('right', 'POTENCIA'),
)
constantes = {
    'PI':   3.1415926,
    'e':    2.71828182,
    'GAMMA':0.57721566,
    'DEG':  57.29577951,
    'PHI':  1.618033988
}
nombres = {}

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion'
    if t[1] not in constantes.keys():
        nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '^':
        t[0] = pow(t[1], t[3])

def p_expresion_funcion(t):
    'expresion : FUNCTION PARIZQ expresion PARDER'
    if t[1] == 'SEN':
        t[0] = math.sin(t[3])

    elif t[1] == 'COS':
        t[0] = math.cos(t[3])

    elif t[1] == 'TAN':
        t[0] = math.tan(t[3])

    elif t[1] == 'EXP':
        t[0] = math.exp(t[3])

    elif t[1] == 'LN':
        t[0] = math.log(t[3])

    elif t[1] == 'LOG':
        t[0] = math.log(t[3],10)

def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]

def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER
    '''
    t[0] = t[2]

def p_expresion_numero(t):
    'expresion : NUMERO'
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        if t[1] in constantes.keys():
            t[0] = constantes[t[1]]
        else:
            t[0] = nombres[t[1]]
    except LookupError:
        print("variable desconocida ", t[1])
        t[0] = 0

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)



# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))

    return resultado_gramatica
