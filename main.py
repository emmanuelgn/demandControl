# main.py
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Demand Control")

        # Calculate the window position for centering
        window_width = 400
        window_height = 200
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # Set the window position and size
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")

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
