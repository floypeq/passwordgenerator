import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
import random
import os

passwd_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
password_complete = []

class PasswordGeneratorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.generate_passwords)

    def generate_passwords(self):
        amount_symbols = int(self.textEdit.toPlainText())
        amount_passwords = int(self.textEdit_2.toPlainText())

        for i in range(amount_passwords):
            random.shuffle(passwd_list)
            join = "".join(passwd_list)
            passwd = join[0:amount_symbols]
            password_complete.append(passwd)

        result = "\n".join(password_complete)
        self.textBrowser.setText(result)

        with open('C:/users/super/desktop/passwordgenrated.txt', 'w') as file:
            for i in password_complete:
                file.write(f"{i}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorWindow()
    window.show()
    sys.exit(app.exec_())


