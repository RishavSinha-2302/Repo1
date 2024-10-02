import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtGui import (QFont, QDesktopServices)
from PyQt5.QtCore import (Qt, QUrl)

class ImageEnhancerUI(QWidget):
    
    def enhance_image(self):
            # Get the image path from the text box
            image_path = self.url_input.text()
            img = cv2.imread(image_path)

            # Create sharpening kernel
            kernel = np.array([[0, -1, 0], 
                               [-1, 5, -1], 
                               [0, -1, 0]])

            # Apply the sharpening filter to the color image
            sharpened_img = cv2.filter2D(img, -1, kernel)

            # Convert BGR to RGB for displaying in matplotlib
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            sharpened_img_rgb = cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB)

            # Display the original and sharpened images
            plt.subplot(1, 2, 1)
            plt.imshow(img_rgb)
            plt.title('Original Image')
            plt.subplot(1, 2, 2)
            plt.imshow(sharpened_img_rgb)
            plt.title('Sharpened Image')

            plt.show()

    def clear_input(self):
            # Code to clear the input
            self.url_input.clear()
    
    def open_website(self):
        url = QUrl("https://www.youtube.com/watch?v=LCo69MDCGMs")
        QDesktopServices.openUrl(url)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Enhancer")
        self.setStyleSheet("background-color: #fffac3;")  # Set background

        # Title
        self.title_label = QLabel("Image Enhancer")
        self.title_label.setFont(QFont("Spicy Rice", 24))  # Use a bolder font
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            background-color: #5ec4ff; 
            border-radius: 16px; 
            color: #000000; 
            padding: 10px;""")

        # Subtitle
        self.subtitle_label = QLabel("Enhance and Sharpen Your Images Instantly")
        self.subtitle_label.setFont(QFont("Spicy Rice", 12))
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setStyleSheet("""
            background-color: #5ec4ff; 
            border-radius: 16px; 
            color: #000000; 
            padding: 5px;""")

        # Input Area (Orange Background)
        self.input_area = QWidget()
        self.input_area.setStyleSheet("background-color: #ffa500; border-radius: 30px; padding: 2px;")

        # Image URL Input
        self.url_label = QLabel("Enter Image URL:")
        self.url_label.setStyleSheet("color: #000000;")
        self.url_label.setFont(QFont("Spicy Rice", 12))
        self.url_input = QLineEdit("")
        self.url_input.setStyleSheet("border-radius: 30px; padding: 5px; border: 1px solid #cccccc;")
        self.url_input.setFont(QFont("Spicy Rice", 17))
        self.url_input.setFixedHeight(100)

        # Buttons
        self.enhance_button = QPushButton("Enhance Image")
        self.enhance_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #3e8e41; /* darker green on hover */
            }
            QPushButton:pressed {
                background-color: #0c5a0f; /* even darker green on click */
            }
        """)
        self.demo_button = QPushButton("Explanation")
        self.demo_button.setStyleSheet("""
            QPushButton {
                background-color: #5eadda; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #2995d3; /* darker blue on hover */
            }
            QPushButton:pressed {
                background-color: #144b6b; /* even darker blue on click */
            }
        """)
        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #d32f2f; /* darker red on hover */
            }
            QPushButton:pressed {
                background-color: #6d0d06; /* even darker red on click */
            }
        """)
        self.enhance_button.setFixedWidth(250)
        self.demo_button.setFixedWidth(250)
        self.clear_button.setFixedWidth(250)
        
        self.enhance_button.setFont(QFont("Spicy Rice", 10))
        self.demo_button.setFont(QFont("Spicy Rice", 10))
        self.clear_button.setFont(QFont("Spicy Rice", 10))

        self.enhance_button.setCursor(Qt.PointingHandCursor)
        self.demo_button.setCursor(Qt.PointingHandCursor)
        self.clear_button.setCursor(Qt.PointingHandCursor)

        self.enhance_button.clicked.connect(self.enhance_image)
        self.demo_button.clicked.connect(self.open_website)
        self.clear_button.clicked.connect(self.clear_input)
        
        # Layout
        title_layout = QVBoxLayout()
        title_layout.addWidget(self.title_label)
        title_layout.addWidget(self.subtitle_label)

        input_layout = QVBoxLayout(self.input_area)
        input_layout.addWidget(self.url_label)
        input_layout.addWidget(self.url_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.enhance_button)
        button_layout.addWidget(self.demo_button)
        button_layout.addWidget(self.clear_button)

        input_layout.addLayout(button_layout)
        
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(title_layout)
        
        # Add stretchable spacers to center the input area vertically
        main_layout.addStretch()
        main_layout.addWidget(self.input_area)
        main_layout.addStretch()

        # Footer
        self.footer_label = QLabel("Created for DM PBL Sem-1      2024-25")
        self.footer_label.setFont(QFont("Spicy Rice", 15))
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setStyleSheet(
            "border-radius: 16px; background-color: #333333; color: white; padding: 5px;"
        )
        self.footer_label.setFixedHeight(100)
        main_layout.addWidget(self.footer_label)

        # Set fixed height for the orange input area
        self.input_area.setFixedHeight(250)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEnhancerUI()
    window.show()
    sys.exit(app.exec_())