###Anotações Gerais Python
**Format**
~~~python
print("Seu nome é: {0} e sua idade é: {1}".format(nome,idade))
~~~
~~~python
print(f"Seu nome é: {nome} e sua idade é: {idade}")
~~~

**Operadores de associação**
* Operador `in` 
* Operador `not in` 

**Operador ternário/Expressões condicionais**
~~~python
print("B") if b > a else print("A")

~~~
**Alinhamento de if**
~~~python
if a > b:
    if a> c:
        print("A é maior que B e que C")
~~~

**Else no While**
~~~python
while a > b:
    #bloco de código
else:
    print("A não é maior que B")
~~~

**Range**
~~~python
    for x in range(5,8):
~~~
start, stop, steep 
~~~python
    for x in range(1,8,2):
~~~

**Continue e Pass**
~~~python
    continue pula oq está acontecendo 
    pass ignora 
~~~

**Listas**
~~~python
    lista = [True, 1, 3, "nome"] 
    print(type(lista))
    print(lista[-1])#nome
    print(lista[::])#imprime tudo
    print(lista[1:])#imprime o primeiro elemento até o último
    print(lista[:3])#imprime do início até o terceiro elemento
    print(lista[1:4])#início e fim
    print(lista[1:4:2]#start, stop, steep)
~~~

**Listas dentro de Listas**
~~~python
    listajunta = lista1+lista2
    print(len(lista1)) #mostra tamanho da lista
~~~

**Funções para tipos de dados numéricos**
~~~python
    print(sum(lista)) #somatório dos valores de uma lista
    print(max(lista)) #maior valor dentro da lista
    print(min(lista))#menor valor dentro da lista
~~~
**Mais sobre listas**
lista a partir de range:
~~~python
    lista = list(range(10)) #cria lista [0,1,2...,9]
    lista2 = list("Frase") #cria lista ['F','r','a','s','e']
~~~
modificar itens na lista: 
~~~python
    lista = ["banana","maça","morango"]
    lista[1] = "amora" #item banana substituido por amaora 
~~~
~~~python
    lista = ["carro","casa","sapato"]
    for x in lista:
        print(x) #mostra valores separados
~~~
outra forma de impressão
~~~python
    lista = ["carro","casa","sapato"]
    for x in range(len(lista)):
        print(x,lista[x]) #mostra o index e o elemento correspondente
~~~
* split
~~~python
    texto = "carro, barco"
    lista = list[texto] #cria lista com cada caracter incluindo a vírgula
    texto = texto.split(',') #vai exibir ['carro','barco']
~~~
**Adicionar elementos na lista**
~~~python
    lista.append("elemento")
    lista.append(["mais elemento","outro"])#adiciona mais de um elemento como uma lista
    lista.insert(1,"novo") #adiciona no lugar especificado
    lista.extend(["mais elemento","outro"])#adiciona mais de um elemento porém cada elemento é adicionada separadamente

~~~
**Remover elementos na lista**
~~~python
    lista.pop()#remove ultimo elemento ou pode passar o index
    lista.remove("barco")
    del lista[0] #deleta o elemento do index
    lista.clear()#limpa os elementos da lista
~~~
**Ordenar listas**
~~~python
    lista.sort()
    lista.sort(reverse=True)#ordena de forma reversa
    lista.reverse()#apenas inverte a lista
    lista.sort(key = str.lower)#ordena mesmo que a primeira letra do elemento seja minúscula
~~~
**Copiando listas**
~~~python
    lista2 = lista #as listas passam a ser iguais, oq edita em uma edita na outra
    lista2 = lista.copy() #copia a lista e as separa
~~~