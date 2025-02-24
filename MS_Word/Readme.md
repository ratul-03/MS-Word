# BSWord - A Simple Text Editor

BSWord is a lightweight text editor built using **PyQt5**. It includes basic functionalities such as undo, redo, cut, copy, paste, font size adjustment, and file saving.

## Features
- **Undo & Redo**
- **Cut, Copy, Paste**
- **Adjustable Font Size**
- **Save File as .txt**
- **Simple & Clean UI**

## Installation

Ensure you have **Python 3** installed. Then, install the required dependencies:

```sh
pip install PyQt5
```

## Usage

Run the application using the following command:

```sh
python main.py
```

## File Structure
```
BSWord/
│── main.py          # Main application script
│── icons/           # Folder for toolbar icons
│   ├── undo.png
│   ├── redo.png
│   ├── cut.png
│   ├── copy.png
│   ├── paste.png
│   ├── save.png
└── README.md        # Project documentation
```

## How to Use
1. **Run** the script (`python main.py`).
2. **Type text** in the editor.
3. Use the toolbar to:
   - **Undo/Redo changes**
   - **Cut/Copy/Paste text**
   - **Change font size** using the spin box
   - **Save** the file by clicking the save button
4. **Choose a location** and save the file as `.txt`.

## Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes.

## License
This project is open-source under the **MIT License**.

---

**Made with ❤️ using PyQt5!**