import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class DataPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Selection Page")
        self.setGeometry(100, 100, 700, 500)
        self.setStyleSheet("background-color: #2c3e50;")  # Dark background

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Select a Data Type")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #ecf0f1; margin: 20px;")

        # Data Boxes Layout
        box_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignCenter)

        self.data_outlet = self.create_box("Data Outlet", "#e74c3c")
        self.data_hider = self.create_box("Data Hider", "#f39c12")
        self.data_receiver = self.create_box("Data Receiver", "#3498db", width=250)

        top_layout.addWidget(self.data_outlet)
        top_layout.addWidget(self.data_hider)

        box_layout.addLayout(top_layout)
        box_layout.addWidget(self.data_receiver, alignment=Qt.AlignCenter)

        main_layout.addWidget(title)
        main_layout.addLayout(box_layout)

        self.setLayout(main_layout)

    def create_box(self, text, color, width=140, height=100):
        box = QFrame()
        box.setFrameShape(QFrame.StyledPanel)
        box.setStyleSheet(f"""
            QFrame {{
                border-radius: 15px;
                background-color: {color};
                color: white;
                padding: 10px;
                transition: 0.3s;
            }}
            QFrame:hover {{
                background-color: {self.darken_color(color, 0.8)};
            }}
        """)
        box.setFixedSize(width, height)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel(text)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("margin-top: 10px;")

        layout.addWidget(label)
        box.setLayout(layout)

        return box

    def darken_color(self, hex_color, factor):
        color = QColor(hex_color)
        color = color.darker(int(factor * 100))
        return color.name()

class MediaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Selection Page")
        self.setGeometry(100, 100, 700, 500)
        self.setStyleSheet("background-color: #2c3e50;")  # Dark background

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Select a Media Type")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #ecf0f1; margin: 20px;")

        # Upper row (Image & Audio)
        upper_layout = QHBoxLayout()
        upper_layout.setAlignment(Qt.AlignCenter)

        self.image_box = self.create_box("Alphabet", "#e74c3c")
        self.image_box.mousePressEvent = self.open_data_page  # Click event
        self.audio_box = self.create_box("Word", "#f39c12")
        self.audio_box.mousePressEvent = self.word_page
        upper_layout.addWidget(self.image_box)
        upper_layout.addWidget(self.audio_box)

        

        # Adding layouts to main layout
        main_layout.addWidget(title)
        main_layout.addLayout(upper_layout)
        

        self.setLayout(main_layout)

    def create_box(self, text, color, width=240, height=100):
        box = QFrame()
        box.setFrameShape(QFrame.StyledPanel)
        box.setStyleSheet(f"""
           QFrame {{
                border-radius: 15px;
                background-color: {color};
                color: white;
                padding: 10px;
                transition: 0.3s;
            }}
            QFrame:hover {{
                background-color: {self.darken_color(color, 0.8)};
            }}
        """)
        box.setFixedSize(width, height)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel(text)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("margin-top: 10px;")

        layout.addWidget(label)
        box.setLayout(layout)

        return box

    def darken_color(self, hex_color, factor):
        color = QColor(hex_color)
        color = color.darker(int(factor * 100))
        return color.name()

    def open_data_page(self, event):
        from slr import main
        main()
    def word_page(self,event):
        import subprocess
        python_path = r"C:\Users\SONALI\.conda\envs\sign\python.exe"
        script_path = r"D:\\Sign-Language-Recognition-master\test.py"
        subprocess.run(f'"{python_path}" "{script_path}"', shell=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaPage()
    window.show()
    sys.exit(app.exec_())
