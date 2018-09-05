from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox, QHBoxLayout,\
    QVBoxLayout, QSpacerItem, QDateEdit, QListWidget, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtGui import QFont
from decimal import *
import datetime
from dateutil.relativedelta import relativedelta


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class AdminWindow(QWidget):

    def __init__(self, db_connection):
        super().__init__()
        self.db_connection = db_connection
        self.create_window()

    def create_window(self):
        self.setGeometry(300, 300, 900, 450) #x, y, w, h
        self.setWindowTitle('3D Printers DB - Administrator ')

        self.main_layout = QHBoxLayout(self)

        self.create_menu()
        self.menu_spacer = QSpacerItem(40, 10)
        self.main_layout.addItem(self.menu_spacer)

        self.create_welcome_message_layout()
        self.create_assign_print_layout()
        self.create_what_is_printed_layout()
        self.create_finish_print_layout()
        self.create_customer_leaderboards_layout()
        self.create_earnings_statistics_layout()

    def create_menu(self):
        self.menu = QVBoxLayout(self)

        self.menu_description = QLabel('Administrator Window', self)
        font = QFont()
        font.setPixelSize(20)
        font.setBold(True)
        self.menu_description.setFont(font)

        self.finish_print_btn = QPushButton('Finish print', self)
        self.customer_leaderboards_btn = QPushButton('Customer leaderboards', self)
        self.assign_print_btn = QPushButton('Assign print', self)
        self.what_is_printed_btn = QPushButton('What is printed?', self)
        self.earnings_statisctics_btn = QPushButton('Earnings Statisctics', self)
        self.logout_btn = QPushButton('Logout and exit', self)

        #self.make_order_btn.clicked.connect(self.make_oder_button_trigger)
        #self.order_history_btn.clicked.connect(self.order_history_button_trigger)
        #self.profile_btn.clicked.connect(self.profile_button_trigger)
        self.logout_btn.clicked.connect(self.logout_button_trigger)
        self.assign_print_btn.clicked.connect(self.assign_print_button_trigger)
        self.what_is_printed_btn.clicked.connect(self.what_is_printed_button_trigger)
        self.finish_print_btn.clicked.connect(self.finish_print_button_trigger)
        self.customer_leaderboards_btn.clicked.connect(self.customer_leaderboards_button_trigger)
        self.earnings_statisctics_btn.clicked.connect(self.earnings_statistics_button_trigger)


        self.menu.addWidget(self.menu_description)
        self.menu.addWidget(self.what_is_printed_btn)
        self.menu.addWidget(self.assign_print_btn)
        self.menu.addWidget(self.finish_print_btn)
        self.menu.addWidget(self.customer_leaderboards_btn)
        self.menu.addWidget(self.earnings_statisctics_btn)
        self.menu.addWidget(self.logout_btn)
        self.menu.addStretch()
        self.main_layout.addLayout(self.menu)

    def create_welcome_message_layout(self):
        self.welcome_message_layout = QVBoxLayout(self)

        self.welcome_message_font = QFont()
        self.welcome_message_font.setPixelSize(12)
        self.welcome_message_text = 'Welcome in Printer DB application in admin mode.\nUse menu ' \
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

    def fill_print(self):
        self.print_field.clear()
        SQL_command = "SELECT id, stl_filename, due_date, filament_type, filament_color, \
         estimated_printing_time FROM print_3d \
         WHERE completion_date IS NULL \
         AND printer_id IS NULL \
         ORDER BY due_date;"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        self.prints_to_do = []
        res = cursor.fetchone()
        while res is not None:
            self.prints_to_do.append(res)
            self.print_field.addItem(str(res.id) + ', ' + res.stl_filename + ', ' + str(res.due_date)[0:9] +', ' + res.filament_type+', ' + res.filament_color)
            res = cursor.fetchone()

    def fill_printers(self):
        self.printer_field.clear()
        SQL_command = "SELECT printer_3d.id, manufacturer, model \
                    FROM printer_3d \
                    JOIN print_3d on printer_3d.id = print_3d.printer_id \
                    WHERE completion_date IS NULL"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()
        self.busy_printers = []

        while res is not None:
            self.busy_printers.append(res)
            res = cursor.fetchone()

        SQL_command = "SELECT printer_3d.id, manufacturer, model \
                            FROM printer_3d"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()
        self.all_printers = []
        while res is not None:
            self.all_printers.append(res)
            res = cursor.fetchone()

        free_printers = []
        for i in self.all_printers:
            if i not in self.busy_printers:
               free_printers.append(i)
               self.printer_field.addItem(str(i.id)  + ', ' + i.manufacturer + ' ' + i.model)

    def create_assign_print_layout(self):
        self.assign_print_layout = QVBoxLayout(self)
        self.assign_print_grid = QGridLayout()

        self.assign_print_info = QLabel('Assign print: ', self)
        self.assign_print_info_font = QFont()
        self.assign_print_info_font.setPixelSize(16)
        self.assign_print_info_font.setBold(True)

        self.assign_print_info.setFont(self.assign_print_info_font)
        self.assign_print_layout.addWidget(self.assign_print_info)

        self.printer_label = QLabel('Printer:', self)
        self.printer_field = QListWidget(self)

        self.print_label = QLabel('Print: ', self)
        self.print_field = QListWidget(self)

        self.assign_print_apply_button = QPushButton('Assign', self)
        self.assign_print_apply_button.clicked.connect(self.print_apply_button_trigger)

        self.assign_print_grid.addWidget(self.printer_label, 0, 0)
        self.assign_print_grid.addWidget(self.printer_field, 0, 1)
        self.assign_print_grid.addWidget(self.print_label, 1, 0)
        self.assign_print_grid.addWidget(self.print_field, 1, 1)
        self.assign_print_grid.addWidget(self.assign_print_apply_button, 2, 1)

        self.assign_print_layout.addLayout(self.assign_print_grid)
        self.assign_print_layout.addStretch()
        self.main_layout.addLayout(self.assign_print_layout)
        self.hide_assign_print_layout()

    def hide_assign_print_layout(self):
        self.assign_print_info.hide()
        self.printer_label.hide()
        self.printer_field.hide()
        self.print_label.hide()
        self.print_field.hide()
        self.assign_print_apply_button.hide()

    def show_assign_print_layout(self):
        self.fill_printers()
        self.fill_print()
        self.assign_print_info.show()
        self.printer_label.show()
        self.printer_field.show()
        self.print_label.show()
        self.print_field.show()
        self.assign_print_apply_button.show()

    def create_what_is_printed_layout(self):
        self.what_is_printed_layout = QVBoxLayout(self)
        self.what_is_printed_info = QLabel('What is currently printed: ', self)
        self.what_is_printed_info_font = QFont()
        self.what_is_printed_info_font.setPixelSize(16)
        self.what_is_printed_info_font.setBold(True)

        self.what_is_printed_info.setFont(self.what_is_printed_info_font)
        self.what_is_printed_layout.addWidget(self.what_is_printed_info)

        self.what_is_printed_table = QTableWidget(self)
        self.what_is_printed_layout.addWidget(self.what_is_printed_table)
        self.main_layout.addLayout(self.what_is_printed_layout)
        self.what_is_printed_table.setColumnCount(3)
        self.what_is_printed_table.setHorizontalHeaderLabels(['Printer', 'Filename', 'Customer name'])
        self.what_is_printed_layout.addWidget(self.what_is_printed_table)
        self.hide_what_is_printed_layout()

    def update_what_is_printed_layout(self):
        SQL_command = "SELECT printer_3d.id, manufacturer, model, stl_filename, customer_username \
                    FROM printer_3d \
                    JOIN print_3d on printer_3d.id = print_3d.printer_id \
                    WHERE completion_date IS NULL"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()
        self.busy_printers = []

        while res is not None:
            self.busy_printers.append(res)
            res = cursor.fetchone()
        self.what_is_printed_table.setRowCount(len(self.busy_printers))
        for i in range(0, len(self.busy_printers)):
            self.what_is_printed_table.setItem(i, 0, QTableWidgetItem(str(self.busy_printers[i].id) + ' ' +\
                                                                    self.busy_printers[i].manufacturer + ' ' + \
                                                                    self.busy_printers[i].model))
            self.what_is_printed_table.setItem(i, 1, QTableWidgetItem(self.busy_printers[i].stl_filename))
            self.what_is_printed_table.setItem(i, 2, QTableWidgetItem(self.busy_printers[i].customer_username))

    def show_what_is_printed_layout(self):
        self.update_what_is_printed_layout()
        self.what_is_printed_info.show()
        self.what_is_printed_table.show()

    def hide_what_is_printed_layout(self):
        self.what_is_printed_info.hide()
        self.what_is_printed_table.hide()

    def create_finish_print_layout(self):
        self.finish_print_layout = QVBoxLayout(self)

        self.finish_print_info = QLabel('Finish print: ', self)
        self.finish_print_info_font = QFont()
        self.finish_print_info_font.setPixelSize(16)
        self.finish_print_info_font.setBold(True)

        self.finish_print_info.setFont(self.finish_print_info_font)
        self.finish_print_layout.addWidget(self.finish_print_info)

        self.busy_printers_field = QListWidget(self)
        self.finish_print_layout.addWidget(self.busy_printers_field)
        self.finish_print_apply_button = QPushButton('Finish print', self)
        self.finish_print_apply_button.clicked.connect(self.finish_print_apply_button_trigger)


        self.finish_print_filo_layout = QHBoxLayout(self)
        self.finish_print_filo_layout_descriptions = QVBoxLayout(self)
        self.finish_print_filo_layout_select = QVBoxLayout(self)
        self.finish_print_filo_layout.addLayout(self.finish_print_filo_layout_descriptions)
        self.finish_print_filo_layout.addLayout(self.finish_print_filo_layout_select)

        self.finish_print_filo_manufacturer_description = QLabel('Filament manufacturer: ', self)
        self.finish_print_filo_diameter_description = QLabel('Filament diameter: ', self)
        self.finish_print_filo_type_description = QLabel('Filament type: ', self)
        self.finish_print_filo_color_description = QLabel('Filament color: ', self)
        self.finish_print_filo_amount_description = QLabel('Amount [gram]: ', self)


        self.finish_print_filo_layout_descriptions.addWidget(self.finish_print_filo_manufacturer_description)
        self.finish_print_filo_layout_descriptions.addWidget(self.finish_print_filo_diameter_description)
        self.finish_print_filo_layout_descriptions.addWidget(self.finish_print_filo_type_description)
        self.finish_print_filo_layout_descriptions.addWidget(self.finish_print_filo_color_description)
        self.finish_print_filo_layout_descriptions.addWidget(self.finish_print_filo_amount_description)

        self.finish_print_filo_manufacturer_select = QComboBox(self)
        self.finish_print_filo_diameter_select = QComboBox(self)
        self.finish_print_filo_type_select = QComboBox(self)
        self.finish_print_filo_color_select = QComboBox(self)
        self.finish_print_filo_amount_select = QLineEdit(self)

        self.finish_print_filo_layout_select.addWidget(self.finish_print_filo_manufacturer_select)
        self.finish_print_filo_layout_select.addWidget(self.finish_print_filo_diameter_select)
        self.finish_print_filo_layout_select.addWidget(self.finish_print_filo_type_select)
        self.finish_print_filo_layout_select.addWidget(self.finish_print_filo_color_select)
        self.finish_print_filo_layout_select.addWidget(self.finish_print_filo_amount_select)

        self.finish_print_layout.addLayout(self.finish_print_filo_layout)
        self.finish_print_layout.addWidget(self.finish_print_apply_button)
        self.main_layout.addLayout(self.finish_print_layout)

        self.hide_finish_print_layout()

    def find_filament_id(self, manufacturer, diameter, type, color):
        SQL_command = "select id FROM filament WHERE " + \
                    "manufacturer = '" + manufacturer +  "' AND " + \
                    "diameter = " + diameter +  " AND " + \
                    "color = '" + color + "' AND " + \
                    "type = '" + type + "'"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()
        if res is not None:
            return res.id
        else:
            return -1



    def update_finish_print_layout(self):
        self.busy_printers_field.clear()
        SQL_command = "SELECT printer_3d.id, manufacturer, model \
                            FROM printer_3d \
                            JOIN print_3d on printer_3d.id = print_3d.printer_id \
                            WHERE completion_date IS NULL AND printer_id IS NOT NULL"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()

        while res is not None:
            self.busy_printers_field.addItem(str(res.id) + ', ' + res.manufacturer + ' ' + res.model)
            res = cursor.fetchone()

        #clearing all fields
        self.finish_print_filo_manufacturer_select.clear()
        self.finish_print_filo_diameter_select.clear()
        self.finish_print_filo_type_select.clear()
        self.finish_print_filo_color_select.clear()
        self.finish_print_filo_amount_select.clear()

        SQL_command = "SELECT DISTINCT manufacturer FROM filament"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()

        while res is not None:
            self.finish_print_filo_manufacturer_select.addItem(res.manufacturer)
            res = cursor.fetchone()

        SQL_command = "SELECT DISTINCT diameter FROM filament"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()

        while res is not None:
            self.finish_print_filo_diameter_select.addItem(str(res.diameter))
            res = cursor.fetchone()

        SQL_command = "SELECT DISTINCT type FROM filament"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()

        while res is not None:
            self.finish_print_filo_type_select.addItem(res.type)
            res = cursor.fetchone()

        SQL_command = "SELECT DISTINCT color FROM filament"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()

        while res is not None:
            self.finish_print_filo_color_select.addItem(res.color)
            res = cursor.fetchone()


    def show_finish_print_layout(self):
        self.update_finish_print_layout()
        self.busy_printers_field.show()
        self.finish_print_info.show()
        self.finish_print_apply_button.show()
        self.finish_print_filo_manufacturer_description.show()
        self.finish_print_filo_diameter_description.show()
        self.finish_print_filo_type_description.show()
        self.finish_print_filo_color_description.show()
        self.finish_print_filo_manufacturer_select.show()
        self.finish_print_filo_diameter_select.show()
        self.finish_print_filo_type_select.show()
        self.finish_print_filo_color_select.show()
        self.finish_print_filo_amount_description.show()
        self.finish_print_filo_amount_select.show()


    def hide_finish_print_layout(self):
        self.busy_printers_field.hide()
        self.finish_print_info.hide()
        self.finish_print_apply_button.hide()
        self.finish_print_filo_manufacturer_description.hide()
        self.finish_print_filo_diameter_description.hide()
        self.finish_print_filo_type_description.hide()
        self.finish_print_filo_color_description.hide()
        self.finish_print_filo_manufacturer_select.hide()
        self.finish_print_filo_diameter_select.hide()
        self.finish_print_filo_type_select.hide()
        self.finish_print_filo_color_select.hide()
        self.finish_print_filo_amount_description.hide()
        self.finish_print_filo_amount_select.hide()


    def create_customer_leaderboards_layout(self):
        self.customer_leaderboards_layout = QVBoxLayout(self)
        self.customer_leaderboards_info = QLabel('Customer leaderboards: ', self)
        self.customer_leaderboards_info_font = QFont()
        self.customer_leaderboards_info_font.setPixelSize(16)
        self.customer_leaderboards_info_font.setBold(True)

        self.customer_leaderboards_info.setFont(self.customer_leaderboards_info_font)
        self.customer_leaderboards_layout.addWidget(self.customer_leaderboards_info)

        self.customer_leaderboards_table = QTableWidget(self)
        self.customer_leaderboards_layout.addWidget(self.customer_leaderboards_table)
        self.main_layout.addLayout(self.customer_leaderboards_layout)
        self.customer_leaderboards_table.setColumnCount(4)
        self.customer_leaderboards_table.setHorizontalHeaderLabels(['Username', 'First name', 'Last name', 'Loyalty points'])
        self.customer_leaderboards_layout.addWidget(self.customer_leaderboards_table)
        self.hide_customer_leaderboards_layout()

    def update_customer_leaderboards_layout(self):
        self.busy_printers_field.clear()
        SQL_command = "SELECT TOP 3 username, first_name, last_name, loyalty_points from customer order by loyalty_points DESC"
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        res = cursor.fetchone()
        customers = []
        while res is not None:
            customers.append(res)
            res = cursor.fetchone()
        self.customer_leaderboards_table.setRowCount(len(customers))
        for i in range(0, len(customers)):
            self.customer_leaderboards_table.setItem(i, 0, QTableWidgetItem(customers[i].username))
            self.customer_leaderboards_table.setItem(i, 1, QTableWidgetItem(customers[i].first_name))
            self.customer_leaderboards_table.setItem(i, 2, QTableWidgetItem(customers[i].last_name))
            self.customer_leaderboards_table.setItem(i, 3, QTableWidgetItem(str(customers[i].loyalty_points)))

    def show_customer_leaderboards_layout(self):
        self.update_customer_leaderboards_layout()
        self.customer_leaderboards_info.show()
        self.customer_leaderboards_table.show()

    def hide_customer_leaderboards_layout(self):
        self.customer_leaderboards_info.hide()
        self.customer_leaderboards_table.hide()

    def hide_all(self):
        self.hide_assign_print_layout()
        self.hide_what_is_printed_layout()
        self.hide_welcome_message_layout()
        self.hide_finish_print_layout()
        self.hide_customer_leaderboards_layout()
        self.hide_earnings_statistics_layout()

    def create_earnings_statistics_layout(self):
        self.earnings_statistics_layout = QVBoxLayout(self)

        self.main_layout.addLayout(self.earnings_statistics_layout)

        self.earnings_statistics_info = QLabel('Earnings Statistics: ', self)
        self.earnings_statistics_info_font = QFont()
        self.earnings_statistics_info_font.setPixelSize(16)
        self.earnings_statistics_info_font.setBold(True)
        self.earnings_statistics_info.setFont(self.earnings_statistics_info_font)
        self.earnings_statistics_layout.addWidget(self.earnings_statistics_info)

        self.earnings_statistics_selection_layout = QHBoxLayout(self)

        self.earnings_statistics_layout.addLayout(self.earnings_statistics_selection_layout)

        self.earnings_statistics_duration_info = QLabel('Statistics duration: ', self)
        self.earnings_statistics_duration_field = QComboBox(self)
        self.earnings_statistics_duration_field.addItem('1 Week')
        self.earnings_statistics_duration_field.addItem('1 Month')
        self.earnings_statistics_duration_field.addItem('1 Year')

        self.earnings_statistics_duration_field.currentIndexChanged.connect(self.update_earnings_plot)
        self.earnings_statistics_selection_layout.addWidget(self.earnings_statistics_duration_info)
        self.earnings_statistics_selection_layout.addWidget(self.earnings_statistics_duration_field)

        self.earnings_statistics_figure = Figure()
        self.earnings_statistics_canvas = FigureCanvas(self.earnings_statistics_figure)
        self.earnings_statistics_layout.addWidget(self.earnings_statistics_canvas)
        self.update_earnings_plot()

        self.hide_earnings_statistics_layout()

    def get_earnings_data_week(self):
        d = datetime.datetime.now()
        delta = datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        dates = []
        earnings = []
        xlabels = []

        for i in range(0, 7):
            dates.append(str(d).split('.')[0])
            d = d - delta
            xlabels.append(-i-1)

        for d in dates:
            SQL_command =  "SELECT SUM(cost) FROM print_3d WHERE completion_date < '" + d + "';"
            cursor = self.db_connection.cursor()
            cursor.execute(SQL_command)
            res = cursor.fetchone()
            if res is not None:
                if res[0] is not None:
                    earnings.append(res[0])
                else:
                    earnings.append(Decimal(0))
        return xlabels, earnings

    def get_earnings_data_month(self):
        d = datetime.datetime.now()
        delta = datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        dates = []
        earnings = []
        xlabels = []

        for i in range(0, 31):
            dates.append(str(d).split('.')[0])
            d = d - delta
            xlabels.append(-i-1)

        for d in dates:
            SQL_command = "SELECT SUM(cost) FROM print_3d WHERE completion_date < '" + d + "';"
            cursor = self.db_connection.cursor()
            cursor.execute(SQL_command)
            res = cursor.fetchone()
            if res is not None:
                if res[0] is not None:
                    earnings.append(res[0])
                else:
                    earnings.append(Decimal(0))
        return xlabels, earnings

    def get_earnings_data_year(self):
        d = datetime.datetime.now()
        delta = relativedelta(months=1)
        dates = []
        earnings = []
        xlabels = []

        for i in range(0, 12):
            dates.append(str(d).split('.')[0])
            d = d - delta
            xlabels.append(-i-1)

        for d in dates:
            SQL_command = "SELECT SUM(cost) FROM print_3d WHERE completion_date < '" + d + "';"
            cursor = self.db_connection.cursor()
            cursor.execute(SQL_command)
            res = cursor.fetchone()
            if res is not None:
                if res[0] is not None:
                    earnings.append(res[0])
                else:
                    earnings.append(Decimal(0))
        return xlabels, earnings

    def update_earnings_plot(self):
        if (str(self.earnings_statistics_duration_field.currentText())) == '1 Week':
            ''' plot some random stuff '''
            print('week')
            datax, datay = self.get_earnings_data_week()

            self.earnings_statistics_figure.clear()

            self.earnings_statiscitcs_subplot = self.earnings_statistics_figure.add_subplot(111)
            self.earnings_statiscitcs_subplot.clear()
            self.earnings_statiscitcs_subplot.grid(True)
            self.earnings_statiscitcs_subplot.set_xlabel('Day (from now)')
            self.earnings_statiscitcs_subplot.set_ylabel('Earnings [zl]')

            self.earnings_statiscitcs_subplot.plot(datax, datay, '*-')
            self.earnings_statistics_canvas.draw()

        if (str(self.earnings_statistics_duration_field.currentText())) == '1 Month':
            ''' plot some random stuff '''

            print('month')
            # random data
            datax, datay = self.get_earnings_data_month()

            self.earnings_statistics_figure.clear()

            self.earnings_statiscitcs_subplot = self.earnings_statistics_figure.add_subplot(111)
            self.earnings_statiscitcs_subplot.clear()
            self.earnings_statiscitcs_subplot.grid(True)
            self.earnings_statiscitcs_subplot.set_xlabel('Day (from now)')
            self.earnings_statiscitcs_subplot.set_ylabel('Earnings [zl]')

            self.earnings_statiscitcs_subplot.plot(datax, datay, '*-')
            self.earnings_statistics_canvas.draw()
        if (str(self.earnings_statistics_duration_field.currentText())) == '1 Year':
            ''' plot some random stuff '''

            datax, datay = self.get_earnings_data_year()

            self.earnings_statistics_figure.clear()

            self.earnings_statiscitcs_subplot = self.earnings_statistics_figure.add_subplot(111)
            self.earnings_statiscitcs_subplot.clear()
            self.earnings_statiscitcs_subplot.grid(True)
            self.earnings_statiscitcs_subplot.set_xlabel('Month (from now)')
            self.earnings_statiscitcs_subplot.set_ylabel('Earnings [zl]')
            print(self.earnings_statiscitcs_subplot.get_ylabel())

            self.earnings_statiscitcs_subplot.plot(datax, datay, '*-')
            self.earnings_statistics_canvas.draw()


    def show_earnings_statistics_layout(self):
        self.earnings_statistics_info.show()
        self.earnings_statistics_duration_info.show()
        self.earnings_statistics_duration_field.show()
        self.earnings_statistics_canvas.show()

    def hide_earnings_statistics_layout(self):
        self.earnings_statistics_info.hide()
        self.earnings_statistics_duration_info.hide()
        self.earnings_statistics_duration_field.hide()
        self.earnings_statistics_canvas.hide()

    def earnings_statistics_button_trigger(self):
        self.hide_all()
        self.show_earnings_statistics_layout()

    def print_apply_button_trigger(self):
        if self.printer_field.currentItem() is not None:
            printer_id = self.printer_field.currentItem().text().split(',')[0]
            if self.print_field.currentItem() is not None:
                print_id = self.print_field.currentItem().text().split(',')[0]
                SQL_command = "UPDATE print_3d SET printer_id = " + \
                                printer_id + " WHERE print_3d.id = " + \
                                print_id
                cursor = self.db_connection.cursor()
                cursor.execute(SQL_command)
                cursor.commit()
                self.hide_assign_print_layout()
                self.show_assign_print_layout()
                popup = QMessageBox()
                popup.setIcon(QMessageBox.Information)
                popup.setText("Successfully assigned print to printer")
                popup.setWindowTitle("Assigned print to printer")
                popup.exec_()
            else:
                popup = QMessageBox()
                popup.setIcon(QMessageBox.Critical)
                popup.setText("Select print")
                popup.setWindowTitle("Error - print not selected")
                popup.exec_()

        else:
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Critical)
            popup.setText("Select printer")
            popup.setWindowTitle("Error - printer not selected")
            popup.exec_()

    def assign_print_button_trigger(self):
        self.hide_all()
        self.show_assign_print_layout()

    def what_is_printed_button_trigger(self):
        self.hide_all()
        self.show_what_is_printed_layout()

    def finish_print_button_trigger(self):
        self.hide_all()
        self.show_finish_print_layout()

    def finish_print_apply_button_trigger(self):

        manufacturer = str(self.finish_print_filo_manufacturer_select.currentText())
        diameter = str(self.finish_print_filo_diameter_select.currentText())
        type = str(self.finish_print_filo_type_select.currentText())
        color = str(self.finish_print_filo_color_select.currentText())

        amount = str(self.finish_print_filo_amount_select.text())
        if len(amount) != 0:
            amount = str((float(amount)) / 1000)
        filament_id = str(self.find_filament_id(manufacturer, diameter, type, color))
        if filament_id == '-1':
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Critical)
            popup.setText("There is no such filament")
            popup.setWindowTitle("No filament")
            popup.exec_()
            return

        date = str(datetime.datetime.now()).split('.')[0]

        if len(amount) == 0:
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Critical)
            popup.setText("Please set amount of used filament")
            popup.setWindowTitle("No filament amount error")
            popup.exec_()
            return


        if self.busy_printers_field.currentItem() is not None:
            now = datetime.datetime.now()

            print_id = self.busy_printers_field.currentItem().text().split(',')[0]
            SQL_command = "UPDATE print_3d SET completion_date = '" + \
                                str(now)[0:10] + "' WHERE printer_id = " + \
                                print_id + "AND completion_date IS NULL"
            cursor = self.db_connection.cursor()
            cursor.execute(SQL_command)
            cursor.commit()
            self.hide_finish_print_layout()
            self.show_finish_print_layout()
        else:
            popup = QMessageBox()
            popup.setIcon(QMessageBox.Critical)
            popup.setText("Please select a printer")
            popup.setWindowTitle("No printer selected")
            popup.exec_()
            return

        SQL_command = "INSERT INTO filament_history (filament_id, order_date, delivered_date, added_amount) VALUES (" \
                      + filament_id + ", '" + date + "', '" + date + "', -" + amount + ')'
        cursor = self.db_connection.cursor()
        cursor.execute(SQL_command)
        cursor.commit()

        popup = QMessageBox()
        popup.setIcon(QMessageBox.Information)
        popup.setText("Successfully finished print")
        popup.setWindowTitle("Finished print")
        popup.exec_()

    def customer_leaderboards_button_trigger(self):
        self.hide_all()
        self.show_customer_leaderboards_layout()

    def logout_button_trigger(self):
        self.destroy()
        exit(0)