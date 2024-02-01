from shop import Shop
import tkinter as tk

boucherie = Shop()

window = tk.Tk()
window.title("Boucherie")
window.geometry("1600x800")

info = ""

def read_all_products():
    global info

    clear()
    for f in boucherie.readProducts():
        info += f"\n ID : {f[0]} | Nom : {f[1]} | Description : {f[2]} | Prix : {f[3]} | Quantité : {f[4]} | ID-Catégorie : {f[5]}"
    label1.config(text=info)


def create_a_product():
    global info
    global canvas1

    clear()
    canvas1.pack()
    create_entry1 = tk.Entry(window)
    create_entry1.insert(0, "Nom")
    create_entry2 = tk.Entry(window)
    create_entry2.insert(0, "Description")
    create_entry3 = tk.Entry(window)
    create_entry3.insert(0, "Prix")
    create_entry4 = tk.Entry(window)
    create_entry4.insert(0, "Quantité")
    create_entry5 = tk.Entry(window)
    create_entry5.insert(0, "ID-Catégorie")
    
    canvas1.create_window(200, 140, window=create_entry1)
    canvas1.create_window(200, 160, window=create_entry2)
    canvas1.create_window(200, 180, window=create_entry3)
    canvas1.create_window(200, 200, window=create_entry4)
    canvas1.create_window(200, 220, window=create_entry5)

    buttonExecute = tk.Button(text='Ajouter', command=lambda: [boucherie.createProduct(create_entry1.get(), create_entry2.get(), create_entry3.get(), create_entry4.get(), create_entry5.get()), clear()])
    canvas1.create_window(200, 250, window=buttonExecute)

def update_a_product():
    global info
    global canvas1

    clear()
    canvas1.pack()
    update_entry1 = tk.Entry(window)
    update_entry1.insert(0, "ID")
    update_entry2 = tk.Entry(window)
    update_entry2.insert(0, "Prix")
    update_entry3 = tk.Entry(window)
    update_entry3.insert(0, "Quantité")
    canvas1.create_window(200, 140, window=update_entry1)
    canvas1.create_window(200, 160, window=update_entry2)
    canvas1.create_window(200, 180, window=update_entry3)
    buttonExecute = tk.Button(text='Modifier', command=lambda: [boucherie.updateProduct(update_entry1.get(), update_entry2.get(), update_entry3.get()), clear()])
    canvas1.create_window(200, 250, window=buttonExecute)

def delete_a_product():
    global info
    global canvas1

    clear()
    canvas1.pack()
    delete_entry1 = tk.Entry(window)
    delete_entry1.insert(0, "ID")
    canvas1.create_window(200, 140, window=delete_entry1)
    buttonExecute = tk.Button(text='Supprimer', command=lambda: [boucherie.deleteProduct(delete_entry1.get()), clear()])
    canvas1.create_window(200, 250, window=buttonExecute)

def clear():
    global canvas1
    global info

    canvas1.delete("all")
    label1.config(text="")
    info = ""

button1 = tk.Button(window, text="Afficher les produits", command= read_all_products)
button2 = tk.Button(window, text="Ajouter un produit", command= create_a_product)
button3 = tk.Button(window, text="Modifier un produit", command= update_a_product)
button4 = tk.Button(window, text="Supprimer un produit", command= delete_a_product)

label1 = tk.Label(window, text=info)
canvas1 = tk.Canvas(window, width=400, height=300)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

label1.pack()





window.mainloop()
