import streamlit as st
import pandas as pd

#sel = input("Ingrese una nota: ").capitalize()
notas = pd.DataFrame({'notas': ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']})

def escalas(sel):
    notas = pd.DataFrame({'notas': ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']})
    pos = notas.index[notas['notas']==sel].to_list()[0]
    notas = pd.concat([notas[pos:], notas[:pos]], ignore_index=True)
    mayor = notas.iloc[[0,2,4,5,7,9,11]]['notas'].tolist()
    lidio = notas.iloc[[0,2,4,6,7,9,11]]['notas'].tolist()
    mixolidio = notas.iloc[[0,2,4,5,7,9,10]]['notas'].tolist()
    menor = notas.iloc[[0,2,3,5,7,8,10]]['notas'].tolist()
    dorico = notas.iloc[[0,2,3,5,7,9,10]]['notas'].tolist()
    frigio = notas.iloc[[0,1,3,5,7,8,10]]['notas'].tolist()
    locrio= notas.iloc[[0,1,3,5,6,8,10]]['notas'].tolist()
    arm_menor = notas.iloc[[0,2,3,5,7,8,11]]['notas'].tolist()
    mel_menor = notas.iloc[[0,2,3,5,7,9,11]]['notas'].tolist()
    campo_mayor=     ["maj7", "m7", "m7", "maj7", '7', "m7", "ø"]
    campo_lidio=     ["maj7", "(7)<-", "m7", "ø", 'maj7', "m7", "m7<-"]
    campo_mixolidio= ["7", "m7", "ø", "maj7", 'm7<-', "m7", "maj7<-"]
    campo_menor=     ["m7", "ø", "maj7", "m7", 'm7', "maj7", "7"]
    campo_dorico=    ["m7", "m7<-", "maj7", "7<-", 'm7', "ø", "maj7"]
    campo_frigio=    ["m7", "maj7<-", "(7)", "m7", 'ø', "maj7", "m7<-"]
    campo_locrio=    ["ø", "", "m7", "m", 'maj7', "", "m"]
    campo_arm_menor= ["m", "ø", "+", "m", '', "", "ø"]
    campo_mel_menor= ["m", "m", "+", "", '', "ø", "ø"]
    escala_mayor = [x+y for x, y in zip(mayor, campo_mayor)]
    escala_lidia = [x+y for x, y in zip(lidio, campo_lidio)]
    escala_mixolidia = [x+y for x, y in zip(mixolidio, campo_mixolidio)]
    escala_menor = [x+y for x, y in zip(menor, campo_menor)]
    escala_dorica = [x+y for x, y in zip(dorico, campo_dorico)]
    escala_frigia = [x+y for x, y in zip(frigio, campo_frigio)]
    escala_locria = [x+y for x, y in zip(locrio, campo_locrio)]
    escala_arm_menor = [x+y for x, y in zip(arm_menor, campo_arm_menor)]
    escala_mel_menor = [x+y for x, y in zip(mel_menor, campo_mel_menor)]
    return escala_mayor, escala_lidia, escala_mixolidia, escala_menor, escala_dorica, escala_frigia, escala_locria, escala_arm_menor, escala_mel_menor


st.header('Selecciona la nota que deseas:')

st_nota = st.select_slider(
     'Nota',
     options=notas)
escala = esc(st_nota)
st.write('Escalas de ', st_nota)

st.code(escala.Show_all(), language="python")