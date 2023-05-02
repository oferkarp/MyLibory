from enum import Enum

FILE_BOOKS = "books.json"
FILE_CUSTOMER = "customer.json"
FILE_LOANS = "loans.json"

'''
constant varible menu for the main class
'''

class Menu(Enum):
    ADD_A_NEW_CUSTOMER = '1'
    DISPLAY_ALL_CUSTOMERS = '2'
    FIND_CUSTOMER_BY_NAME = '3'
    REMOVE_CUSTOMER = '4'
    ADD_A_NEW_BOOK = '5'
    DISPLAY_ALL_BOOKS = '6'
    FIND_BOOK_BY_NAME = '7'
    REMOVE_BOOK = '8'
    LOAN_A_BOOK = '9'
    RETURN_A_BOOK = '10'
    DISPLAY_ALL_LOANS = '11'
    DISPLAY_LATE_LOANS = '12'
    EXIT = '13'