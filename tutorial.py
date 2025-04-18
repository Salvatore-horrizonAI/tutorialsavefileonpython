#Tutorial da Salvatore Naro su come creare un file per salvare le varie informazioni su un file CSV 
import tkinter #Importate tkinter
from tkinter import filedialog #importare filedialog
import csv #importare csv

save = filedialog.asksaveasfilename(defaultextension=".csv",#utilizziamo la libreria filedialog per creare il menu per salvare il file
                                    filetypes=[("CSV","*.csv")],
                                    title="Save file CSV")


try:# per prevenire i vari errori usiamo try,except,finally
    nome={
        "Salvatore":"Giovanni",#creiamo una variabile nome contente i vari valori
        "Carlo":"Roberto"
    }
    with open(save,"w",newline="") as file: 
        save_file= csv.writer(file)#leggiamo la variabile file
        save_file.writerow(["Nome1","Nome2"])#creiamo una tabella
        for key,value in nome.items(): #dato che sono due i nomi creiamo due variabili e li assegnamo i valori della variabile nome
            value_str=str(value) #creiamo una stringa contente il valore di value
            save_file.writerow([key,str(value_str)])#assegnamo alla tabella i vari valori

except ValueError as e:#preveniamo i vari errori del programma
    print(f"Non è stato possibile salvare il file ")
except KeyboardInterrupt as e:#preveniamo i vari errori del programma
     print(f"Non è stato possibile salvare il file ")
except KeyError as e:#preveniamo i vari errori del programma
     print(f"Non è stato possibile salvare il file ")
finally:#alla fine di tutto stampa tale risultato
    print(f"Buonagiornata")