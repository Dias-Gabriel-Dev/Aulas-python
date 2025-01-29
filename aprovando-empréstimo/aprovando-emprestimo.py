rendaMensal = int(input("Digite o valor da sua mensal: "))
parcelaEmprestimo = int(input("Digite o valor da parcela desejada: "))

if rendaMensal > 2000 and parcelaEmprestimo <= 0.3 * rendaMensal:
    print("Empréstimo aprovado!")
elif rendaMensal <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")    