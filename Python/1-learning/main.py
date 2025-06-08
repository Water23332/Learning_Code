import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QLabel

# Assigning values to variables
name: str = "Alice"  # A string
age: int = 30       # An integer
height: float = 5.5   # A float
is_student: bool = True # A boolean


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A window title")
        self.setFixedSize(600, 700)

        label = QLabel(f"My name is {name}. Im {age} years old. I'm {height} foot tall. It's {is_student} that im a student.", self)
        label.setWordWrap(True)
        
        layout = QHBoxLayout()
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    
    window = MainWindow()  # Create the main window
    window.show()  # Display the window
    
    sys.exit(app.exec())  # Start the event loop