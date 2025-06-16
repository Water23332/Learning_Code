# gui.py
import sys
import time
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt

class DictionaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Japanese Dictionary (SQLite + Go)")
        
        # Widgets
        self.input = QLineEdit(placeholderText="Enter a word (e.g., 猫 or ねこ)...")
        self.output = QLabel("Results appear here")
        self.time_label = QLabel("Time: 0 ms")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.output)
        layout.addWidget(self.time_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Signals
        self.input.returnPressed.connect(self.lookup_word)
    
    def lookup_word(self):
        word = self.input.text().strip()
        if not word:
            self.output.setText("Please enter a word!")
            return
        
        start_time = time.time()
        
        try:
            result = subprocess.run(
                ["./dicttool", word],
                capture_output=True,
                text=True,
                check=True
            )
            elapsed_ms = (time.time() - start_time) * 1000
            self.output.setText(result.stdout.strip())
            self.time_label.setText(f"Time: {elapsed_ms:.2f} ms")
            
        except subprocess.CalledProcessError as e:
            self.output.setText(e.stderr.strip() or "Word not found")
        except FileNotFoundError:
            self.output.setText("Error: Go binary './dicttool' not found")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionaryApp()
    window.show()
    app.exec()
