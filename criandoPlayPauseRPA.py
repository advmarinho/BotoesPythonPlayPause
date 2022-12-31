import tkinter as tk
import time
from threading import Thread


def start_rpa():
    # O código do seu RPA vai aqui
    print("Iniciando RPA...")
    for i in range(5):
        time.sleep(1)
        print(f"Executando passo {i+1}")
   

def pause_rpa():
    # Pausa a execução do RPA
    print("RPA pausado")

def gui():
    root = tk.Tk()
    name = 'Play/Pause to RPA'
    root.title(name)
    # cenario = tk.Canvas(root, width=300, height=300)



    start_button = tk.Button(root, text="Iniciar", command=start_rpa, bg='green')
    start_button.pack()
    start_button.place(x=25, y=75)

    pause_button = tk.Button(root, text="Pausar", command=pause_rpa, bg='red')
    pause_button.pack()
    pause_button.place(x=100, y=75)
    root.mainloop()
Thread(target=gui).start()