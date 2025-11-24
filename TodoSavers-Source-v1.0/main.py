import customtkinter as ctk
import json
import os

# ==================== APP CONFIG ====================
ctk.set_appearance_mode("system")      # "dark", "light", "system"
ctk.set_default_color_theme("blue")    # ძალიან ლამაზია "green" და "dark-blue"აც

class TodoSavers(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ===== Window Settings =====
        self.title("TodoSavers 1.0")                    # ← შენი სურვილისამებრ
        self.geometry("500x700")
        self.minsize(400, 600)
        
        # App icon (თუ გაქვს icon.ico ფაილი საქაღალდეში)
        if os.path.exists("icon.ico"):
            self.iconbitmap("icon.ico")

        # ===== Data =====
        self.file_path = "todos.tdlist"
        self.todos = self.load_todos()

        # ===== UI =====
        self.create_widgets()
        self.update_list()

        # Save on close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        # Title
        title = ctk.CTkLabel(
            self,
            text="TodoSavers",
            font=ctk.CTkFont(size=36, weight="bold")
        )
        title.pack(pady=25)

        version = ctk.CTkLabel(
            self,
            text="v1.0",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        version.pack(pady=(0, 20))

        # Input frame
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, padx=40, fill="x")

        self.entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="What needs to be done?",
            height=45,
            font=ctk.CTkFont(size=15)
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(15, 8), pady=12)
        self.entry.bind("<Return>", lambda e: self.add_todo())

        add_btn = ctk.CTkButton(
            input_frame,
            text="+",
            width=55,
            height=45,
            font=ctk.CTkFont(size=28, weight="bold"),
            command=self.add_todo
        )
        add_btn.pack(side="right", padx=(8, 15), pady=12)

        # Task list
        self.listbox = ctk.CTkScrollableFrame(self)
        self.listbox.pack(pady=25, padx=40, fill="both", expand=True)

    def load_todos(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_todos(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)

    def add_todo(self):
        task = self.entry.get().strip()
        if task:
            self.todos.append({"task": task, "done": False})
            self.entry.delete(0, "end")
            self.update_list()
            self.save_todos()

    def toggle(self, idx):
        self.todos[idx]["done"] = not self.todos[idx]["done"]
        self.update_list()
        self.save_todos()

    def delete(self, idx):
        self.todos.pop(idx)
        self.update_list()
        self.save_todos()

    def update_list(self):
        for widget in self.listbox.winfo_children():
            widget.destroy()

        for i, todo in enumerate(self.todos):
            frame = ctk.CTkFrame(self.listbox)
            frame.pack(fill="x", pady=5, padx=8)

            # Checkbox
            cb = ctk.CTkCheckBox(
                frame,
                text="",
                width=30,
                command=lambda i=i: self.toggle(i)
            )
            cb.pack(side="left", padx=12, pady=10)
            if todo["done"]:
                cb.select()

            # Task label
            label_text = ("✓ " + todo["task"]) if todo["done"] else todo["task"]
            label = ctk.CTkLabel(
                frame,
                text=label_text,
                font=ctk.CTkFont(size=16),
                anchor="w",
                text_color="#888888" if todo["done"] else "white"
            )
            label.pack(side="left", fill="x", expand=True, padx=10, pady=10)

            # Delete button
            delete_btn = ctk.CTkButton(
                frame,
                text="Delete",
                width=40,
                fg_color="transparent",
                hover_color="#e74c3c",
                text_color="#e74c3c",
                command=lambda i=i: self.delete(i)
            )
            delete_btn.pack(side="right", padx=12, pady=8)

    def on_close(self):
        self.save_todos()
        self.destroy()


if __name__ == "__main__":
    app = TodoSavers()
    app.mainloop()