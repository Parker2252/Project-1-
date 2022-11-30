from PyQt5.QtWidgets import *
from view import *
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the submit and clear button.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_submit.clicked.connect(lambda: self.submit())
        self.pushButton_clear.clicked.connect(lambda: self.clear())

    def submit(self):
        """
        This function does the calculations after button is pressed and displays the output.
        :return: The calculations into the label summary.
        """
        try:
            food = float(self.lineEdit_food.text())
            drink = float(self.lineEdit_drink.text())
            dessert = float(self.lineEdit_dessert.text())
            participants = int(self.lineEdit_participants.text())
            tip = float(self.lineEdit_tip.text())
            round_pay = self.radioButton_round_up.isChecked()
            tax = (food + drink + dessert) * .10
            tip = tip / 100
            total_tip = (tax + (food + drink + dessert)) * tip / participants
            total = food + drink + dessert + tax + total_tip

            if round_pay is True:
                total = math.ceil(total)
            per_person = total / participants

            self.label_summary.setText(f'{"SUMMARY":^25}  \n\n'
                                       f'Food: {"$":>10}{food:.2f}\n'
                                       f'Drink: {"$":>10}{drink:.2f}\n'
                                       f'Dessert: {"$":>7}{dessert:.2f}\n'
                                       f'Tax: {"$":>12}{tax:.2f}\n'
                                       f'Tip: {"$":>12}{total_tip:.2f}\n\n'
                                       f'Total: {"$":>10}{total:.2f}\n'
                                       f'Per person: {"$":>5}{per_person:.2f} ')

        # If not given an int or float will return error
        except ValueError:
            self.label_summary.setText('Food, drink, dessert\n'
                                       'and tip need to be numeric\n'
                                       'e.g. 10.25 not %10.25\n'
                                       'Participants must be whole\n'
                                       'number')

    def clear(self) -> bool:
        """
        :return: Clears all buttons that were checked when clear button is pressed. Then sets participants button back to 1 and tip to 10%.
        """
        self.lineEdit_food.clear()
        self.lineEdit_drink.clear()
        self.lineEdit_dessert.clear()
        self.lineEdit_participants.clear()
        self.lineEdit_tip.clear()
        self.radioButton_round_up.setAutoExclusive(False)
        self.radioButton_round_up.setChecked(False)
        self.radioButton_round_up.setAutoExclusive(True)
        self.label_summary.clear()
        return
