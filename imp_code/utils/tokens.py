#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LOWER_ALPHA = 'abcdefghijklmnopqrstuvwxyz'
UPPER_ALPHA = LOWER_ALPHA.upper()
ALPHABET = LOWER_ALPHA + UPPER_ALPHA

#######################################
# TOKENS
#######################################

# MAIN
TT_MAIN     = 'Commence'

# DATA TYPES
TT_INT		= 'Numeral'
TT_FLOAT    = 'Decimal'
TT_CHAR     = 'Letter'
TT_STRING   = 'Missive'
TT_DOUBLE   = 'Doublet'
TT_BOOL     = 'Veracity'
TT_LONG     = 'Prolonged'
TT_SHORT    = 'Brief'
TT_VOID     = 'Void'
TT_CONST    = 'Constant'
TT_UNSIGNED = 'Unsigned'
TT_SIGNED   = 'Signed'
TT_STRUCT   = 'Assembly'
TT_UNION    = 'Consort'
TT_ENUM     = 'Enumerate'
TT_ARRAY = 'Ledger'

#INPUT/OUTPUT
TT_INPUT = 'Proclaim'
TT_OUTPUT = 'Inquire'

# ARITHMETIC OPERATIONS
TT_PLUS     = '+'
TT_MINUS    = '-'
TT_MUL      = '*'
TT_DIV      = '/'
TT_MODULU   = '%'

#CONDITIONAL STATEMENTS
TT_CASE     = 'Event'
TT_IF       = 'Perchance'
TT_ELSE     = 'Otherwise'
TT_SWITCH   = 'Given'
TT_DEFAULT  = 'Default'

#MEMORY MANAGEMENT FUNCTIONS
TT_MALLOC = 'Allocate'
TT_FREE = 'Liberate'

#LOOP STATEMENTS
TT_WHILE    = 'Whilst'
TT_FOR      = 'Iterate'
TT_DO       = 'Perform'

#LOOP CONTROL
TT_BREAK = 'Cease'
TT_CONTINUE = 'Proceed'
TT_RETURN = 'Dispatch'
TT_GOTO = 'Direct'

#VALUES
TT_TRUE     = 'Indeed'
TT_FALSE    = 'Nay'
TT_NULL     = 'Naught'

#LOGICAL OPERATOR
TT_AND = '&&'
TT_OR = '||'
TT_NOT = '!'


TT_LPAREN   = '('
TT_RPAREN   = ')'
TT_LBRACKET ='['
TT_RBRACKET = ']'
TT_LBRACE   = '{'
TT_RBRACE   = '}'

#ASSIGNMENT OPERATOR
TT_EQUAL    = '='

#COMPOUND ASSIGNMENT OPERATOR
TT_PLUSEAND = '+='
TT_MINUSAND = '-='
TT_MULAND   = '*='
TT_DIVAND   = '/='
TT_MODAND   = '%='

#INCREAMENT AND DECREMENT OPERATORS
TT_INC      = '++'
TT_DEC      = '--'

#COMPARISON OPERATORS
TT_EQUALTO  = '=='
TT_NOTEQUAL = '!='
TT_LESSTHAN = '<'
TT_GREATERTHAN = '>'
TT_LESSTHANEQUAL = '<='
TT_GREATERTHANEQUAL = '>='

# OTHERS
TT_SPACE     = 'SPACE'
TT_NEWLINE   = '\n'
TT_TERMINATE = ';'
TT_PERIOD    = '.'
TT_COMMA     = ','
TT_SLINECOM  = '//'
TT_LMULCOM   = '/*'
TT_RMULCOM   = '*/'
TT_SIZEOF    = 'Sizeof'
TT_CLRSCR    = 'Voila'


class Tokens:
    def __init__(self, type_,value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'