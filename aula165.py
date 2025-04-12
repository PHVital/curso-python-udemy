from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parecelas = len(data_parcelas)
valor_parcela = valor_total / numero_parecelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R${valor_total:,.2f} para pagar'
    f'em {delta_anos.years} anos'
    f'({numero_parecelas} meses) em parcelas de '
    f'R${valor_parcela:,.2f}.'
)