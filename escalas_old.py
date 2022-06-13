import streamlit as st
#import numpy as np
#import pandas as pd

notas_5= ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
notas_5_bem = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']
notas_num = [0,1,2,3,4,5,6,7,8,9,10,11]
zip_notas= list(zip(notas_num, notas_5))
zip_notas_bem= list(zip(notas_num, notas_5_bem))


class Escalas:
    def __init__(self,nota):
        self.nota = nota
        
    def First_order(self):

        nota_select = notas_5.index(self.nota)
        nota_select_list_order=notas_num[nota_select:] + notas_num[:nota_select]
        number_select_list_order=notas_5[nota_select:] + notas_5[:nota_select]
        zip_nota_selected= list(zip(nota_select_list_order, number_select_list_order))
        self.notas_selected = [b for a,b in zip_nota_selected]
        # nota_select_sos = notas_5_sos.index(self.nota)
        # nota_select_list_order_sos=notas_num[nota_select_sos:] + notas_num[:nota_select_sos]
        # number_select_list_order_sos=notas_5_sos[nota_select_sos:] + notas_5_sos[:nota_select_sos]
        # zip_nota_selected_sos= list(zip(nota_select_list_order_sos, number_select_list_order_sos))
        # self.notas_selected_sos = [b for a,b in zip_nota_selected_sos]
        return

    def Mayor(self):
        mayor = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [1,3,6,8,10]
        men = [1,2,5]
        self.mayor_final= [i for j, i in enumerate(mayor) if j not in rem]
        self.mayor_final=[self.mayor_final[k]+'m' if k in men else self.mayor_final[k] for k,v in enumerate(self.mayor_final)]
        self.mayor_final[-1] += 'dim'
        #mayor_final = " - ".join(mayor_final)
        return self.mayor_final
    
    def Menor(self):
        menor = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [1,4,6,9,11]
        men = [0,3,4]
        self.menor_final= [i for j, i in enumerate(menor) if j not in rem]
        self.menor_final=[self.menor_final[k]+'m' if k in men else self.menor_final[k] for k,v in enumerate(self.menor_final)]
        self.menor_final[1] += 'dim'
        #self.menor_final = " - ".join(self.menor_final)        
        return self.menor_final
    
    def Lidian(self):
        lidian = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [1,3,5,8,10]
        men = [2,5,6]
        lidian_final= [i for j, i in enumerate(lidian) if j not in rem]
        lidian_final=[lidian_final[k]+'m' if k in men else lidian_final[k] for k,v in enumerate(lidian_final)]
        lidian_final[3] += 'dim'
        for k,v in enumerate(lidian_final):
            if v in self.mayor_final:
                lidian_final[k]= '-'
        for k,v in enumerate(lidian_final):
            if v in self.menor_final:
                lidian_final[k]= '-'
        #lidian_final = " - ".join(lidian_final)
        return lidian_final
    
    def Mixo(self):
        mixo = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [1,3,6,8,11]
        men = [1,4,5]
        mixo_final= [i for j, i in enumerate(mixo) if j not in rem]
        mixo_final=[mixo_final[k]+'m' if k in men else mixo_final[k] for k,v in enumerate(mixo_final)]
        mixo_final[2] += 'dim'
        for k,v in enumerate(mixo_final):
            if v in self.mayor_final:
                mixo_final[k]= '-'   
        for k,v in enumerate(mixo_final):
            if v in self.menor_final:
                mixo_final[k]= '-'     
        #mixo_final = " - ".join(mixo_final)        
        return mixo_final
    
    def Dorian(self):
        dorian = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [1,4,6,8,11]
        men = [0,1,4]
        dorian_final= [i for j, i in enumerate(dorian) if j not in rem]
        dorian_final=[dorian_final[k]+'m' if k in men else dorian_final[k] for k,v in enumerate(dorian_final)]
        dorian_final[5] += 'dim'
        for k,v in enumerate(dorian_final):
            if v in self.menor_final:
                dorian_final[k]= '-'  
        for k,v in enumerate(dorian_final):
            if v in self.mayor_final:
                dorian_final[k]= '-'  
        #dorian_final = " - ".join(dorian_final)        
        return dorian_final
    
    def Frigia(self):
        frigia = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [2,4,6,9,11]
        men = [0,3,6]
        frigia_final= [i for j, i in enumerate(frigia) if j not in rem]
        frigia_final=[frigia_final[k]+'m' if k in men else frigia_final[k] for k,v in enumerate(frigia_final)]
        frigia_final[4] += 'dim'
        for k,v in enumerate(frigia_final):
            if v in self.menor_final:
                frigia_final[k]= '-' 
        for k,v in enumerate(frigia_final):
            if v in self.mayor_final:
                frigia_final[k]= '-'   
        #frigia_final = " - ".join(frigia_final)        
        return frigia_final
    
    def Locrian(self):
        locrian = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [2,4,7,9,11]
        men = [2,3,6]
        locrian_final= [i for j, i in enumerate(locrian) if j not in rem]
        locrian_final=[locrian_final[k]+'m' if k in men else locrian_final[k] for k,v in enumerate(locrian_final)]
        locrian_final[0] += 'dim'
        for k,v in enumerate(locrian_final):
            if v in self.menor_final:
                locrian_final[k]= '-'  
        for k,v in enumerate(locrian_final):
            if v in self.mayor_final:
                locrian_final[k]= '-'  
        #locrian_final = " - ".join(locrian_final)        
        return locrian_final
    
    def Harm_min(self):
        harm_min = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [1,4,6,9,10]
        men = [0,3]
        harm_min_final= [i for j, i in enumerate(harm_min) if j not in rem]
        harm_min_final=[harm_min_final[k]+'m' if k in men else harm_min_final[k] for k,v in enumerate(harm_min_final)]
        harm_min_final[1] += 'dim'
        harm_min_final[6] += 'dim'
        harm_min_final[2] += '+'
        for k,v in enumerate(harm_min_final):
            if v in self.menor_final:
                harm_min_final[k]= '-'  
        for k,v in enumerate(harm_min_final):
            if v in self.mayor_final:
                harm_min_final[k]= '-'  
        #harm_min_final = " - ".join(harm_min_final)        
        return harm_min_final
    
    def Mel_men(self):
        mel_men = self.notas_selected
        add = [0,2,4,5,7,9,11]
        rem = [1,4,6,8,10]
        men = [0,1]
        mel_men_final= [i for j, i in enumerate(mel_men) if j not in rem]
        mel_men_final=[mel_men_final[k]+'m' if k in men else mel_men_final[k] for k,v in enumerate(mel_men_final)]
        mel_men_final[5] += 'dim'
        mel_men_final[6] += 'dim'
        mel_men_final[2] += '+'
        for k,v in enumerate(mel_men_final):
            if v in self.menor_final:
                mel_men_final[k]= '-'  
        for k,v in enumerate(mel_men_final):
            if v in self.mayor_final:
                mel_men_final[k]= '-'  
        #mel_men_final = " - ".join(mel_men_final)        
        return mel_men_final
    
    def Show_all(self):
        escala.First_order()
        escala.Mayor()
        escala.Menor()
        escala.Lidian()
        escala.Mixo()
        escala.Dorian()
        escala.Frigia()
        escala.Locrian()
        escala.Harm_min()
        escala.Mel_men()
        return  f"\nEscala Mayor:\n{escala.Mayor()}\nEscala Lidia:\n{escala.Lidian()}\nEscala Mixolidia:\n{escala.Mixo()}\n\n\n" \
                f"Escala Menor:\n{escala.Menor()}\nEscala Dorica:\n{escala.Dorian()}\nEscala Frigia:\n{escala.Frigia()}\n" \
                f"Escala Locria:\n{escala.Locrian()}\n" \
                f"Escala Harmonica Menor:\n{escala.Harm_min()}\nEscala Melodica Menor:\n{escala.Mel_men()}\n\n"



st.header('Selecciona la nota que deseas:')

st_nota = st.select_slider(
     'Nota',
     options=notas_5)
escala = Escalas(st_nota)
st.write('Escalas de ', st_nota)

st.code(escala.Show_all(), language="python")
