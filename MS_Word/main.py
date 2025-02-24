from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class BSWord(QMainWindow):
    def __init__(self, parent=None, flags=...):
        super(BSWord, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.editor.setFontPointSize(20)
        self.font_size_box = QSpinBox()
        self.create_tool_bar()

    def create_tool_bar(self):
        toolBar = QToolBar()
        
        # Undo Action
        undo_action = QAction(QIcon('BS_Word/undo.png'), 'Undo', self)
        undo_action.triggered.connect(self.editor.undo)
        toolBar.addAction(undo_action)

        # Redo Action
        redo_action = QAction(QIcon('BS_Word/redo.png'), 'Redo', self)
        redo_action.triggered.connect(self.editor.redo)
        toolBar.addAction(redo_action)

        # Cut Action
        cut_action = QAction(QIcon('BS_Word/cut.png'), 'Cut', self)
        cut_action.triggered.connect(self.editor.cut)
        toolBar.addAction(cut_action)

        # Copy Action
        copy_action = QAction(QIcon('BS_Word/copy.png'), 'Copy', self)
        copy_action.triggered.connect(self.editor.copy)
        toolBar.addAction(copy_action)

        # Paste Action
        paste_action = QAction(QIcon('BS_Word/paste.png'), 'Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        toolBar.addAction(paste_action)

        toolBar.addSeparator()

        # Font Size Selector
        self.font_size_box.valueChanged.connect(self.set_font_size)
        self.font_size_box.setValue(20)
        toolBar.addWidget(self.font_size_box)

        toolBar.addSeparator()

        # Save Action
        save_action = QAction(QIcon('BS_Word/save.png'), 'Save', self)
        save_action.triggered.connect(self.save_file)
        toolBar.addAction(save_action)

        self.addToolBar(toolBar)

    def set_font_size(self, size):
        self.editor.setFontPointSize(size)

    def save_file(self):
        """Opens a file dialog and saves the text editor content to a file."""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.editor.toPlainText())

app = QApplication(sys.argv)
window = BSWord()
window.show()
sys.exit(app.exec_())
