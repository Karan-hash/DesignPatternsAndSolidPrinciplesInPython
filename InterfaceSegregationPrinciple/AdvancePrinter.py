from Printer import Printer
from FaxDevice import FaxDevice


class AdvancePrinter(FaxDevice):
    def printDocument(self):
        print("The advanced printer prints a document.")

    def sendFax(self):
        print("The advanced printer sends a fax.")
