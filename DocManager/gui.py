import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Liste zum Speichern der Dokumentinformationen
documents = []

def upload_document():
    """Funktion zum Hochladen eines Dokuments."""
    file_path = filedialog.askopenfilename()
    if file_path:
        document_name = file_path.split('/')[-1]
        description = simpledialog.askstring("Beschreibung", "Gib eine Beschreibung für das Dokument ein:")
        documents.append({"name": document_name, "path": file_path, "description": description or "Keine Beschreibung"})
        messagebox.showinfo("Erfolg", f"Dokument '{document_name}' hochgeladen.")
        update_listbox()

def update_listbox():
    """Aktualisiere die Liste der hochgeladenen Dokumente."""
    listbox.delete(0, tk.END)
    for doc in documents:
        listbox.insert(tk.END, doc["name"])

def show_document_details():
    """Zeige die Details des ausgewählten Dokuments an."""
    selected_index = listbox.curselection()
    if selected_index:
        doc = documents[selected_index[0]]
        details = f"Name: {doc['name']}\nPfad: {doc['path']}\nBeschreibung: {doc['description']}"
        messagebox.showinfo("Dokument Details", details)

def delete_document():
    """Lösche das ausgewählte Dokument aus der Liste."""
    selected_index = listbox.curselection()
    if selected_index:
        documents.pop(selected_index[0])
        update_listbox()
        messagebox.showinfo("Erfolg", "Dokument gelöscht.")

def search_document():
    """Suche nach einem Dokument basierend auf dem Namen."""
    query = search_entry.get()
    results = [doc for doc in documents if query.lower() in doc["name"].lower()]
    
    listbox.delete(0, tk.END)
    for doc in results:
        listbox.insert(tk.END, doc["name"])

def reset_listbox():
    """Setzt die Dokumentenliste zurück."""
    update_listbox()

def start_gui():
    """Startet die grafische Benutzeroberfläche."""
    global listbox, search_entry
    window = tk.Tk()
    window.title("Dokumentenverwaltung")

    # Dokument hochladen
    upload_button = tk.Button(window, text="Dokument hochladen", command=upload_document)
    upload_button.pack(pady=10)

    # Dokument löschen
    delete_button = tk.Button(window, text="Dokument löschen", command=delete_document)
    delete_button.pack(pady=10)

    # Dokumentenliste
    listbox = tk.Listbox(window, width=50, height=10)
    listbox.pack(pady=10)

    # Dokumentendetails anzeigen
    details_button = tk.Button(window, text="Details anzeigen", command=show_document_details)
    details_button.pack(pady=10)

    # Suchfeld
    search_frame = tk.Frame(window)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Dokument suchen:")
    search_label.pack(side=tk.LEFT)

    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT)

    search_button = tk.Button(search_frame, text="Suchen", command=search_document)
    search_button.pack(side=tk.LEFT)

    reset_button = tk.Button(search_frame, text="Zurücksetzen", command=reset_listbox)
    reset_button.pack(side=tk.LEFT)

    update_listbox()
    window.mainloop()

if __name__ == "__main__":
    start_gui()
