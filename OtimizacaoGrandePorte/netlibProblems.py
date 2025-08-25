import pulp


path = 'NETLIB/ship12s.mps'
variables, problem = pulp.LpProblem.fromMPS(path)

#descrição do problema
print("\n-------------------------------- Descrição do problema: --------------------------------")
print(f"Problema carregado: {problem.name}")
print(f"Tipo: {'Maximização' if problem.sense == 1 else 'Minimização'}")
print(f"Variáveis: {len(variables)}")
print(f"Restrições: {len(problem.constraints)}")

#solução do problema
print("\n-------------------------------- Solução do problema: --------------------------------")

solver = pulp.PULP_CBC_CMD(msg=0)
# solver = pulp.GUROBI_CMD(msg=0)
results = problem.solve(solver)

print(f'status: {results}')
print(f"objective: {problem.objective.value()}")


results = {
    "status": pulp.LpStatus[results],
    "objective_value": pulp.value(problem.objective),
    "variables": {},
    "problem_name": problem.name
}

for var in problem.variables():
    results["variables"][var.name] = var.varValue


print(f"\n=== RESULTADOS ===")
print(f"Status: {results['status']}")
print(f"Valor da função objetivo: {results['objective_value']}")


if results['variables']:
    print(f"\nValores das variáveis (não-zero):")
    count = 0
    for var_name, value in results['variables'].items():
        if value is not None and abs(value) > 1e-10:
            print(f"  {var_name}: {value:.6f}")
            count += 1
            if count >= 10:  # Limita a 10 variáveis para não poluir a saída
                print(f"  ... e mais {len(results['variables']) - count} variáveis")
                break


