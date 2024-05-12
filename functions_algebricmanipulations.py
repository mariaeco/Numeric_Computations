from sympy import symbols, IndexedBase, Sum, Eqn, simplify
from algebra_with_sympy import *
import numpy as np


def ponto1(yv, eq, k): #k é a equação que quero 
    y = IndexedBase('y')
    z = yv[0] #valor inicial y0 que temos
    
    eq[k] = eq[k].evalf(4, subs={y[0]: z})
    #Colocando o valor y0 para o outro lado da equação
    #Neste caso só preciso mudar a primeira Equação
    common_y_terms = eq[k].lhs.collect(y[0])
    remaining_terms = eq[k].rhs
    eq[k] = Eq(common_y_terms + z, remaining_terms+z) #aqui estou jogando o valor de y0 para o outro lado

    return eq[k]

def ponto2(yv, eq, k): #k é a equação que quero 
    i = symbols('i')
    y = IndexedBase('y')
    
    size = len(yv)-1
    z = yv[size] #valor inicial y0 que temos
    for k in range(1, len(eq)+1):
        eq[k] = eq[k].evalf(4, subs={y[size]: z})

    #Colocando o valor y0 para o outro lado da equação
    #Neste caso só preciso mudar a primeira Equação
    common_y_terms = eq[k].lhs.collect(y[i])
    remaining_terms = eq[k].rhs
    eq[k] = Eq(common_y_terms + z, remaining_terms+z) #aqui estou jogando o valor de y0 para o outro lado

    
    return eq[k]
    
def eq1(eq, valor, ylprog):
    #Mudando a primeira equação
    i, h = symbols('i, h')
    y = IndexedBase('y')
    ylprog = ylprog.subs(i, 0)
    ylprog_lhs = ylprog.lhs.subs(y[0], valor)
    eq_substituted = Eq(ylprog_lhs, ylprog.rhs)
    equation_moved = Eq(ylprog_lhs * h, ylprog.rhs * h)
    eq_moved = Eq((-1)*(equation_moved.rhs-y[1]),(-1)*(equation_moved.lhs-y[1]))
    eqmoved = Eq(eq[1].lhs - eq_moved.rhs + eq_moved.lhs, eq[1].rhs)
    # Agrupando os elementos em comum
    common_y_terms = eqmoved.lhs.collect(y[1])
    remaining_terms = eqmoved.rhs
    # Equação discretizada final
    grouped_equation = Eq(common_y_terms, remaining_terms)
    const = 1
    eq[1] = Eq(grouped_equation.lhs - const*h, grouped_equation.rhs + h) 

    return eq[1]


def eqF(eq, valor, ylregr):
    #Mudando a ultima equação
    i, h = symbols('i, h')
    y = IndexedBase('y')
    n = len(eq)+1
    ylregr = ylregr.subs(i, n)
    ylregr_lhs = ylregr.lhs.subs(y[n], valor)
    equation_moved = Eq(ylregr_lhs * h, ylregr.rhs * h)
    eq_moved = Eq(equation_moved.rhs + y[n-1],equation_moved.lhs+y[n-1])
    #substituindo na ultima equacao
    eqmoved = Eq(eq[n-1].lhs - eq_moved.rhs + eq_moved.lhs, eq[n-1].rhs)
    # Agrupando os elementos em comum
    common_y_terms = eqmoved.lhs.collect(y[n-1])
    remaining_terms = eqmoved.rhs
    # Equação discretizada final
    grouped_equation = Eq(common_y_terms, remaining_terms)
    const = 1
    eq[n-1] = Eq(grouped_equation.lhs  - const*h, grouped_equation.rhs + h) 

    return eq[n-1]


def matriz(eq):
    #RETORNO AS MATRIZES A E B
    n = len(eq)
    matrix = [[0 for _ in range(n-1)] for _ in range(n-1)]
    matrix
    
    for i in range(1,n):
    # print("Eq ", i, "---------------")
        for j in range(len(eq[i].args[0].args)): #len(eq[2].args[0].args) é a qtd de y que tenho
            if eq[i].args[0].args[j].args[1].args[1] == 1:
                matrix[i-1][0] = eq[i].args[0].args[j].args[0]
            if eq[i].args[0].args[j].args[1].args[1] == 2:
                matrix[i-1][1] = eq[i].args[0].args[j].args[0]
            if eq[i].args[0].args[j].args[1].args[1] == 3:
                matrix[i-1][2] = eq[i].args[0].args[j].args[0]
            if eq[i].args[0].args[j].args[1].args[1] == 4:
                matrix[i-1][3] = eq[i].args[0].args[j].args[0]
    B = []
    for i in range(1,n):
        B.append(eq[i].rhs)
    
    return matrix, B


def matriz_aumentada(matrixA, b, xv):
    i, h, z = symbols('i h z')
    y = IndexedBase('y')
    x = IndexedBase('x')
    A = np.array(matrixA.copy())
    for i in range(len(matrixA)):
        A[i, i] = A[i, i].subs(h, 0.25)

    B = np.array(b.copy())
    for i in range(len(B)):
        B[i] = B[i].subs(h, 0.25)
        B[i] = B[i].subs(x[i+1],xv[i+1])
        
    matrix_aumentada = np.concatenate((Matrix(A),Matrix(B)), axis=1)

    return list(matrix_aumentada)

def criaEq(eq_geral):
    n = 5
    i  = symbols('i')
    y = IndexedBase('y')
    x = IndexedBase('x')
    eq = {}
    for k in range(1,n):
        equation = eq_geral.subs(i, k)
        eq[k] = equation
    return eq