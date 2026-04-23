from PyQt6.QtWidgets import *
import csv
from gui2 import *
import os
from datetime import datetime
from PyQt6.QtCore import QDate


#this class handles all widget behavior and logic
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''
        This function creates an instance of the Logic class
        It is responsible for validating all values and exporting to a csv file
        '''
        super().__init__()
        self.setupUi(self)
        now = datetime.now().strftime('%H%M')
        self.current_time = now
        self.real_time.display(now)
        self.submit_button.clicked.connect(self.check_valid)

    def check_name(self):
        '''
        This function checks if names are valid
        and that there are no numbers
        It then calls the check_date function
        '''
        if self.entry_name.text().strip() == '':
            self.name_error.setText('Please enter a name')
            return False
        else:
            for char in self.entry_name.text():
                if char.isdigit():
                    self.name_error.setText('No digits allowed')
                    return False
                elif not char.strip().replace(' ', '').isalpha():
                    self.name_error.setText('No special characters allowed')
                    return False
            self.name_error.setText('')
            return True
    def check_date(self):
        '''
        This function checks if the date is entered in appropriate format
        and if the date is a real date
        It then calls the check_reason function
        '''
        day = self.date.selectedDate()
        if day != QDate.currentDate():
            self.date_error.setText('Please select today\'s date')
            return False
        else:
            self.date_error.setText('')
            return True

    def check_reason(self):
        '''This function simply checks if a value was entered at all
        Then calls the save function
        '''
        if self.reason_text.toPlainText().strip() == '':
            self.reason_error.setText('Please enter a reason')
            return False
        else:
            self.reason_error.setText('')
            return True

    def check_valid(self):
        self.current_time = datetime.now().strftime('%H%M')
        self.real_time.display(self.current_time)
        name = self.check_name()
        date = self.check_date()
        reason = self.check_reason()
        if name and date and reason:
            self.messageBoard.setText('')
            self.save()
        else:
            self.messageBoard.setText('Please correct errors')

    def save(self):
        '''This function takes all input fields and the check box
        and appends/adds them to a csv file
        It then clears all fields and posts a saved message
        '''
        file_exists = os.path.isfile('log_in.csv')
        with open('log_in.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists or os.path.getsize('log_in.csv') == 0:
                writer.writerow(['Name', 'Date', 'Time', 'Reason', 'Follow-Up'])
            writer.writerow([
                self.entry_name.text(),
                self.date.selectedDate().toString('ddMMM').upper(),
                self.current_time,
                self.reason_text.toPlainText(),
                self.checkYes.isChecked()
            ])
        self.entry_name.clear()
        self.reason_text.clear()
        self.checkYes.setChecked(False)
        self.messageBoard.setText('Saved!')