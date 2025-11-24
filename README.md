# ✅ TodoSavers 1.0

Modern, clean and ultra-simple task manager built with **CustomTkinter 5**.
Supports persistence, animations (CTk style), fast UX, scrollable task pane and JSON-based data storage.

---

## 📸 Preview

*(add your screenshots here)*

```
<img width="512" height="743" alt="Screen-UUID-HW0h8hH9808" src="https://github.com/user-attachments/assets/7cde15a5-9c48-42b0-b7c9-7658cfcf844a" />

```

---

# 🧩 Features

* ✔️ Add unlimited todos
* ✔️ Mark tasks as **Done / Undone**
* ✔️ Delete tasks
* ✔️ Auto-save to `.tdlist` custom file
* ✔️ Fully responsive minimalistic UI
* ✔️ Beautiful typography with CTkFont
* ✔️ Smooth list rebuilding
* ✔️ Smart JSON recovery (if corrupted)
* ✔️ Cross-platform (Windows / Linux / Mac)
* ✔️ Lightweight (single-file application)
* ✔️ Clean architecture

---

# 🛠 Installation

### 1. Install requirements

```sh
pip install customtkinter
```

### 2. Run the app

```sh
python main.py
```

---

# 📂 Project Structure

```
TodoSavers/
│
├── main.py
├── todos.tdlist
├── icon.ico             (optional)
└── README.md
```

---

# 🧠 How it Works (Deep Technical Explanation)

## 1. App Class

Main window inherits from `ctk.CTk`
Handles:

* init
* loading
* saving
* rebuilding UI
* closing event

## 2. Persistent Storage

File: `todos.tdlist`
Format: JSON array
Example:

```json
[
  {
    "task": "Finish homework",
    "done": false
  }
]
```

If file is missing → created automatically.
If broken → app resets safely.

## 3. UI Composition

### 💠 Title Area

* Big title
* Small version label

### 💠 Input Box

* `CTkEntry`
* Press Enter → add task
* Press + button → add task

### 💠 List View

Scrollable container (`CTkScrollableFrame`) containing dynamic frames.

### 💠 Task Item Layout

```
[Checkbox] [Task Text……………………………………] [Delete]
```

### 💠 Color Logic

* Done → gray text + ✓ prefix
* Not done → white

---

# 🔧 Code Architecture (Full Explanation)

## add_todo()

* Reads input
* Trims text
* Appends dictionary
* Rebuilds UI
* Saves file

## toggle(i)

* toggles True/False
* rebuilds
* saves

## delete(i)

* pops index
* rebuilds
* saves

## update_list()

* Destroys all items
* Recreates frames dynamically
* Rebinds per-item actions

---

# 🚀 Roadmap (Planned Features)

### 🎯 Version 1.1

* Smooth fade animations
* Task categories
* Task priority levels (⭐ ⚠️ ❗)
* Colored labels

### 🎯 Version 1.2

* Drag & Drop task sorting
* Deadlines and reminders
* Dark/Light override

### 🎯 Version 2.0

* Cloud sync (Firebase or SQLite server)
* Mobile-style UI
* Export/Import todo lists
* Encryption mode (AES-256)
* Themes marketplace

---

# 🧪 Testing Specification

### Test #1 — Add Task

Steps:

1. Type text
2. Press Enter
3. UI updates
4. File written

Expected:

* Task appears
* todos.tdlist updated

### Test #2 — Mark as Done

Steps:

1. Click checkbox
2. Label turns gray
3. ✓ prefix added
4. JSON updated

### Test #3 — Delete

Expected:

* Item removed
* All other indexes re-bound

### Test #4 — Save on Close

* Close window
* Reopen
* Last state should load

---

# 📜 JSON File Format (Spec Document)

### Object Format

```
task: string
done: boolean
```

### Example file

```json
[
  {"task": "Wake up", "done": true},
  {"task": "Write code", "done": false}
]
```

### Validation Rules

* `task` must NOT be empty
* `done` must be boolean
* Corrupted file = reset

---

# 🎨 UI/UX Philosophy

TodoSavers uses **flat UI** + **soft shadows (CTk theme)**.
Designed to be distraction-free:

* No dialog boxes
* No popups
* Fast input UX
* Every action = instant list rebuild
* Minimal colors
* Maximum readability

---

# 🧩 Developer Notes

* CustomTkinter automatically adapts to system appearance
* The scroll frame rebuild is optimized
* Lambda closures correctly preserve index via `lambda i=i:`
* File operations are UTF-8 encoded

---

# 🧭 FAQ

### ❓ Where is the data saved?

In `todos.tdlist` inside the same folder.

### ❓ Does it work without icon.ico?

Yes — icon is optional.

### ❓ Can I move todos.tdlist elsewhere?

Yes, but you must update `self.file_path`.

### ❓ Can I pack this into EXE?

Yes.
Use:

```
pyinstaller --onefile --noconsole main.py
```

---

# 📝 Changelog

## v1.0

* Initial release
* Full UI
* JSON storage
* Scrollable list
* Checkboxes
* Delete system

---

# ⭐ Credits

Created by **saba developer** 🎉
Thanks to CustomTkinter developers for such a clean UI framework.

---

# 📃 License

MIT License
Free for personal & commercial use.

---

# ❤️ Support

If you enjoy this project:

* ⭐ Star the repository
* 🔱 Fork and contribute
* 🐛 Report issues
