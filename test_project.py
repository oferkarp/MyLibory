# tests

from class_Book import BookList
from class_Customers import CustomerList
from class_Loans import LoanList
from constant import FILE_BOOKS, FILE_CUSTOMER, FILE_LOANS

#  Test functions that check the initialization of the files

def test_load_customer():
    CustomerList.load_all_customer(FILE_CUSTOMER)
    assert CustomerList.all_customers[0].id == "1"
    assert CustomerList.all_customers[0].name == "Bob Johnson"
    assert CustomerList.all_customers[0].city == "Chicago"
    assert CustomerList.all_customers[0].age == "42"
    print("test check load customer is ok")


def test_load_book():
    BookList.load_all_books(FILE_BOOKS)
    assert BookList.all_books[0].id == "1"
    assert BookList.all_books[0].name == "The Great Gatsby"
    assert BookList.all_books[0].author == "F. Scott Fitzgerald"
    assert BookList.all_books[0].published == "1925"
    assert BookList.all_books[0].type == "1"
    print("test check load books is ok")


def test_load_loan():
    LoanList.load_all_loans(FILE_LOANS)
    assert LoanList.all_loans[0].customer_id == "14"
    assert LoanList.all_loans[0].book_id == "17"
    assert LoanList.all_loans[0].loan_date == "2021-05-03T00:00:00"
    assert LoanList.all_loans[0].return_date == "2021-05-13T00:00:00"
    print("test check load loan is ok")


if __name__ == '__main__':
    test_load_customer()
    test_load_book()
    test_load_loan()
    
