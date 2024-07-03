
from BasicPrinter import BasicPrinter
from AdvancePrinter import AdvancePrinter

if __name__ == "__main__":
    print("***A demo that follows the ISP.***\n")
    
    basic_printer = BasicPrinter()
    advance_printer = AdvancePrinter()

    basic_printer.printDocument()
    advance_printer.printDocument()
    advance_printer.sendFax()