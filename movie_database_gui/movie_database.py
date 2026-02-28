# 1️⃣ IMPORTS
import json
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# 2️⃣ DATA STORAGE
movies = {}  # Dictionary to store all movie info

# 3️⃣ HELPER FUNCTIONS
def validate_year(year):
    """Check if year is valid (1800-2100)"""
    if not year.isdigit():
        return False
    return 1800 <= int(year) <= 2100

# 4️⃣ ADD MOVIE
def add_movie():
    title = simpledialog.askstring("Input", "Enter movie title:")
    if not title:
        return
    if title in movies:
        messagebox.showerror("Error", "Movie already exists!")
        return
    genre = simpledialog.askstring("Input", "Enter genre:")
    director = simpledialog.askstring("Input", "Enter director:")
    year = simpledialog.askstring("Input", "Enter release year:")
    actors = simpledialog.askstring("Input", "Enter actors (comma separated):")
    if not validate_year(year):
        messagebox.showerror("Error", "Invalid year format!")
        return
    movies[title] = {
        "year": int(year),
        "genre": genre,
        "director": director,
        "actors": [a.strip() for a in actors.split(",")]
    }
    messagebox.showinfo("Success", "Movie added successfully!")

# 5️⃣ EDIT MOVIE
def edit_movie():
    title = simpledialog.askstring("Edit", "Enter movie title to edit:")
    if title not in movies:
        messagebox.showerror("Error", "Movie not found!")
        return
    genre = simpledialog.askstring("Input", "Enter new genre:", initialvalue=movies[title]["genre"])
    director = simpledialog.askstring("Input", "Enter new director:", initialvalue=movies[title]["director"])
    year = simpledialog.askstring("Input", "Enter new release year:", initialvalue=str(movies[title]["year"]))
    actors = simpledialog.askstring("Input", "Enter new actors (comma separated):", initialvalue=", ".join(movies[title]["actors"]))
    if not validate_year(year):
        messagebox.showerror("Error", "Invalid year format!")
        return
    movies[title].update({
        "year": int(year),
        "genre": genre,
        "director": director,
        "actors": [a.strip() for a in actors.split(",")]
    })
    messagebox.showinfo("Success", "Movie updated successfully!")

# 6️⃣ DELETE MOVIE
def delete_movie():
    title = simpledialog.askstring("Delete", "Enter movie title to delete:")
    if title in movies:
        del movies[title]
        messagebox.showinfo("Success", "Movie deleted successfully!")
    else:
        messagebox.showerror("Error", "Movie not found!")

# 7️⃣ VIEW ALL MOVIES
def view_movies():
    if not movies:
        messagebox.showinfo("Movies", "No movies in database.")
        return
    result = ""
    for title, info in movies.items():
        result += f"\nTitle: {title}\n"
        for k, v in info.items():
            result += f"{k}: {v}\n"
        result += "-"*30 + "\n"
    messagebox.showinfo("Movie List", result)

# 8️⃣ SEARCH MOVIES
def search_movie():
    keyword = simpledialog.askstring("Search", "Enter title, genre, director, year or actor:")
    if not keyword:
        return
    results = ""
    for title, info in movies.items():
        if (keyword.lower() in title.lower() or
            keyword.lower() in info["genre"].lower() or
            keyword.lower() in info["director"].lower() or
            keyword == str(info["year"]) or
            any(keyword.lower() in actor.lower() for actor in info["actors"])):
            results += f"\nTitle: {title}\n"
            for k, v in info.items():
                results += f"{k}: {v}\n"
            results += "-"*30 + "\n"
    if results:
        messagebox.showinfo("Search Results", results)
    else:
        messagebox.showinfo("Search Results", "No matching movies found.")

# 9️⃣ SAVE DATA
def save_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".json")
    if file_path:
        with open(file_path, "w") as f:
            json.dump(movies, f)
        messagebox.showinfo("Success", "Data saved successfully!")

# 🔟 LOAD DATA
def load_data():
    global movies
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        try:
            with open(file_path, "r") as f:
                movies = json.load(f)
            messagebox.showinfo("Success", "Data loaded successfully!")
        except:
            messagebox.showerror("Error", "Failed to load file.")

# ----------------------------
# GUI SETUP (END)
# ----------------------------
root = tk.Tk()
root.title("Movie Database Management System")
root.geometry("400x400")

# Buttons
tk.Button(root, text="Add Movie", width=25, command=add_movie).pack(pady=5)
tk.Button(root, text="Edit Movie", width=25, command=edit_movie).pack(pady=5)
tk.Button(root, text="Delete Movie", width=25, command=delete_movie).pack(pady=5)
tk.Button(root, text="View All Movies", width=25, command=view_movies).pack(pady=5)
tk.Button(root, text="Search Movie", width=25, command=search_movie).pack(pady=5)
tk.Button(root, text="Save Data", width=25, command=save_data).pack(pady=5)
tk.Button(root, text="Load Data", width=25, command=load_data).pack(pady=5)
tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=5)

# Start GUI
root.mainloop()  # Keep the window running
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Program closed.")