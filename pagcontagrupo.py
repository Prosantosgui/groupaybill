import sys
c = float(input('Informe o valor total do consumo: R$'))
if c <= 0:
    print('Valor Inválido!')
    sys.exit()
f = int(input('Informe o total de pessoas: '))
if f <= 0:
    print('Valor inválido!')
    sys.exit('Número inválido de pessoas!')
p = float(input('Informe o percentual da taxa de serviço: '))
if p>100 or p<0:
    print('Valor inválido!')
    sys.exit()
vtaxa = c * (p/100)
vtotal = c + vtaxa
vfinal = vtotal / f
vtotal = round (vtotal,2)
vfinal = round (vfinal,2)
vtotal_format = str(vtotal)
vtotal_format = vtotal_format.replace('.',',')
vfinal_format = str(vfinal)
vfinal_format = vfinal_format.replace('.',',')
print(f'O valor total da conta, com a taxa de serviço será de R${vtotal_format}!')
print(f'Dividindo a conta por {f} pessoa(s), cada pessoa pagará R${vfinal_format}!')