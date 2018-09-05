import sys
from PyQt5.QtWidgets import QApplication, QWidget
from pyqt_app.LoginWindow import LoginWindow
from pyqt_app.CustomerWindow import CustomerWindow
from pyqt_app.AdminWindow import AdminWindow
import pyodbc


app = QApplication(sys.argv)

db_connection = pyodbc.connect(
    'DRIVER={ODBC Driver 11 for SQL Server};SERVER=REALITYISFALSE0;DATABASE=Printers3D;UID=user;PWD=password')

w = LoginWindow(db_connection)

w.show()
sys.exit(app.exec_())
