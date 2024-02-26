### Universidad de Costa Rica
#### IE0405 - Modelos Probabilísticos de Señales y Sistemas
##### Proyecto 5: Teoría de colas 

Segundo ciclo del 2022

- Brayan Leal , B74083
- Joaquín Brenes, B61220
- Kevin Campos, B91519


# Paquete `cadena`

> Dentro de este paquete cadena se encuentras las diferentes funciones empaquetadas dentro
>de sus respectivos archivos ejecutables, las cuales se encargan de realizar cálculos
>respecto a los temas relacionados con Cadenas de Markof, encargándose estas de abarcar
>temas como: el cálculo de los parámetros Omega, p y q. Los parámetros mencionados 
>anteriormente son necesarios para poder desarrollar todos los cálculos posteriores 
>como gráficas, probabilidades, valores esperados y vectores de probabilidades.


La documentación completa está en `docs/_build/html/index.html`.

## Resultados

### Resultados del módulo análisis

![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/caso1.JPG)


![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/caso2.JPG)

### Resultados del módulo simulación
Grafica generada en la funcion visualizació utilizando datos aleatorios y un numero alto de clientes
![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/Figure_1.png)
Se observa como con los parametros base se da un sobrepaso de la fila esperada en muchas ocasiones

Los datos de la grafica se ven representados en la siguiente tabla obtenida de la funcion sistema
![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/ResultadoA4.jpg)

### Resultados del módulo servicio
Tablas del vector de estado estable generadas con el codigo de probabilidad para 5 y 10 estados

![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/mod6.png)

![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/mod61.png)

Resultado del servicio y porcentaje de clientes utilizando obtenido de la funcion fila

![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/mod7.png)

![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/mod71.png)

### Resultados del módulo dimensionamiento
Cantidad de servidores necesarios para reducir la fila a una cantidad menor a 5 en un total del 95% del tiempo

![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/mod8.png)

Cantidad de tiempo necesario para reducir la fila a una cantidad menor a 5 en un total del 95% del tiempo

![h](https://github.com/mpss-eie/P5G19/blob/main/cadena/mod9.png)
