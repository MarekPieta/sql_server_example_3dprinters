from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox
import hashlib
from pyqt_app.CustomerWindow import CustomerWindow
from pyqt_app.AdminWindow import AdminWindow

class LoginWindow(QWidget):

    def __init__(self, db_connection):
        super().__init__()
        self.create_window()
        self.db_connection = db_connection

    def create_window(self):
        self.setGeometry(300, 300, 200, 160) #x, y, w, h
        self.setWindowTitle('3D Printers DB - Login Window')


        #Creating descriptions for text fields
        self.login_description = QLabel('Login:', self)
        self.password_description = QLabel('Password:', self)

        #Creating two text fields
        self.login_field = QLineEdit(self)
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)

        #Creagin push button
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login_button_click)


        self.grid = QGridLayout(self)
        self.grid.addWidget(self.login_description, 0, 0)
        self.grid.addWidget(self.password_description, 1, 0)
        self.grid.addWidget(self.login_field, 0, 1)
        self.grid.addWidget(self.password_field, 1, 1)
        self.grid.addWidget(self.login_button, 2, 1)

        self.show()

    def login_button_click(self):

        login = self.login_field.text()
        password = self.password_field.text()

        m = hashlib.sha512()
        m.update(password.encode())
        password_hash = m.hexdigest()

        if login == 'admin':
            if password == 'admin':
                self.admin_window = AdminWindow(self.db_connection)
                self.admin_window.show()
                self.destroy()
            else:
                popup = QMessageBox()
                popup.setIcon(QMessageBox.Critical)
                popup.setText("Invalid password")
                popup.setWindowTitle("Login error")
                popup.exec_()
        else:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT username, password_hash FROM customer WHERE username='" + login + "'")
            user_data = cursor.fetchone()
            if user_data is None:
                popup = QMessageBox()
                popup.setIcon(QMessageBox.Critical)
                popup.setText("Invalid login")
                popup.setWindowTitle("Login error")
                popup.exec_()
            else:

                if user_data.password_hash != password_hash:
                    popup = QMessageBox()
                    popup.setIcon(QMessageBox.Critical)
                    popup.setText("Invalid password")
                    popup.setWindowTitle("Login error")
                    popup.exec_()
                if user_data.password_hash == password_hash:
                    self.customer_window = CustomerWindow(self.db_connection, login)
                    self.customer_window.show()
                    self.destroy()