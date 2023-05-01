import tkinter as tk
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from requests import get
from pymongo import MongoClient
from decouple import config


BASE_URL = 'https://www.albion-online-data.com/api/v2/stats/Prices/'

#############################    MONGO   #############################

# Conectar a la base de datos
client = config("MONGOAPI")
client = MongoClient(client)

db = client['AlbionMarketplace']
items = db['items']
world = db['world']

#############################   TKINTER   #############################

# Ventana principal
root = tk.Tk()
root.title("Albion Marketplace")

# NOTEBOOKS ---------------------
# Create a notebook for the tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# FRAMES ---------------------
# Create a frame for the comparision tab
comparision_frame = ttk.Frame(notebook, padding=10)
notebook.add(comparision_frame, text="Comparación")
# Create a frame for the items tab
allitems_frame = ttk.Frame(notebook, padding=10)
notebook.add(allitems_frame, text="Items")


# Frame de los ítems
items_frame = tk.Frame(root)
items_frame.pack(side=tk.TOP)
# Frame de los precios
prices_frame = tk.Frame(root)
prices_frame.pack(side=tk.TOP)

# Crear una frame para la combobox en la pestaña "Comparación"
combobox_frame = ttk.Frame(comparision_frame, padding=10)
combobox_frame.pack(side=tk.TOP)

# LISTBOX ---------------------
# Lista desplegable de ítems en la comparación
item_var = tk.StringVar()
item_combobox = AutocompleteCombobox(
    combobox_frame, 
    textvariable=item_var, 
    completevalues=sorted([i['UniqueName'] for i in items.find()]))
item_combobox.pack(side=tk.LEFT, padx=5)
item_combobox.config(width=60)

# Crear un scrollbar
scrollbar = tk.Scrollbar(allitems_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Crear la lista desplegable y asociarla con el scrollbar
items_listbox = tk.Listbox(allitems_frame, width=40, height=10, yscrollcommand=scrollbar.set)
items_listbox.pack(side=tk.LEFT, padx=5)
# Configurar el scrollbar para controlar la lista
scrollbar.config(command=items_listbox.yview)

# Agregar los elementos de la lista
for item in items.find():
    items_listbox.insert(tk.END, item['UniqueName'])


# Frame de los precios
prices_frame = tk.Frame(comparision_frame)
prices_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)


# FUNCTIONS ---------------------
def search():

    item = item_var.get()
    for child in prices_frame.winfo_children():
        child.destroy()
    prices = [] # Lista para almacenar los precios

    for i, city_doc in enumerate(world.find()):
        city_name = city_doc['UniqueName']
        label = tk.Label(prices_frame, text=city_name + ": ")
        label.grid(row=i, column=0, sticky=tk.E, padx=5, pady=5)
        params = {
            'item': item,
            'locations': city_name,
            'qualities': '1'
        }
        response = get(f'{BASE_URL}{item}.json', params=params)
        # Comprobación de éxito en la api
        if response.status_code == 200:
            response_data = response.json()[0]
            price = response_data['sell_price_min']
            if price is not None and price != 0: # Excluir valores en 0 y None
                price = int(price)
                prices.append(price) # Añadir precio a la lista
                price_label = tk.Label(prices_frame, text=str(price) + " Plata")
                price_label.grid(row=i, column=1, sticky=tk.W, padx=5, pady=5)
            else:
                price_label = tk.Label(prices_frame, text="No hay existencias")
                price_label.grid(row=i, column=1, sticky=tk.W, padx=5, pady=5)
        else:
            price_label = tk.Label(prices_frame, text="Error al obtener precios")
            price_label.grid(row=i, column=1, sticky=tk.W, padx=5, pady=5)
    
    # Encontrar el mínimo y el máximo precio, si hay precios
    if prices:
        min_price = min(prices)
        max_price = max(prices)
    else:
        min_price = 0
        max_price = 0
    
    # Asignar el color de acuerdo al precio mínimo o máximo
    for i, child in enumerate(prices_frame.winfo_children()):
        if isinstance(child, tk.Label) and "Plata" in child.cget("text"):
            price = int(child.cget("text").replace(" Plata", ""))
            if price == min_price:
                child.config(fg='green')
            elif price == max_price:
                child.config(fg='red')
                
# Autocompletados
item_combobox.bind("<<ComboboxSelected>>", lambda event: item_var.set(item_combobox.get()))
item_combobox.bind("<<ComboboxSelected>>", lambda event: item_combobox.config(completevalues=sorted([i['UniqueName'] for i in items.find()])))

# BUTTONS ---------------------
search_button = tk.Button(comparision_frame, text="Buscar", command=search)
search_button.pack(side=tk.TOP, padx=5)


# Mostrar la ventana principal
root.mainloop()