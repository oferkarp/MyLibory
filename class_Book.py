import json
from enum import Enum
from constant import FILE_BOOKS


class Books:
    # constant varible
    class Book_type(Enum):
        TYPE_10_DAY = '1'
        TYPE_5_DAY = '2'
        TYPE_2_DAY = '3'

    def __init__(self, id, name, author, published, type):
        self.id = id
        self.name = name
        self.author = author
        self.published = published
        self.type = type

    # use the constant to to check which type is the book and return the day of loan 
    def get_max_loan_days(self):
        if self.type == Books.Book_type.TYPE_10_DAY.value:
            return 10
        elif self.type == Books.Book_type.TYPE_5_DAY.value:
            return 5
        elif self.type == Books.Book_type.TYPE_2_DAY.value:
            return 2

    def __str__(self):
        return f"The Book name is:{self.name}, is id:{self.id}, the author is:{self.author}, published in:{self.published},type book is:{self.type}"


class BookList:
    all_books = []

    def add_book(self, book):
        self.all_books.append(book)

    @staticmethod
    def load_all_books(fillename):
        # reading the file
        with open(fillename) as f:
            all_file_json = json.load(f)

        # turn into objects
        for single_json in all_file_json:
            book = Books(**single_json)
            BookList.all_books.append(book)

    @staticmethod
    def save_all_books(fillename):
        new_list = []
        for book in BookList.all_books:
            new_list.append(book.__dict__)
        with open(fillename, "w") as f:
            json.dump(new_list, f)

#The function add_new_book adds books, and checks at the beginning that a 
# book whose ID and name already exists in the system has not been entered to the fille.
# after the check we get the type of the book only 1,2,3 valid.

    def add_new_book(self, bookdata):
        new_list_id = []
        new_list_name = []
        for book in BookList.all_books:
            new_list_id.append(book.id)
            new_list_name.append(book.name.lower())
        id = input("Enter book id:")
        while True:
            if id not in new_list_id:
                break
            else:
                id = input("The id book is already taken please enter new id:")
        name = input("Enter book name:")
        while True:
            if name.lower() not in new_list_name:
                break
            else:
                name = input(
                    "The book name is already exist please enter new book:")
        author = input("Enter author name:")
        published = input("When the book was published:")
        while True:
            print("Set the book type the maximum loan time for book:")
            print("1 - up to 10 days")
            print("2 - up to 5 days")
            print("3 - up to 2 days")
            book_type = input()
            if book_type in ['1', '2', '3']:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        book = Books(id=id, name=name, author=author,
                     published=published, type=book_type)
        bookdata.add_book(book)
        bookdata.save_all_books(FILE_BOOKS)
        print("---Book added successfully.---")

    def remove_book(self):
        book_remove = input("Enter book name you want to remove:")
        found = False
        for book in self.all_books:
            if book.name.lower() == book_remove.lower():
                self.all_books.remove(book)
                BookList.save_all_books(FILE_BOOKS)
                print("---Book remove successfully.---")
                found = True
                break
        if not found:
            print(f"---Book with name {book_remove} not found.---")

    def search_book(self):
        book_search = input("Enter book name you want to search:")
        found = False
        for book in self.all_books:
            if book.name.lower() == book_search.lower():
                print(book)
                found = True
                break
        if not found:
            print(f"---Book with name {book_search} not found.---")

    def __str__(self):
        ret_str = ""
        for book in self.all_books:
            ret_str += str(book) + "\n"
        return ret_str
