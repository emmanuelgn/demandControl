# main.py
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Minha Aplicação de Produtividade")

        self.label = tk.Label(master, text="Adicionar Nova Demanda:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Adicionar", command=self.add_demand)
        self.add_button.pack()

    def add_demand(self):
        demand = self.entry.get()
        # Aqui você pode adicionar a lógica para salvar a demanda localmente
        print("Nova demanda adicionada:", demand)
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
