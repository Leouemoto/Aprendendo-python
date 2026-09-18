faturamento = 1000
custo = 600 
lucro = faturamento - custo

novas_vendas = 200

faturamento = faturamento + novas_vendas

imposto = 0.15  * faturamento #float
lucro = faturamento - custo - imposto

print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", lucro)   
print("Imposto", imposto)

mensagem = "O lucro é de: " + str(lucro) #string
teve_lucro = lucro > 0 #boolean

margem_lucro = lucro / faturamento * 100

print(mensagem)
print("Teve lucro?", teve_lucro)
print("Margem de lucro:", margem_lucro, "%")


#int = numeros inteiros
#float = numeros decimais
#string = texto
#boolean = verdadeiro ou falso

#operadores especiais

# mod -> %
# resto da divisão de um numero pelo outro
# 10 % 3 = 1

#floor division -> //
# divisão inteira de um numero pelo outro