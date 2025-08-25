
import mip


path = 'NETLIB/ship12s.mps'


model = mip.Model(solver_name='CBC') #GUROBI 
print("\n-------------------------------- Descrição do problema: --------------------------------")
print(f"Lendo arquivo: {path}")
model.read(path)

print(f"Problema: {model.name}")
print(f"Tipo: {'Maximização' if model.sense == mip.MAXIMIZE else 'Minimização'}")
print(f"Variáveis: {len(model.vars)}")
print(f"Restrições: {len(model.constrs)}")


print("\n-------------------------------- Solução do problema: --------------------------------")
model.optimize(max_seconds=3200)
model.verbose = False

# # Exibe resultados
print(f"\nStatus: {model.status.name}")
print(f"Valor objetivo: {model.objective_value:.6f}")

# # Algumas variáveis
print(f"\nPrimeiras 5 variáveis:")
count = 0
for var in model.vars:
    if count < 5:
        print(f"  {var.name}: {var.x:.6f}")
        count += 1
    else:
        break

