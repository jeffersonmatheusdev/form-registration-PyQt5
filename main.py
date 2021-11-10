import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QMessageBox
from CRUD.main import CRUD

class userReg(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Registration Form'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.initUI()
        self.db = CRUD()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QFormLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Enter your name')
        self.layout.addRow('Name:', self.name)

        self.age = QLineEdit(self)
        self.age.setPlaceholderText('Enter your age')
        self.layout.addRow('Age:', self.age)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText('Enter your email')
        self.layout.addRow('Email:', self.email)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText('Enter your password')
        self.password.setEchoMode(QLineEdit.Password)
        self.layout.addRow('Password:', self.password)

        self.submit = QPushButton('Register', self)
        self.submit.clicked.connect(self.submitForm)
        self.layout.addWidget(self.submit)

        self.clear = QPushButton('Clear', self)
        self.clear.clicked.connect(self.clearForm)
        self.layout.addWidget(self.clear)

        self.exit = QPushButton('Exit', self)
        self.exit.clicked.connect(self.exitForm)
        self.layout.addWidget(self.exit)
        self.setLayout(self.layout)

    def submitForm(self):
        name = self.name.text()
        age = self.age.text()
        email = self.email.text()
        password = self.password.text()

        if name == '' or age == '' or email == '':
            QMessageBox.warning(self, 'Warning', 'Please fill in all the fields')
        else:
            if len(self.db.select(email)) != 0:
                QMessageBox.warning(self, 'Warning', 'Email already exists')
            else:
                self.db.insert(name, age, email, password)
                QMessageBox.information(self, 'Success', 'Registration successful')
                self.clearForm()

    def clearForm(self):
        self.name.setText('')
        self.age.setText('')
        self.email.setText('')
        self.password.setText('')

    def exitForm(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = userReg()
    ex.show()
    sys.exit(app.exec_())