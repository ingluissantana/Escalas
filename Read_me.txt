La idea es crear un programa que cuando el usuario ingrese la nota de su preferencia, la salida sería todas las escalas relacionadas a esa nota.

El problema que tengo ahora es que:

- Usualmente las notas no deberian repetirse, por ejemplo:

1.- Cuando el usuario ingresa la letra 'G' el programa da este resultado:

Em - Gbm - G - A - Bm - Dbdim - D

pero eso es incorrecto ya que las notas no deberian repetirse (en este caso la G y la D estan dos veces y 
en su lugar deberia aparecer el F# y C# que es lo mismo pero son sustitutos especificamente para que no existan
notas repetidas)

2.- Deberia ser:

Em - F#m - G - A - Bm - C#dim - D

existe alguna manera en python de comparar listas de strings? o como podria decirle al programa si consigues 
dos notas repetidas al principio del string de la lista avisame y la reemplazas por otra nota que esta en otra lista.

Muchas gracias por tu ayuda.
