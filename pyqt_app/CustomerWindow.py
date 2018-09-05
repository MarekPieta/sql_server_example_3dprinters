from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox, QHBoxLayout,\
    QVBoxLayout, QSpacerItem, QDateEdit, QListWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
from random import randint
import hashlib

class CustomerWindow(QWidget):

    def __init__(self, db_connection, customer_name):
        super().__init__()
        self.customer_name = customer_name
        self.db_connection = db_connection
        self.create_window()

    def create_window(self):
        self.setGeometry(300, 300, 600, 300) #x, y, w, h
        self.setWindowTitle('3D Printers DB - Logged as: ')

        self.main_layout = QHBoxLayout(self)
        self.create_menu()

        self.menu_spacer = QSpacerItem(40, 10)
        self.main_layout.addItem(self.menu_spacer)

        self.create_welcome_message_layout()
        self.create_customer_profile_layout()
        self.create_order_history_layout()
        self.create_make_order_layout()

    def hide_all(self):
        self.hide_welcome_message_layout()
        self.hide_customer_profile_layout()
        self.hide_make_order_layout()
        self.hide_order_history_layout()

    def create_menu(self):
        self.menu = QVBoxLayout(self)

        self.login_description = QLabel('Logged in as: ' + self.customer_name, self)
        font = QFont()
        font.setPixelSize(20)
        font.setBold(True)
        self.login_description.setFont(font)

        self.make_order_btn = QPushButton('Make order', self)
        self.order_history_btn = QPushButton('Order history', self)
        self.profile_btn = QPushButton('Profile', self)
        self.logout_btn = QPushButton('Logout and exit', self)

        self.make_order_btn.clicked.connect(self.make_oder_button_trigger)
        self.order_history_btn.clicked.connect(self.order_history_button_trigger)
        self.profile_btn.clicked.connect(self.profile_button_trigger)
        self.logout_btn.clicked.connect(self.logout_button_trigger)

        self.menu.addWidget(self.login_description)
        self.menu.addWidget(self.make_order_btn)
        self.menu.addWidget(self.order_history_btn)
        self.menu.addWidget(self.profile_btn)
        self.menu.addWidget(self.logout_btn)
        self.menu.addStretch()
        self.main_layout.addLayout(self.menu)

    def create_welcome_message_layout(self):
        self.welcome_message_layout = QVBoxLayout(self)

        self.welcome_message_font = QFont()
        self.welcome_message_font.setPixelSize(12)
        self.welcome_message_text = 'Welcome in Printer DB application.\nUse menu ' \
                                    'located on the left site of window for navigation.'
        self.welcome_message = QLabel(self.welcome_message_text)
        self.welcome_message.setFont(self.welcome_message_font)
        self.welcome_message_layout.addWidget(self.welcome_message)
        self.welcome_message_layout.addStretch()
        self.main_layout.addLayout(self.welcome_message_layout)

    def hide_welcome_message_layout(self):
        self.welcome_message.hide()

    def show_welcome_message_layout(self):
        self.welcome_message.show()

    def create_customer_profile_layout(self):
        self.customer_profile_grid = QGridLayout()
        self.customer_profile_layout = QVBoxLayout()

        self.customer_profile_info = QLabel('Profile: ', self)

        self.customer_profile_info_font = QFont()
        self.customer_profile_info_font.setPixelSize(16)
        self.customer_profile_info_font.setBold(True)
        self.customer_profile_info.setFont(self.customer_profile_info_font)

        self.customer_profile_layout.addWidget(self.customer_profile_info)

        self.password_label = QLabel('Password:', self)
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)

        self.first_name_label = QLabel('First name:', self)
        self.first_name_field = QLineEdit(self)

        self.last_name_label = QLabel('Last name:', self)
        self.last_name_field = QLineEdit(self)

        self.phone_label = QLabel('Phone number:', self)
        self.phone_field = QLineEdit(self)

        self.address_label = QLabel('Address:', self)
        self.address_field = QLineEdit(self)

        self.city_label = QLabel('City:', self)
        self.city_field = QLineEdit(self)

        self.loyalty_points_label = QLabel('Loyalty points:', self)
        self.loyalty_points_field = QLabel('numa', self)

        self.profile_change_button = QPushButton('Apply', self)
        self.profile_change_button.clicked.connect(self.apply_profile_change_button_trigger)

        self.customer_profile_grid.addWidget(self.password_label, 0, 0)
        self.customer_profile_grid.addWidget(self.password_field, 0, 1)
        self.customer_profile_grid.addWidget(self.first_name_label, 1, 0)
        self.customer_profile_grid.addWidget(self.first_name_field, 1, 1)
        self.customer_profile_grid.addWidget(self.last_name_label, 2, 0)
        self.customer_profile_grid.addWidget(self.last_name_field, 2, 1)
        self.customer_profile_grid.addWidget(self.phone_label, 3, 0)
        self.customer_profile_grid.addWidget(self.phone_field, 3, 1)
        self.customer_profile_grid.addWidget(self.address_label, 4, 0)
        self.customer_profile_grid.addWidget(self.address_field, 4, 1)
        self.customer_profile_grid.addWidget(self.city_label, 5, 0)
        self.customer_profile_grid.addWidget(self.city_field, 5, 1)
        self.customer_profile_grid.addWidget(self.first_name_label, 6, 0)
        self.customer_profile_grid.addWidget(self.first_name_field, 6, 1)
        self.customer_profile_grid.addWidget(self.loyalty_points_label, 7, 0)
        self.customer_profile_grid.addWidget(self.loyalty_points_field, 7, 1)
        self.customer_profile_grid.addWidget(self.profile_change_button, 8, 1)

        self.customer_profile_layout.addLayout(self.customer_profile_grid)
        self.customer_profile_layout.addStretch()
        self.main_layout.addLayout(self.customer_profile_layout)
        self.hide_customer_profile_layout()

    def hide_customer_profile_layout(self):
        self.customer_profile_info.hide()
        self.password_label.hide()
        self.password_field.hide()
        self.first_name_label.hide()
        self.first_name_field.hide()
        self.last_name_label.hide()
        self.last_name_field.hide()
        self.phone_label.hide()
        self.phone_field.hide()
        self.address_label.hide()
        self.address_field.hide()
        self.city_label.hide()
        self.city_field.hide()
        self.loyalty_points_label.hide()
        self.loyalty_points_field.hide()
        self.profile_change_button.hide()

    def show_customer_profile_layout(self):

        self.update_customer_profile_layout()

        self.customer_profile_info.show()
        self.password_label.show()
        self.password_field.show()
        self.first_name_label.show()
        self.first_name_field.show()
        self.last_name_label.show()
        self.last_name_field.show()
        self.phone_label.show()
        self.phone_field.show()
        self.address_label.show()
        self.address_field.show()
        self.city_label.show()
        self.city_field.show()
        self.loyalty_points_label.show()
        self.loyalty_points_field.show()
        self.profile_change_button.show()

    def update_customer_profile_layout(self):
        SQL_command = "SELECT * FROM customer WHERE username = '"
        SQL_command += self.customer_name + "'"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)

        res = cursor.fetchone()
        self.first_name_field.setText(res.first_name)
        self.last_name_field.setText(res.last_name)
        self.phone_field.setText(res.phone)
        self.address_field.setText(res.address)
        self.city_field.setText(res.city)
        self.loyalty_points_field.setText(str(res.loyalty_points))

    def create_make_order_layout(self):

        self.make_order_layout = QVBoxLayout(self)
        self.make_order_grid = QGridLayout()

        self.make_order_info = QLabel('Make an order: ', self)
        self.make_order_info_font = QFont()
        self.make_order_info_font.setPixelSize(16)
        self.make_order_info_font.setBold(True)

        self.make_order_info.setFont(self.customer_profile_info_font)
        self.make_order_layout.addWidget(self.make_order_info)

        self.due_date_label = QLabel('Due date:', self)
        self.due_date_field = QDateEdit(self)

        self.filename_label = QLabel('File: ', self)
        self.filename_field = QLineEdit(self)

        self.filament_type_label = QLabel('Filament type:', self)
        self.filament_type_field = QListWidget(self)
        self.filament_type_field.addItem('ABS')
        self.filament_type_field.addItem('PLA')

        self.filament_color_label = QLabel('Filament color:', self)
        self.filament_color_field = QListWidget(self)
        self.filament_color_field.addItem('red')
        self.filament_color_field.addItem('green')
        self.filament_color_field.addItem('blue')
        self.filament_color_field.addItem('black')
        self.filament_color_field.addItem('white')
        self.filament_color_field.addItem('yellow')
        self.filament_color_field.addItem('pink')

        self.make_order_apply_button = QPushButton('Make order', self)
        self.make_order_apply_button.clicked.connect(self.apply_make_order_button_trigger)


        self.make_order_grid.addWidget(self.due_date_label, 0, 0)
        self.make_order_grid.addWidget(self.due_date_field, 0, 1)
        self.make_order_grid.addWidget(self.filename_label, 1, 0)
        self.make_order_grid.addWidget(self.filename_field, 1, 1)
        self.make_order_grid.addWidget(self.filament_type_label, 2, 0)
        self.make_order_grid.addWidget(self.filament_type_field, 2, 1)
        self.make_order_grid.addWidget(self.filament_color_label, 3, 0)
        self.make_order_grid.addWidget(self.filament_color_field, 3, 1)
        self.make_order_grid.addWidget(self.make_order_apply_button, 4, 1)

        self.make_order_layout.addLayout(self.make_order_grid)
        self.make_order_layout.addStretch()
        self.main_layout.addLayout(self.make_order_layout)
        self.hide_make_order_layout()

    def hide_make_order_layout(self):
        self.make_order_info.hide()
        self.due_date_label.hide()
        self.due_date_field.hide()
        self.filename_label.hide()
        self.filename_field.hide()
        self.filament_type_label.hide()
        self.filament_type_field.hide()
        self.filament_color_label.hide()
        self.filament_color_field.hide()
        self.make_order_apply_button.hide()

    def show_make_order_layout(self):
        self.make_order_info.show()
        self.due_date_label.show()
        self.due_date_field.show()
        self.filename_label.show()
        self.filename_field.show()
        self.filament_type_label.show()
        self.filament_type_field.show()
        self.filament_color_label.show()
        self.filament_color_field.show()
        self.make_order_apply_button.show()

    def create_order_history_layout(self):
        self.order_history_layout = QVBoxLayout(self)
        self.order_history_info = QLabel('Order history: ', self)
        self.order_history_info_font = QFont()
        self.order_history_info_font.setPixelSize(16)
        self.order_history_info_font.setBold(True)

        self.order_history_info.setFont(self.customer_profile_info_font)
        self.order_history_layout.addWidget(self.order_history_info)

        self.order_history_table = QTableWidget(self)
        self.order_history_layout.addWidget(self.order_history_table)
        self.main_layout.addLayout(self.order_history_layout)
        self.order_history_table.setColumnCount(5)
        self.order_history_table.setHorizontalHeaderLabels(['Filename', 'Filament type', 'Filament color', 'Due date', 'Completed', 'Cost'])
        self.hide_order_history_layout()

    def hide_order_history_layout(self):
        self.order_history_info.hide()
        self.order_history_table.hide()

    def show_order_history_layout(self):
        self.update_order_history_layout()
        self.order_history_info.show()
        self.order_history_table.show()

    def update_order_history_layout(self):
        SQL_command = "SELECT stl_filename, filament_type, filament_color, due_date, completion_date, cost \
        FROM customer JOIN print_3d ON customer.username = print_3d.customer_username \
        WHERE customer.username = '"
        SQL_command += self.customer_name + "'"
        SQL_command += "ORDER BY due_date"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()
        self.order_history = []

        while res is not None:
            self.order_history.append(res)
            res = cursor.fetchone()
        self.order_history_table.setRowCount(len(self.order_history))
        for i in range(0, len(self.order_history)):
            self.order_history_table.setItem(i, 0, QTableWidgetItem(self.order_history[i].stl_filename))
            self.order_history_table.setItem(i, 1, QTableWidgetItem(self.order_history[i].filament_type))
            self.order_history_table.setItem(i, 2, QTableWidgetItem(self.order_history[i].filament_color))
            self.order_history_table.setItem(i, 3, QTableWidgetItem(str(self.order_history[i].due_date)[0:10]))

            if self.order_history[i].completion_date is not None:
                completion = 'Yes'
            else:
                completion = 'Not'
            self.order_history_table.setItem(i, 4, QTableWidgetItem(completion))
            self.order_history_table.setItem(i, 5, QTableWidgetItem(str(self.order_history[i].cost)))


    def order_history_button_trigger(self):
        self.hide_all()
        self.show_order_history_layout()

    def make_oder_button_trigger(self):
        self.hide_all()
        self.show_make_order_layout()

    def apply_make_order_button_trigger(self):
        due_date = self.due_date_field.date()
        due_date = due_date.toPyDate()
        filename = self.filename_field.text()

        print_time = str(randint(0, 15)) + ':' + str(randint(0, 59))
        print_cost = str(randint(0, 50))

        if len(filename) == 0:
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Critical)
            popup.setText("Please insert model filename")
            popup.setWindowTitle("Error - no modelname")
            popup.exec_()
            return

        if self.filament_type_field.currentItem() is None:
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Critical)
            popup.setText("Please select filament type")
            popup.setWindowTitle("Error - no filament type")
            popup.exec_()
            return
        filament_type = self.filament_type_field.currentItem().text()
        if self.filament_color_field.currentItem() is None:
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Critical)
            popup.setText("Please select filament color")
            popup.setWindowTitle("Error - no filament color")
            popup.exec_()
            return
        filament_color = self.filament_color_field.currentItem().text()
        SQL_command = "INSERT INTO print_3d (printer_id, customer_username, due_date, completion_date," \
                      " estimated_printing_time, stl_filename, cost, filament_type, filament_color) " \
                      "VALUES(NULL, '"
        SQL_command += self.customer_name + "', '"
        SQL_command += str(due_date) + "', NULL, '"
        SQL_command += print_time + "', '"
        SQL_command += filename + "', "
        SQL_command += print_cost + ", '"
        SQL_command += filament_type + "', '"
        SQL_command += filament_color + "');"

        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        self.db_connection.commit()
        popup = QMessageBox()
        popup.setIcon(QMessageBox.Information)
        popup.setText("Successfully made an order")
        popup.setWindowTitle("Order sent")
        popup.exec_()

    def profile_button_trigger(self):
        self.hide_all()
        self.show_customer_profile_layout()

    def apply_profile_change_button_trigger(self):
        change = False

        SQL_command = 'UPDATE customer SET '

        if len(self.password_field.text()) != 0:
            password = self.password_field.text()
            m = hashlib.sha512()
            m.update(password.encode())
            password_hash = m.hexdigest()
            SQL_command += "password_hash = '"
            SQL_command += password_hash + "', "

        if len(self.first_name_field.text()) != 0:
            SQL_command += "first_name = '"
            SQL_command += self.first_name_field.text() + "', "

            change = True

        if len(self.last_name_field.text()) != 0:
            SQL_command += "last_name = '"
            SQL_command += self.last_name_field.text() + "', "
            change = True

        if len(self.phone_field.text()) == 9:
            SQL_command += "phone = '"
            SQL_command += self.phone_field.text() + "', "
            change = True

        if len(self.address_field.text()) != 0:
            SQL_command += "address = '"
            SQL_command += self.address_field.text() + "', "
            change = True

        if len(self.city_field.text()) != 0:
            SQL_command += "city = '"
            SQL_command += self.city_field.text() + "', "
            change = True

        SQL_command = SQL_command[:-2]

        SQL_command += 'WHERE username = '
        SQL_command += "'" + self.customer_name + "'"

        if change == True:
            cursor = self.db_connection.cursor()
            cursor.execute(SQL_command)
            self.db_connection.commit()
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Information)
            popup.setText("Successfully applied changes to profile")
            popup.setWindowTitle("Profile Updated")
            popup.exec_()

    def logout_button_trigger(self):
        self.destroy()
        exit(0)