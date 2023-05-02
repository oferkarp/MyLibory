# Imoprts
from class_Loans import LoanList
from class_Book import BookList
from class_Customers import CustomerList
from constant import FILE_BOOKS, FILE_CUSTOMER, FILE_LOANS, Menu

# Initializes the variables
Books_members = BookList()
Books_members.load_all_books(FILE_BOOKS)
Customer_members = CustomerList()
Customer_members.load_all_customer(FILE_CUSTOMER)
loans_members = LoanList()
loans_members.load_all_loans(FILE_LOANS)

# main project
while True:
    print("****************************")
    print("***Welcome to the library***")
    print("****************************")
    print("What is your command?")
    print("1.Add a new customer")
    print("2.Display all customers")
    print("3.Find customer by name")
    print("4.Remove customer")
    print("5.Add a new book")
    print("6.Display all books")
    print("7.Find book by name")
    print("8.Remove book")
    print("9.Loan a book")
    print("10.Return a book")
    print("11.Display all loans")
    print("12.Display late loans")
    print("13.Exit")

    command = input("Enter your command: ")

    if command == Menu.ADD_A_NEW_CUSTOMER.value:
        Customer_members.add_new_customer(customerdata=Customer_members)
    elif command == Menu.DISPLAY_ALL_CUSTOMERS.value:
        print(Customer_members)
    elif command == Menu.FIND_CUSTOMER_BY_NAME.value:
        Customer_members.search_customer()
    elif command == Menu.REMOVE_CUSTOMER.value:
        Customer_members.remove_customer()
    elif command == Menu.ADD_A_NEW_BOOK.value:
        Books_members.add_new_book(bookdata=Books_members)
    elif command == Menu.DISPLAY_ALL_BOOKS.value:
        print(Books_members)
    elif command == Menu.FIND_BOOK_BY_NAME.value:
        Books_members.search_book()
    elif command == Menu.REMOVE_BOOK.value:
        Books_members.remove_book()
    elif command == Menu.LOAN_A_BOOK.value:
        loans_members.add_new_loan(loandata=loans_members)
    elif command == Menu.RETURN_A_BOOK.value:
        loans_members.remove_loan()
    elif command == Menu.DISPLAY_ALL_LOANS.value:
        print(loans_members)
    elif command == Menu.DISPLAY_LATE_LOANS.value:
        loans_members.display_late_loans()
    elif command == Menu.EXIT.value:
        break



