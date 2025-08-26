
import highspy
import numpy as np

path = 'NETLIB/25FV47.MPS'


h = highspy.Highs()
h.setOptionValue('solver', 'simplex') #simplex"/"i modelos disponiveis ipm, pdlp, simplex
h.readModel(path)
h.run()
print('Model ', path, ' has status ', h.getModelStatus())


solution = h.getSolution()
h.writeSolution('solution.txt', 1)


# opt_sol = np.array(solution.col_value, dtype=float)
# for i in range(len(opt_sol)):
#     if opt_sol[i] > 1:
#         print(f"Variável {i} tem valor {opt_sol[i]}")


#VER PARA O RELATORIO
#IMPRIMIR AS RESTRIÇOES ATIVAS
#IMPRIMIR O TIPO DE SOLUÇÃO: DUAL, PRIMAL, BOTH
#FAZER UM RELATÓRIO COMPARANDO SOLUÇÃO DE TODOS OS PROBLEMAS COM A SOLUÇÃO DO AQUITVO RESULTADOS.PDF
#FAZER UM RELATÓRIO DETALHADO PARA DOIS PROBLEMAS 

