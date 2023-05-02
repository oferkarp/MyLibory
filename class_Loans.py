import json
from datetime import datetime, timedelta
from class_Book import BookList
from class_Customers import CustomerList
from constant import FILE_LOANS

class Loans:
    def __init__(self, customer_id, book_id, loan_date, return_date):
        self.customer_id = customer_id
        self.book_id = book_id 
        self.loan_date = loan_date
        self.return_date = return_date

    def __str__(self):
        return f"loan id is:{self.customer_id}, the book id:{self.book_id}, the loan date start: {self.loan_date}, the return date: {self.return_date}"

class LoanList:
    all_loans = [] 
    
    def add_loan(self, loan):
        self.all_loans.append(loan)

    @staticmethod
    def load_all_loans(fillename):
        # reading the file
        with open(fillename) as f:
            all_file_json = json.load(f)

        # turn into objects
        for single_json in all_file_json:
            loan = Loans(**single_json)
            LoanList.all_loans.append(loan)

    @staticmethod
    def save_all_loans(fillename):
        new_list = []
        for loan in LoanList.all_loans:
            new_list.append(loan.__dict__)
        with open(fillename,"w") as f:        
            json.dump(new_list, f)

#The function add_new_loan adds loans, and checks at the beginning that a 
# loan whose ID not exists in the system has not been entered to the fille.
# and also check that he take valid book.
# than the client enter date and we check that a valid date and than use the 
# function get_max_loan_days to return how much they loan the book.

    def add_new_loan(self, loandata):
        new_list_id = []
        loan_book_id = []
        book_list_id = []
        for customer in CustomerList.all_customers:
            new_list_id.append(customer.id)
        for loan in LoanList.all_loans:
            loan_book_id.append(loan.book_id)
        for book in BookList.all_books:
            book_list_id.append(book.id)
        id = input("Enter customer id:")
        while True:
            if id in new_list_id:
                break
            else:
                id = input("There is no such id on customer list id, please enter new id:")
        book = input("Enter book id you want to loan:")
        while True:
            if (book not in loan_book_id) and (book in book_list_id):
                break
            else:
                book = input("The book id is already on loan or not exist, please enter new book id:")
        while True:
            try:
                year = int(input("Enter year loan:"))
                month = int(input("Enter month loan:"))
                day = int(input("Enter day loan:"))
                Loandate = datetime(year,month,day)
                break
            except ValueError:
                print("Invalid date entered. Please try again.")
        for book_type in BookList.all_books:
            if book_type.id == book:
                days_loans = book_type.get_max_loan_days()
        Returndate = Loandate + timedelta(days=int(days_loans))
        loan = Loans(customer_id = id, book_id = book, loan_date = Loandate.isoformat(), return_date=Returndate.isoformat())
        loandata.add_loan(loan)
        loandata.save_all_loans(FILE_LOANS)
        print("---loan added successfully.---") 

    def remove_loan(self):
        book_id_return = input("Enter book id you want to return:")
        found = False
        for loan in self.all_loans:
            if loan.book_id == book_id_return:
                self.all_loans.remove(loan)
                LoanList.save_all_loans(FILE_LOANS)
                print("---Loan customer was remove successfully.---")
                found = True
                break
        if not found:
            print(f"---book with id {book_id_return} has not in loan.---")

    def display_late_loans(self):
        for loan in self.all_loans:
            return_date = datetime.strptime(loan.return_date, "%Y-%m-%dT%H:%M:%S")
            if return_date < datetime.now():
                print(loan)

    def __str__(self):
        ret_str = ""
        for loan in self.all_loans:
            ret_str += str(loan) + "\n"
        return ret_str     
    











