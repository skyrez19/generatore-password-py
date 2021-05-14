import tkinter as tk
import random, string, os

# setup della finestra
finestra = tk.Tk()
finestra.geometry("600x350")
finestra.title("Generatore casuale di password - Realizzato da SkyRez19")
finestra.grid_columnconfigure(0, weight=1)
finestra.resizable(False, False)

def generaPassword():
    # controllo che la password sia stata inserita
    if lunghezzaInput.get():
        # prendo la lunghezza
        lunghezza = int(lunghezzaInput.get())
    # altrimenti, default 14
    else:
        lunghezza = 14

    # genero la password
    caratteri = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    password = (''.join(random.choice(caratteri) for i in range(lunghezza)))

    # stampo il risultato
    messaggio = tk.Label(text=("PASSWORD DI %s CARATTERI GENERATA CON SUCCESSO" % lunghezza), font=("Arial 8 bold"),fg="green")
    messaggio.grid(row=5, column=0, sticky="N", pady=(10, 10))
    risultato = tk.Text(finestra, height=5)
    risultato.insert(tk.END, password)
    risultato.grid(row=6, column=0, sticky="WE", padx=50, pady=0)

# testo iniziale
intestazione = tk.Label(finestra, text="GENERATORE CASUALE DI PASSWORD", font=("Arial 16 bold"))
intestazione.grid(row=0, column=0, pady=(30, 0))
intestazioneNome = tk.Label(finestra, text="Sviluppato da SkyRez19", font=("Arial 10 bold italic"))
intestazioneNome.grid(row=1, column=0)

# testo della lunghezza
testoLunghezza = tk.Label(finestra, text="Scegli la lunghezza della password (default 14 caratteri)", font=("Arial", 10))
testoLunghezza.grid(row=2, column=0, pady=(25, 10))
# input lunghezza della password da generare
lunghezzaInput = tk.Entry()
lunghezzaInput.grid(row=3, column=0, sticky="WE", padx=50)
# pulsante genera password
generaBtn = tk.Button(finestra, text="Genera password", command=generaPassword)
generaBtn.grid(row=4, column=0, sticky="WE", padx=50, pady=(10, 0))

# eseguo la finestra
finestra.mainloop()

