# Listas en Python


<!--sec data-title="Ejercicio 1" data-id="section0" data-show=true data-collapse=true ces-->

Realiza una funcion que dada una matriz cuadrada \(es decir de tamaño n x n \) , dada la una fila elegida se desplace horizontalmente  a otra posicion .

Ejemplo :

Original              Mover Fila 1 a 3

1 2 3                           7 8 9

4 5 6                           6 5 2

7 8 9                           1 2 3

matrizEj = \[ \[1,2,3\],\[4,5,6\],\[7,8,9\] \]

matriz = moverFila\(matrizEj,1,3\)

print matriz =&gt; \[ \[7,8,9\] , \[6,5,2\] , \[1,2,3\] \]

<button class="section" target="section0_1" show="Mostrar Solucion" hide="Ocultar solucion"></button>

<!--endsec-->

<!--sec data-title="Ejercicio 1 Solucion" data-id="section0_1" data-show=false ces-->


```python

matriz = [ [1,2,3], [4,5,6], [7,8,9] ]
matriz2 = [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ]


def moverFila(matriz,filaOri,filaDest): 
    
    aux=matriz[filaDest]
    matriz[filaDest]=matriz[filaOri]
    matriz[filaOri]=aux 

    return matriz

print moverFila(matriz,1,2)
print moverFila(matriz2,1,2)


```

<!--endsec-->

<!--sec data-title="Ejercicio 2" data-id="section1" data-show=true data-collapse=true ces-->

Realiza una funcion que dada una matriz cuadrada \(es decir de tamaño n x n \) , dada la una columna elegida se desplace verticalmente a otra posicion .

Ejemplo :

Original          Mover Columnar 1 a 3

1 2 3                3 2 1

4 5 6                6 5 2

7 8 9                9 8 3

matrizEj = \[ \[1,2,3\],\[4,5,6\],\[7,8,9\] \]

matriz = moverColumna\(matrizEj,1,3\)

print matriz     =&gt; \[ \[3,2,1\] , \[6,5,2\] , \[9,8,3\] \]

<!--endsec-->


<!--sec data-title="Ejercicio 3" data-id="section2" data-show=true data-collapse=true ces-->

Realiza una funcion que dada una matriz cuadrada \(es decir de tamaño n x n \) , dada la una columna elegida se desplace verticalmente a otra posicion .

Ejemplo :

Matriz A                Matriz B

1 2                         3 2

4 5                         6 5

matrizA = \[ \[1,2\],\[4,5\] \]

matrizB = \[ \[3,2\],\[6,5\] \]

matriz= multiplicarMatrices\(matrizA,matrizB\)

print matriz =&gt; \[ \[15,12 \] , \[33,26\] \]

<!--endsec-->


<!--sec data-title="Ejercicio 4" data-id="section3" data-show=true data-collapse=true ces-->


Encuentra el [determinante](http://www.vitutor.com/algebra/determinantes/calculo.html) de una matriz \(Tienes un ejemplo en el link\)

<!--endsec-->






