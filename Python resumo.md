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
