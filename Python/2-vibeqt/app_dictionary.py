import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PyQt6.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    """
    Main application window that encapsulates all UI elements and functionality.
    """
    def __init__(self):
        """
        Initializes the main window, UI, and connects signals.
        """
        super().__init__()

        self.setWindowTitle("JGlossator")
        self.setFixedSize(650, 488)

        # --- Central Widget and Layouts ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        bottom_widget = QWidget()
        bottom_layout = QHBoxLayout(bottom_widget)

        # --- Create Widgets ---
        self.main_text_edit = QTextEdit()
        self.main_text_edit.setReadOnly(True)

        bottom_left_text_edit = QTextEdit()
        bottom_left_text_edit.setReadOnly(True)
        bottom_left_text_edit.setFixedHeight(120)

        bottom_right_text_edit = QTextEdit()
        bottom_right_text_edit.setReadOnly(True)
        bottom_right_text_edit.setFixedHeight(120)

        # --- Assemble Layouts ---
        bottom_layout.addWidget(bottom_left_text_edit, 1)
        bottom_layout.addWidget(bottom_right_text_edit, 1)
        main_layout.addWidget(self.main_text_edit, 1)
        main_layout.addWidget(bottom_widget, 0)
        
        # --- Set static HTML content for bottom panels ---
        self.set_static_content(bottom_left_text_edit, bottom_right_text_edit)

        # --- Connect Clipboard Signal ---
        # Get the application's clipboard instance
        clipboard = QApplication.clipboard()
        # Connect its dataChanged signal to our update function (slot)
        clipboard.dataChanged.connect(self.update_text_from_clipboard)

        # --- Initial text load ---
        # Perform an initial update when the application starts
        self.update_text_from_clipboard()

    @pyqtSlot()
    def update_text_from_clipboard(self):
        """
        This function (slot) is called whenever the clipboard's
        dataChanged signal is emitted.
        """
        clipboard = QApplication.clipboard()
        clipboard_text = clipboard.text()

        # Use a default message if the clipboard is empty
        if not clipboard_text:
            clipboard_text = "Clipboard is empty. Copy some text."

        # Note: The detailed analysis below the heading is static and will not
        # change with the clipboard content. We add a note for the user.
        self.main_text_edit.setHtml(f"""
            <body style="color: #e0e0e0; font-family: 'MS Shell Dlg 2', Arial, sans-serif; font-size: 11px;">
                <h1 style="font-size: 23px; color: #50fa7b; margin-bottom: 2px;">{clipboard_text}</h1>
                <p style="font-size: 13px; color: #bd93f9; margin-top: 0px; margin-bottom: 15px;"><i>(Analysis below is static and does not update)</i></p>

                <div style="margin-bottom: 15px;">
                    <p style="font-size: 15px; color: #f8f8f2; margin-bottom: 3px;">
                        昨日 <span style="color: #bd93f9;">きのう、さくじつ</span> <span style="color: #8be9fd;">2880</span>
                        <span style="background-color: #44475a; color: #ffb86c; padding: 1px 4px; border-radius: 3px; font-size: 10px;">EDICT</span>
                    </p>
                    <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 5px;">(n-adv, n-t) yesterday. (P)</p>
                </div>

                <div style="margin-bottom: 15px;">
                    <p style="font-size: 15px; color: #f8f8f2; margin-bottom: 3px;">
                        すき焼き <span style="color: #bd93f9;">すきやき</span> <span style="color: #8be9fd;">048007</span>
                        <span style="background-color: #44475a; color: #ffb86c; padding: 1px 4px; border-radius: 3px; font-size: 10px;">EDICT</span>
                    </p>
                    <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 5px;">(n) (food) sukiyaki, thin slices of beef... (P)</p>
                </div>

                <div>
                    <p style="font-size: 15px; color: #f8f8f2; margin-bottom: 3px;">
                        食べる <span style="color: #bd93f9;">たべる</span> <span style="color: #8be9fd;">2392</span> (polite past)
                        <span style="background-color: #44475a; color: #ffb86c; padding: 1px 4px; border-radius: 3px; font-size: 10px;">EDICT</span>
                    </p>
                    <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 5px;">(v1,vt) to eat... (P)</p>
                </div>
            </body>
        """)

    def set_static_content(self, left_panel, right_panel):
        """
        Sets the HTML for the non-changing bottom panels.
        """
        left_panel.setHtml("""
            <body style="color: #e0e0e0; font-family: 'MS Shell Dlg 2', Arial, sans-serif; font-size: 11px;">
                <p style="font-size: 12px; color: #ff79c6; margin-bottom: 2px;">昨 <span style="color: #8be9fd;">226 ワク</span></p>
                <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 8px;">昨日 <span style="color: #bd93f9;">1140</span></p>
                <hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
                <p style="color: #f1fa8c; margin-top: 0px;">yesterday, previous</p>
                <br>
                <p style="font-size: 12px; color: #ff79c6; margin-bottom: 2px;">日 <span style="color: #8be9fd;">1</span></p>
                <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 2px;">12</p>
                <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 8px;">ニチ、ジッ、ひ、-び、-か</p>
                <hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
                <p style="color: #f1fa8c; margin-top: 0px;">day, sun, Japan, counter for days</p>
            </body>
        """)
        right_panel.setHtml("""
            <body style="color: #e0e0e0; font-family: 'MS Shell Dlg 2', Arial, sans-serif; font-size: 11px;">
                <p style="font-size: 12px; color: #ff79c6; margin-bottom: 2px;">焼 <span style="color: #8be9fd;">1200 カ 982 ショウ</span></p>
                <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 8px;">やける</p>
                <hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
                <p style="color: #f1fa8c; margin-top: 0px;">bake, burning</p>
                <br>
                <p style="font-size: 12px; color: #ff79c6; margin-bottom: 2px;">食 <span style="color: #8be9fd;">328 ショク、ジキ</span></p>
                <p style="color: #f8f8f2; margin-top: 0px; margin-bottom: 2px;">く(う)、た(べる) <span style="color: #bd93f9;">1472</span></p>
                <hr style="border: 0; border-top: 1px solid #6272a4; margin-bottom: 8px;">
                <p style="color: #f1fa8c; margin-top: 0px;">eat, food</p>
            </body>
        """)

def main():
    """
    Creates and runs the application.
    """
    app = QApplication(sys.argv)
    
    # Apply stylesheet to the entire application for consistency
    app.setStyleSheet("""
        QMainWindow, QWidget {
            background-color: #282a36;
        }
        QTextEdit {
            background-color: #282a36;
            color: #f8f8f2;
            border: 1px solid #44475a;
            font-family: "MS Shell Dlg 2", "Arial", sans-serif;
            font-size: 11px;
            padding: 8px;
        }
        QScrollBar:vertical {
            border: 1px solid #1e1f29; background: #1e1f29;
            width: 15px; margin: 15px 0 15px 0;
        }
        QScrollBar::handle:vertical {
            background: #44475a; min-height: 20px; border-radius: 7px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none; background: none; height: 14px;
            subcontrol-position: top; subcontrol-origin: margin;
        }
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        QScrollBar:horizontal {
            border: 1px solid #1e1f29; background: #1e1f29;
            height: 15px; margin: 0 15px 0 15px;
        }
        QScrollBar::handle:horizontal {
            background: #44475a; min-width: 20px; border-radius: 7px;
        }
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none; background: none; width: 14px;
            subcontrol-position: left; subcontrol-origin: margin;
        }
        QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal,
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }
    """)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()