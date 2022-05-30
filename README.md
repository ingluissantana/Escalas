# Escalas
Obtener todas las distintas escalas, despues de recibir una nota como entrada.



   
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

Link a la aplicacion:

https://share.streamlit.io/ingluissantana/escalas/main/escalas.py

#------------------------------------------------------------------------------------------------------------------------------------------------------------

The idea is to create a program that when the user enters the note of their choice, the output would be all the scales related to that note.

The problem I have now is that:

- Usually the notes should not be repeated, for example:

1.- When the user enters the letter 'G' the program gives this result:

Em - Gbm - G - A - Bm - Dbdim - D

but that is incorrect since the notes should not be repeated (in this case the G and the D are twice and
instead, the F # and C # should appear, which are the same but are substitutes specifically so that they do not exist
repeated notes)

2.- It should be:

Em - F # m - G - A - Bm - C # dim - D

is there a way in python to compare lists of strings? or how could I tell the program if you get
two notes repeated at the beginning of the string of the list let me know and you replace it with another note that is in another list.

Thank you very much for your help.

Link to the app:

https://share.streamlit.io/ingluissantana/escalas/main/escalas.py
