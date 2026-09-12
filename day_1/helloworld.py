#Day 1 - David's practice

print(2+3) #Addition
print(5-2) #Subtraction
print(2*3) #multiplication
print(6/2) #Division
print(2**3) #Exponentiation
print(5%2) #Modulus
print(5//2) #Floor Division

#Checking data types
print(type(10)) #int
print(type(10.5)) #float
print(type("Hello World")) #str
print(type(True)) #bool
print(type(1+2j)) #complex
print(type([1,2,3])) #list #You can modify the list
print(type((1,2,3))) #tuple #You cannot modify the tuple, they are immutable
print(type({1,3,2,3})) #set #You cannot modify the set, they are mutable but unordered
print(type({"name":"David", "age":30})) #dict #You can modify the dictionary

#Practice

A=10
print('TIPO DE ARCHIVO:', type(A))

#Calcular la distancia euclidiana entre (2,3) y (10,8)
x1=2
y1=3
x2=10
y2=8
distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('La distancia euclidiana entre (2,3) y (10,8) es:', distancia)
